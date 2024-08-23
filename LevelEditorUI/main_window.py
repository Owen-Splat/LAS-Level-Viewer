from PySide6 import QtCore, QtWidgets, QtGui
from LevelEditorUI.UI.ui_form import Ui_MainWindow
import LevelEditorCore.Tools.leb as leb
import copy, os, sys, yaml, random

if getattr(sys, "frozen", False):
    RUNNING_FROM_SOURCE = False
    root_path = os.path.dirname(sys.executable)
else:
    RUNNING_FROM_SOURCE = True
    root_path = os.path.dirname(os.path.dirname(__file__))

data_folder = 'LevelEditorCore/Data' if RUNNING_FROM_SOURCE else 'lib/LevelEditorCore/Data'
DATA_PATH = os.path.join(root_path, data_folder)
with open(os.path.join(DATA_PATH, 'actors.yml'), 'r') as f:
    actor_list = yaml.safe_load(f)
with open(os.path.join(DATA_PATH, 'actor_parameters.yml'), 'r') as f:
    ACTOR_PARAMETERS = yaml.safe_load(f)

ACTORS = {}
for i, actor in enumerate(actor_list):
    ACTORS[actor['name']] = hex(i)
ACTOR_IDS = list(ACTORS.values())
ACTOR_NAMES = list(ACTORS.keys())
REQUIRED_ACTORS = [0x185] # MapStatic

icons_folder = 'LevelEditorUi/Icons' if RUNNING_FROM_SOURCE else 'lib/LevelEditorUi/Icons'
ACTOR_ICONS_PATH = os.path.join(root_path, icons_folder, 'Actors')
ACTOR_ICONS = [f.split('.')[0] for f in os.listdir(ACTOR_ICONS_PATH) if f.endswith('.png')]
TILE_ICONS_PATH = os.path.join(root_path, icons_folder, 'Tiles')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super (MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        self.file = ''
        self.file_loaded = False
        self.save_location = ''
        self.data_viewed = False
        self.room_data = None
        self.current_actor = -1
        self.next_actor = -1
        self.current_section = -1
        self.current_entry = -1
        self.deleted = False
        self.manual_editing = False
        self.drawing = False
        self.keys = []
        self.actor_sprites = []
        self.hideEmptySprites = True

        self.ui.hideUnimportantCheck.setChecked(True)
        self.ui.gridWidget.hide()

        self.ui.actionOpen.triggered.connect(self.fileOpen)
        self.ui.actionSave.triggered.connect(self.fileSave)
        self.ui.actionSaveAs.triggered.connect(self.fileSaveAs)
        self.ui.actionClose.triggered.connect(self.fileClose)
        self.ui.listWidget.currentRowChanged.connect(self.selectedActorChanged)
        self.ui.dataType.currentIndexChanged.connect(self.updateActorType)
        self.ui.addButton.clicked.connect(self.copyActor)
        self.ui.delButton.clicked.connect(self.deleteButton_Clicked)
        self.ui.showButton.clicked.connect(self.toggleActor)
        self.ui.hideUnimportantCheck.clicked.connect(self.toggleNoModelObjects)
        self.ui.gridCheck.clicked.connect(self.toggleGrid)

        for line in self.findChildren(QtWidgets.QLineEdit):
            if line.objectName().startswith('dataPos'):
                line.__class__ = PosLineEdit
            elif line.objectName().startswith('dataRot'):
                line.__class__ = RotLineEdit

        self.tiles = []
        for i in range(8):
            for b in range(10):
                tile = QtWidgets.QLabel(self.ui.roomFrame)
                tile.setGeometry((45 * b), (45 * i), 45, 45)
                tile.setStyleSheet("")
                self.tiles.append(tile)
        self.ui.gridWidget.raise_() # raise the grid above the painted tiles

        self.setFixedSize(self.size())
        self.setWindowTitle('LAS Level Editor')
        self.show()


    def fileOpen(self, dragged_file=None) -> None:
        if dragged_file:
            path = dragged_file
        else:
            path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',
                os.path.dirname(self.file) if self.file_loaded else '', "Room files (*.leb)")[0]
            if not path.endswith(".leb"):
                return
        
        self.fileClose()
        self.file = path
        self.manual_editing = False

        try:
            with open(path, 'rb') as f:
                self.room_data = leb.Room(f.read())
        except (FileNotFoundError, ValueError) as e:
            self.showError(e.args[0])
        else:
            self.setWindowTitle(os.path.basename(path))
            self.topleft = [self.room_data.grid.info.x_coord, self.room_data.grid.info.z_coord]

            # draw out the room based on tile data
            if self.room_data.grid.info.room_height == 8:
                self.draw3DRoom()
            else:
                self.draw2DRoom()

            self.file_loaded = True
            self.ui.listWidget.setEnabled(True)
            self.next_actor = 0
            self.drawRoom(toggle_hide=True)


    def fileSave(self) -> None:
        if self.file_loaded:
            path = os.path.dirname(self.file)
            if not os.path.exists(path):
                os.makedirs(path)
            
            self.saveActor(self.ui.listWidget.currentRow())

            try:
                with open(self.file, 'wb') as f:
                    f.write(self.room_data.repack())
            except (ValueError, OverflowError) as e:
                self.showError(e.args[0])
            else:
                message = QtWidgets.QMessageBox()
                message.setWindowTitle('LAS Level Editor')
                message.setText('File saved successfully')
                message.exec()


    def fileSaveAs(self) -> None:
        if self.file_loaded:
            path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File As',
                os.path.join(os.path.dirname(self.file), os.path.basename(self.file)), "Room files (*.leb)")[0]
            
            if path:
                self.saveActor(self.ui.listWidget.currentRow())
                try:
                    actor_keys = []
                    for act in self.room_data.actors:
                        if act.key not in actor_keys:
                            actor_keys.append(act.key)
                        else:
                            raise ValueError('Actors cannot share the same Hex!')
                    with open(path, 'wb') as f:
                        f.write(self.room_data.repack())
                except (ValueError, OverflowError) as e:
                    self.showError(e.args[0])
                else:
                    self.file = path
                    message = QtWidgets.QMessageBox()
                    message.setWindowTitle('LAS Level Editor')
                    message.setText('File saved successfully')
                    message.exec()


    def fileClose(self) -> None:
        self.file = ''
        self.file_loaded = False
        self.save_location = ''
        self.data_viewed = False
        self.room_data = None
        self.current_actor = -1
        self.next_actor = -1
        self.current_section = -1
        self.current_entry = -1
        self.deleted = False
        self.manual_editing = False
        self.drawing = False
        self.keys = []
        self.ui.listWidget.clear()
        self.ui.listWidget.setEnabled(False)
        self.ui.dataType.clear()
        for c in self.ui.groupBox.children():
            c.setEnabled(False)
        for field in self.ui.groupBox.findChildren(QtWidgets.QLineEdit):
            field.setText('')
        for act in self.actor_sprites:
            act.deleteLater()
        self.actor_sprites = []
        for tile in self.tiles:
            tile.clear()
        self.setWindowTitle('Level Editor')


    def selectedActorChanged(self, current_row) -> None:
        if not self.file_loaded or self.drawing or self.deleted:
            return

        if (current_row != -1) and (current_row != self.current_actor):
            self.next_actor = current_row
            self.drawRoom()


    def displayActorInfo(self) -> None:
        if not self.file_loaded:
            return

        self.manual_editing = False

        if not self.data_viewed:
            self.enableEditor()

        if not self.deleted:
            self.saveActor(self.current_actor)
        else:
            self.deleted = False

        self.current_actor = self.ui.listWidget.currentRow() if self.room_data.actors else -1

        if self.current_actor != -1:
            try:
                act = self.room_data.actors[self.current_actor]
            except IndexError:
                return
            else:
                full_name = ACTOR_NAMES[ACTOR_IDS.index(hex(act.type))]
                self.ui.ID_lineEdit.setText(str(act.key))
                self.ui.dataType.setCurrentIndex(
                    self.ui.dataType.findText(full_name, QtCore.Qt.MatchExactly))
                self.ui.dataPos_X.setText(self.removeTrailingZeros(f'{act.posX:.8f}'))
                self.ui.dataPos_Y.setText(self.removeTrailingZeros(f'{act.posY:.8f}'))
                self.ui.dataPos_Z.setText(self.removeTrailingZeros(f'{act.posZ:.8f}'))
                self.ui.dataRot_X.setText(self.removeTrailingZeros(f'{act.rotX:.8f}'))
                self.ui.dataRot_Y.setText(self.removeTrailingZeros(f'{act.rotY:.8f}'))
                self.ui.dataRot_Z.setText(self.removeTrailingZeros(f'{act.rotZ:.8f}'))
                self.ui.dataScale_X.setText(self.removeTrailingZeros(f'{act.scaleX:.8f}'))
                self.ui.dataScale_Y.setText(self.removeTrailingZeros(f'{act.scaleY:.8f}'))
                self.ui.dataScale_Z.setText(self.removeTrailingZeros(f'{act.scaleZ:.8f}'))

                for i in range(8):
                    if isinstance(act.parameters[i], bytes):
                        param = str(act.parameters[i], 'utf-8')
                    elif isinstance(act.parameters[i], float):
                        param = self.removeTrailingZeros(f'{act.parameters[i]:.8f}')
                    else:
                        param = str(act.parameters[i])
                    exec(f'self.ui.dataParameters_{i}.setText(str(param))')
                    exec(f'self.ui.dataParameters_{i}.setPlaceholderText("")')
                    if full_name in ACTOR_PARAMETERS:
                        if i+1 <= len(ACTOR_PARAMETERS[full_name]):
                            param_info = str(ACTOR_PARAMETERS[full_name][i])
                            exec(f'self.ui.dataParameters_{i}.setPlaceholderText(param_info)')

                self.ui.dataSwitches_0.setText(str(act.switches[0][1]))
                self.ui.comboBox.setCurrentIndex(act.switches[0][0])
                self.ui.dataSwitches_1.setText(str(act.switches[1][1]))
                self.ui.comboBox_2.setCurrentIndex(act.switches[1][0])
                self.ui.dataSwitches_2.setText(str(act.switches[2][1]))
                self.ui.comboBox_3.setCurrentIndex(act.switches[2][0])
                self.ui.dataSwitches_3.setText(str(act.switches[3][1]))
                self.ui.comboBox_4.setCurrentIndex(act.switches[3][0])

                # relationships
                self.ui.comboBox_5.setCurrentIndex(act.relationships.is_enemy)
                self.ui.comboBox_6.setCurrentIndex(act.relationships.check_kills)
                self.ui.comboBox_7.setCurrentIndex(act.relationships.is_chamber_enemy)
                self.displayEntryInfo()

        for field in self.ui.groupBox.findChildren(QtWidgets.QLineEdit): # forces QLineEdit to display from leftmost character
            field.home(False)

        # let the GUI know that any further changes are from the user and now should update
        self.manual_editing = True


    def displayEntryInfo(self) -> None:
        act = self.room_data.actors[self.current_actor]
        relationship_info = {}

        relationship_info['Controlled_Actors'] = []
        for entry in act.relationships.section_1:
            params = []
            for param in entry[0]:
                params.append(str(param))
            relationship_info['Controlled_Actors'].append({
                self.room_data.actors[entry[1]].key: {
                    'Parameters': params
                }
            })
        
        relationship_info['Needed_Positions'] = []
        for entry in act.relationships.section_2:
            params = []
            for param in entry[0]:
                params.append(str(param))
            relationship_info['Needed_Positions'].append({
                'Rail_Index': entry[1],
                'Point_Index': entry[2],
                'Parameters': params
            })
        
        relationship_info['Actors_That_Use_Me'] = []
        for entry in act.relationships.section_3:
            relationship_info['Actors_That_Use_Me'].append(self.room_data.actors[entry].key)
        
        self.ui.textEdit.setText(yaml.dump(relationship_info, Dumper=MyDumper, sort_keys=False, default_flow_style=False, indent=4))
    

    def saveEntryData(self) -> None:
        pass


    def saveActor(self, previous=-1) -> None:
        if previous != -1:
            try:
                act = self.room_data.actors[previous]
                act.type = int(ACTORS[self.ui.dataType.currentText()], 16)
                act.posX = float(self.ui.dataPos_X.text())
                act.posY = float(self.ui.dataPos_Y.text())
                act.posZ = float(self.ui.dataPos_Z.text())
                act.rotX = float(self.ui.dataRot_X.text())
                act.rotY = float(self.ui.dataRot_Y.text())
                act.rotZ = float(self.ui.dataRot_Z.text())
                act.scaleX = float(self.ui.dataScale_X.text())
                act.scaleY = float(self.ui.dataScale_Y.text())
                act.scaleZ = float(self.ui.dataScale_Z.text())

                ldict = locals()
                for i in range(8):
                    exec(f"v = self.ui.dataParameters_{i}.text()")
                    if str(ldict['v']).isdigit():
                        act.parameters[i] = int(ldict['v'])
                    else:
                        try:
                            exec(f"act.parameters[i] = float(ldict['v'])")
                        except ValueError:
                            exec(f"act.parameters[i] = bytes(ldict['v'], 'utf-8')")
                
                act.switches[0] = (self.ui.comboBox.currentIndex(), int(self.ui.dataSwitches_0.text()))
                act.switches[1] = (self.ui.comboBox_2.currentIndex(), int(self.ui.dataSwitches_1.text()))
                act.switches[2] = (self.ui.comboBox_3.currentIndex(), int(self.ui.dataSwitches_2.text()))
                act.switches[3] = (self.ui.comboBox_4.currentIndex(), int(self.ui.dataSwitches_3.text()))

                self.saveEntryData()
            
            except ValueError as e:
                print('error at saveActor', f"current actor: {self.current_actor}")
                self.showError(e.args[0])
                self.ui.listWidget.setCurrentRow(previous)
            
            except IndexError:
                pass


    def copyActor(self) -> None:
        """Makes a copy of the currently selected actor. The new actor is then given a unique ID"""

        if self.file_loaded:
            try:
                self.saveActor(self.current_actor)
                act = copy.deepcopy(self.room_data.actors[self.current_actor])
                while act.key in self.keys:
                    act.key = random.getrandbits(64) # the list of keys is updated when calling drawRoom()
                self.room_data.actors.append(act)
                self.next_actor = self.ui.listWidget.count()
                self.drawRoom()
            except ValueError as e:
                self.showError(e.args[0])
            except IndexError:
                pass


    def deleteButton_Clicked(self) -> None:
        if self.file_loaded:
            if self.room_data.actors[self.current_actor].type not in REQUIRED_ACTORS:
                self.deleteActor()
            else:
                if len([act for act in self.room_data.actors if act.type == self.room_data.actors[self.current_actor].type]) > 1:
                    self.deleteActor()
                else:
                    self.showError('Levels require at least 1 actor of this type')


    def deleteActor(self) -> None:
        # before deleting the actor, we need to adjust actor references
        for act in self.room_data.actors:
            i = 0
            while i < len(act.relationships.section_1):
                try:
                    index = act.relationships.section_1[i][1]
                    if index > self.current_actor:
                        act.relationships.section_1[i][1] -=1
                    elif index == self.current_actor:
                        act.relationships.section_1.pop(i)
                        act.relationships.num_entries_1 -= 1
                        continue
                    i += 1
                except IndexError:
                    print('section 1:' + i)

            i = 0
            while i < len(act.relationships.section_3):
                try:
                    index = act.relationships.section_3[i]
                    if index > self.current_actor:
                        act.relationships.section_3[i] -= 1
                    elif index == self.current_actor:
                        act.relationships.section_3.pop(i)
                        act.relationships.num_entries_3 -= 1
                        continue
                    i += 1
                except IndexError:
                    print('section 3:' + i)

        self.keys.remove(self.room_data.actors[self.current_actor].key)
        del self.room_data.actors[self.current_actor]
        if self.current_actor == self.ui.listWidget.count() - 1:
            self.next_actor = self.current_actor - 1
        self.deleted = True
        self.drawRoom()


    def toggleActor(self) -> None:
        if self.room_data == None:
            return
        act = self.room_data.actors[self.current_actor]
        act.visible = not act.visible
        self.drawRoom()


    def toggleShowButton(self) -> None:
        if self.current_actor == -1:
            return
        if self.room_data.actors[self.current_actor].visible:
            self.ui.showButton.setText("Hide")
        else:
            self.ui.showButton.setText("Show")


    def toggleNoModelObjects(self) -> None:
        self.hideEmptySprites = self.ui.hideUnimportantCheck.isChecked()
        self.drawRoom(toggle_hide=True)


    def toggleGrid(self) -> None:
        if self.ui.gridCheck.isChecked():
            self.ui.gridWidget.show()
        else:
            self.ui.gridWidget.hide()


    def updateActorType(self) -> None:
        """Runs when the type field is edited and updates the actor"""

        if not self.manual_editing: # only change actor type when the user actually manually edits
            return

        act = self.room_data.actors[self.current_actor]
        new_type = ACTOR_NAMES.index(self.ui.dataType.currentText())

        if new_type == act.type: # do not do anything if the type is not being changed
            return

        if not self.room_data.actors[self.current_actor].type in REQUIRED_ACTORS:
            act.type = new_type
        else:
            if len([act for act in self.room_data.actors if act.type == self.room_data.actors[self.current_actor].type]) > 1:
                act.type = new_type
            else:
                self.showError('Levels require at least 1 actor of this type')
                self.ui.dataType.setCurrentIndex(
                    self.ui.dataType.findText(ACTOR_NAMES[ACTOR_IDS.index(hex(act.type))], QtCore.Qt.MatchExactly))

        self.drawRoom()


    def enableEditor(self) -> None:
        fields = [f for f in self.ui.tab.children()]
        fields += [f for f in self.ui.groupBox.children()]
        fields += [f for f in self.ui.tab_2.children()]
        for field in fields:
            field.setProperty('enabled', True)
        abc_actors = list(copy.deepcopy(ACTORS))
        abc_actors.sort()
        for actor in abc_actors:
            if not actor.startswith(('Player', 'null')):
                self.ui.dataType.addItem(actor)
        self.data_viewed = True


    def removeTrailingZeros(self, dec: str) -> str:
        """Removes trailing zeros in float strings"""

        dec_list = [c for c in dec]
        dec_list.reverse()
        dec_list_2 = dec_list.copy()
        
        for d in dec_list_2:
            if d == '0':
                dec_list.remove(d)
            else:
                break
        
        dec_str = ''
        dec_list.reverse()
        for d in dec_list:
            dec_str += d
        
        if dec_str.endswith('.'):
            dec_str += '0'
        
        return dec_str


    def showError(self, error_message) -> None:
        """Opens a new QMessageBox with error_message as the text"""

        message = QtWidgets.QMessageBox()
        message.setWindowTitle('LAS Level Editor')
        message.setText(error_message)
        message.exec()


    def dragEnterEvent(self, event) -> None:
        """Allows dragging level files into this tool. Dropping the file is handled in dropEvent()"""

        if event.mimeData().hasUrls():
            links = [str(l.toLocalFile()) for l in event.mimeData().urls() if l.toLocalFile().endswith(".leb")]
            if links:
                event.accept()
                return
        event.ignore()


    def dropEvent(self, event) -> None:
        """Allows dropping level files into this tool. Dragging the file is handed in dragEnterEvent()"""

        event.accept()
        link = [str(l.toLocalFile()) for l in event.mimeData().urls() if l.toLocalFile().endswith(".leb")][0]
        self.fileOpen(link)


    def drawRoom(self, toggle_hide=False) -> None:
        """Updates actor info and draws basic sprites to represent the room and its actors"""

        if self.room_data == None:
            return

        self.drawing = True

        # delete old actor sprites
        for act in self.actor_sprites:
            act.deleteLater()
        self.actor_sprites = []

        # redraw actor list
        self.keys.clear()
        self.ui.listWidget.clear()
        for act in self.room_data.actors:
            self.keys.append(act.key)
            self.ui.listWidget.addItem(ACTOR_NAMES[ACTOR_IDS.index(hex(act.type))])
        if self.current_actor >= 0:
            self.ui.listWidget.setCurrentRow(self.next_actor)
        else:
            self.ui.listWidget.setCurrentRow(0)

        # display the info of the currently selected actor
        self.displayActorInfo()

        # now draw the actor sprites
        current_sprite = None
        enemy_sprites = []
        for i, act in enumerate(self.room_data.actors):
            if i == self.current_actor:
                sprite = SelectedLabel(self.ui.roomFrame)
            else:
                sprite = QtWidgets.QLabel(self.ui.roomFrame)

            # define the sprite name and create a pixmap out of it
            name = self.ui.listWidget.item(i).text()
            if name in ACTOR_ICONS:
                pix = QtGui.QPixmap(os.path.join(ACTOR_ICONS_PATH, f"{name}.png"))
            else:
                pix = QtGui.QPixmap(os.path.join(ACTOR_ICONS_PATH, "NoSprite.png"))
                # if "hide objects without sprites" was just toggled, set the visible variable
                if toggle_hide:
                    act.visible = not self.hideEmptySprites

            # create refs of enemy sprites to raise above other actors
            if name.startswith('Enemy'):
                enemy_sprites.append(sprite)

            # rotate sprite, will need to create a mapping of actors and default rotations
            # trans = QtGui.QTransform()
            # trans.rotate(act.rotY * -1)
            # pix = pix.transformed(trans)

            # add sprite and scale it
            sprite.setPixmap(pix)
            sprite.setScaledContents(True)

            # define geometry
            posX = round(((act.posX - self.topleft[0]) * 30) - 22.5)

            if self.room_data.grid.info.room_height == 8: # 3D room
                posY = round(((act.posZ - self.topleft[1]) * 30) - 22.5)
            else: # 2D room
                posY = round((12 - act.posY) * 30)

            sprite.setGeometry(posX, posY, 45, 45)

            # add sprite to a reference list so we can delete it before a redraw
            self.actor_sprites.append(sprite)

            # create reference to the sprite of the currently selected actor
            if i == self.current_actor:
                current_sprite = sprite

            # only show the sprite if it's not hidden
            if act.visible:
                sprite.show()

        # raise enemy sprites
        for spr in enemy_sprites:
            spr.raise_()

        # raise the currently selected actor's sprite above everything else
        if current_sprite != None:
            current_sprite.raise_()

        self.toggleShowButton()
        self.drawing = False


    def draw3DRoom(self) -> None:
        """Draws out the sprites to represent a 3D room from a top-down view"""

        for i, tile in enumerate(self.room_data.grid.tilesdata):
            v_tile: QtWidgets.QLabel = self.tiles[i]
            v_tile.setPixmap(QtGui.QPixmap(os.path.join(TILE_ICONS_PATH, f"{self.getTileSprite(tile)}.png")))
            v_tile.setScaledContents(True)


    def draw2DRoom(self) -> None:
        """Draws out the sprites to represent a 2D room from a front-facing view"""

        # we do not care about the z-axis technically being 2 tiles long, so we only look at half the tile data
        # tile_data = self.room_data.grid.tilesdata
        # tile_data = tile_data[:int(len(tile_data) / 2)]
        for i, tile in enumerate(self.room_data.grid.tilesdata):
            spr = self.getTileSprite(tile)
            pos = int(i + 80 - (10 * (tile.elevation // 1.5))) - 10
            if spr == "Wall" and str(pos)[-1] in ("0", "9"): # walls need to go up all the way
                pos = int(str(pos)[-1])
            while pos < 80:
                v_tile: QtWidgets.QLabel = self.tiles[pos]
                v_tile.setPixmap(QtGui.QPixmap(os.path.join(TILE_ICONS_PATH, f"{spr}.png")))
                v_tile.setScaledContents(True)
                pos += 10


    def getTileSprite(self, tile) -> str:
        """Determines the sprite by reading the tile's data, and returns the pixmap"""

        contains_collision: bool = tile.flags1['containscollision']
        deep_water: bool = tile.flags1['deepwaterlava']
        is_water: bool = tile.flags3['iswaterlava']
        can_dig: bool = tile.flags3['isdigspot']
        tile_sprite = 'Walkable' #"#e5cc8f"

        # Some tiles contain collision for actors. By checking can_dig & is_water, we can elim most
        if contains_collision and (not can_dig or not is_water):
            tile_sprite = 'Wall' #"#775c2e"
        else:
            if deep_water:
                tile_sprite = 'Water' #"#6b7d63"
                if not is_water:
                    tile_sprite = 'Hole' #"black"
            elif is_water:
                tile_sprite = 'ShallowWater' #"#8a9b75"

        return tile_sprite


class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


class PosLineEdit(QtWidgets.QLineEdit):
    """Allows moving the actor by using the arrow keys

    These directions go from negative to positive:
        X-axis: West -> East
        Y-axis: Down -> Up
        Z-axis: North -> South"""

    DIRECTIONS = {
        'X': (QtCore.Qt.Key_Left, QtCore.Qt.Key_Right),
        'Y': (QtCore.Qt.Key_Down, QtCore.Qt.Key_Up),
        'Z': (QtCore.Qt.Key_Up, QtCore.Qt.Key_Down)
    }

    def keyPressEvent(self, event) -> None:
        super().keyPressEvent(event)
        self.moveTile(event.key())

    def moveTile(self, key) -> None:
        try:
            pos = float(self.text())
        except ValueError:
            return

        dirs = self.DIRECTIONS[self.objectName()[-1]]
        if key == dirs[0]:
            amount = -1.5
        elif key == dirs[1]:
            amount = 1.5
        else:
            return

        self.setText(str(pos + amount))
        self.window().drawRoom()


class RotLineEdit(QtWidgets.QLineEdit):
    """Allows rotating the actor by using the arrow keys

    Rotating on the Y-axis is what we want to use in 99% of situations. The direction should be self explanatory

    Some actors have natural rotations that differ from most, but this tool automatically adjusts for them"""

    def keyPressEvent(self, event) -> None:
        super().keyPressEvent(event)
        self.rotateTile(event.key())

    def rotateTile(self, key) -> None:
        if key == QtCore.Qt.Key_Down:
            rot = 0.0
        elif key == QtCore.Qt.Key_Right:
            rot = 90.0
        elif key == QtCore.Qt.Key_Up:
            rot = 180.0
        elif key == QtCore.Qt.Key_Left:
            rot = -90.0
        else:
            return

        self.setText(str(rot))
        self.window().drawRoom()


class SelectedLabel(QtWidgets.QLabel):
    """A custom QLabel that flashes its opacity to indicate focus on this object"""

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setParent(parent)

        effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.anim_1 = QtCore.QPropertyAnimation(effect, b"opacity")
        self.anim_1.finished.connect(self.startAnimation)
        self.anim_1.setDuration(750)
        self.values = [0.65, 1.0]
        self.startAnimation()

    def startAnimation(self) -> None:
        """Reverses the animation start & end values each time before running"""

        self.anim_1.setStartValue(self.values[0])
        self.anim_1.setEndValue(self.values[1])
        self.values.reverse()
        self.anim_1.start()
