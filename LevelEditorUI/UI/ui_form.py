# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QSize(1200, 600))
        MainWindow.setBaseSize(QSize(800, 600))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionActors = QAction(MainWindow)
        self.actionActors.setObjectName(u"actionActors")
        self.actionPoints = QAction(MainWindow)
        self.actionPoints.setObjectName(u"actionPoints")
        self.actionRails = QAction(MainWindow)
        self.actionRails.setObjectName(u"actionRails")
        self.actionGrid = QAction(MainWindow)
        self.actionGrid.setObjectName(u"actionGrid")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 6, 191, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QRect(15, 41, 201, 491))
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(14, 540, 61, 24))
        self.delButton = QPushButton(self.centralwidget)
        self.delButton.setObjectName(u"delButton")
        self.delButton.setGeometry(QRect(80, 540, 61, 24))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(231, 9, 501, 561))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 511, 541))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox#groupBox {border:0;}")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QRect(10, 50, 51, 22))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dataPos_X = QLineEdit(self.groupBox)
        self.dataPos_X.setObjectName(u"dataPos_X")
        self.dataPos_X.setEnabled(False)
        self.dataPos_X.setGeometry(QRect(70, 110, 131, 22))
        font2 = QFont()
        font2.setPointSize(10)
        self.dataPos_X.setFont(font2)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QRect(10, 110, 51, 22))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dataPos_Y = QLineEdit(self.groupBox)
        self.dataPos_Y.setObjectName(u"dataPos_Y")
        self.dataPos_Y.setEnabled(False)
        self.dataPos_Y.setGeometry(QRect(210, 110, 131, 22))
        self.dataPos_Y.setFont(font2)
        self.dataPos_Z = QLineEdit(self.groupBox)
        self.dataPos_Z.setObjectName(u"dataPos_Z")
        self.dataPos_Z.setEnabled(False)
        self.dataPos_Z.setGeometry(QRect(350, 110, 131, 22))
        self.dataPos_Z.setFont(font2)
        self.dataRot_Y = QLineEdit(self.groupBox)
        self.dataRot_Y.setObjectName(u"dataRot_Y")
        self.dataRot_Y.setEnabled(False)
        self.dataRot_Y.setGeometry(QRect(210, 140, 131, 22))
        self.dataRot_Y.setFont(font2)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QRect(10, 140, 51, 22))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dataRot_X = QLineEdit(self.groupBox)
        self.dataRot_X.setObjectName(u"dataRot_X")
        self.dataRot_X.setEnabled(False)
        self.dataRot_X.setGeometry(QRect(70, 140, 131, 22))
        self.dataRot_X.setFont(font2)
        self.dataRot_Z = QLineEdit(self.groupBox)
        self.dataRot_Z.setObjectName(u"dataRot_Z")
        self.dataRot_Z.setEnabled(False)
        self.dataRot_Z.setGeometry(QRect(350, 140, 131, 22))
        self.dataRot_Z.setFont(font2)
        self.dataScale_Y = QLineEdit(self.groupBox)
        self.dataScale_Y.setObjectName(u"dataScale_Y")
        self.dataScale_Y.setEnabled(False)
        self.dataScale_Y.setGeometry(QRect(210, 170, 131, 22))
        self.dataScale_Y.setFont(font2)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QRect(10, 170, 51, 22))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dataScale_X = QLineEdit(self.groupBox)
        self.dataScale_X.setObjectName(u"dataScale_X")
        self.dataScale_X.setEnabled(False)
        self.dataScale_X.setGeometry(QRect(70, 170, 131, 22))
        self.dataScale_X.setFont(font2)
        self.dataScale_Z = QLineEdit(self.groupBox)
        self.dataScale_Z.setObjectName(u"dataScale_Z")
        self.dataScale_Z.setEnabled(False)
        self.dataScale_Z.setGeometry(QRect(350, 170, 131, 22))
        self.dataScale_Z.setFont(font2)
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        self.label_10.setGeometry(QRect(70, 90, 131, 20))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)
        self.label_11.setGeometry(QRect(210, 90, 131, 20))
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QRect(350, 90, 131, 20))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.dataParameters_0 = QLineEdit(self.groupBox)
        self.dataParameters_0.setObjectName(u"dataParameters_0")
        self.dataParameters_0.setEnabled(False)
        self.dataParameters_0.setGeometry(QRect(40, 235, 201, 22))
        self.dataParameters_0.setFont(font1)
        self.dataParameters_1 = QLineEdit(self.groupBox)
        self.dataParameters_1.setObjectName(u"dataParameters_1")
        self.dataParameters_1.setEnabled(False)
        self.dataParameters_1.setGeometry(QRect(280, 235, 201, 22))
        self.dataParameters_1.setFont(font1)
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(False)
        self.label_15.setGeometry(QRect(40, 210, 441, 21))
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.dataParameters_2 = QLineEdit(self.groupBox)
        self.dataParameters_2.setObjectName(u"dataParameters_2")
        self.dataParameters_2.setEnabled(False)
        self.dataParameters_2.setGeometry(QRect(40, 265, 201, 22))
        self.dataParameters_2.setFont(font1)
        self.dataParameters_3 = QLineEdit(self.groupBox)
        self.dataParameters_3.setObjectName(u"dataParameters_3")
        self.dataParameters_3.setEnabled(False)
        self.dataParameters_3.setGeometry(QRect(280, 265, 201, 22))
        self.dataParameters_3.setFont(font1)
        self.dataParameters_6 = QLineEdit(self.groupBox)
        self.dataParameters_6.setObjectName(u"dataParameters_6")
        self.dataParameters_6.setEnabled(False)
        self.dataParameters_6.setGeometry(QRect(40, 325, 201, 22))
        self.dataParameters_6.setFont(font1)
        self.dataParameters_4 = QLineEdit(self.groupBox)
        self.dataParameters_4.setObjectName(u"dataParameters_4")
        self.dataParameters_4.setEnabled(False)
        self.dataParameters_4.setGeometry(QRect(40, 295, 201, 22))
        self.dataParameters_4.setFont(font1)
        self.dataParameters_7 = QLineEdit(self.groupBox)
        self.dataParameters_7.setObjectName(u"dataParameters_7")
        self.dataParameters_7.setEnabled(False)
        self.dataParameters_7.setGeometry(QRect(280, 325, 201, 22))
        self.dataParameters_7.setFont(font1)
        self.dataParameters_5 = QLineEdit(self.groupBox)
        self.dataParameters_5.setObjectName(u"dataParameters_5")
        self.dataParameters_5.setEnabled(False)
        self.dataParameters_5.setGeometry(QRect(280, 295, 201, 22))
        self.dataParameters_5.setFont(font1)
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(False)
        self.label_16.setGeometry(QRect(40, 370, 441, 21))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.dataSwitches_0 = QLineEdit(self.groupBox)
        self.dataSwitches_0.setObjectName(u"dataSwitches_0")
        self.dataSwitches_0.setEnabled(False)
        self.dataSwitches_0.setGeometry(QRect(40, 395, 201, 22))
        self.dataSwitches_0.setFont(font2)
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QRect(280, 395, 201, 22))
        self.comboBox.setFont(font2)
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setEnabled(False)
        self.label_17.setGeometry(QRect(10, 265, 21, 22))
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(False)
        self.label_18.setGeometry(QRect(10, 295, 21, 22))
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setEnabled(False)
        self.label_19.setGeometry(QRect(10, 325, 21, 22))
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setEnabled(False)
        self.label_20.setGeometry(QRect(250, 265, 21, 22))
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setEnabled(False)
        self.label_21.setGeometry(QRect(250, 295, 21, 22))
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(False)
        self.label_22.setGeometry(QRect(250, 325, 21, 22))
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setEnabled(False)
        self.label_23.setGeometry(QRect(10, 235, 21, 22))
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setEnabled(False)
        self.label_24.setGeometry(QRect(250, 235, 21, 22))
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setEnabled(False)
        self.label_25.setGeometry(QRect(10, 395, 21, 22))
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setEnabled(False)
        self.label_26.setGeometry(QRect(10, 425, 21, 22))
        self.label_26.setFont(font1)
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dataSwitches_1 = QLineEdit(self.groupBox)
        self.dataSwitches_1.setObjectName(u"dataSwitches_1")
        self.dataSwitches_1.setEnabled(False)
        self.dataSwitches_1.setGeometry(QRect(40, 425, 201, 22))
        self.dataSwitches_1.setFont(font2)
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setGeometry(QRect(280, 425, 201, 22))
        self.comboBox_2.setFont(font2)
        self.dataSwitches_3 = QLineEdit(self.groupBox)
        self.dataSwitches_3.setObjectName(u"dataSwitches_3")
        self.dataSwitches_3.setEnabled(False)
        self.dataSwitches_3.setGeometry(QRect(40, 485, 201, 22))
        self.dataSwitches_3.setFont(font2)
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setEnabled(False)
        self.label_27.setGeometry(QRect(10, 455, 21, 22))
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setEnabled(False)
        self.label_28.setGeometry(QRect(10, 485, 21, 22))
        self.label_28.setFont(font1)
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.comboBox_4 = QComboBox(self.groupBox)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setEnabled(False)
        self.comboBox_4.setGeometry(QRect(280, 485, 201, 22))
        self.comboBox_4.setFont(font2)
        self.dataSwitches_2 = QLineEdit(self.groupBox)
        self.dataSwitches_2.setObjectName(u"dataSwitches_2")
        self.dataSwitches_2.setEnabled(False)
        self.dataSwitches_2.setGeometry(QRect(40, 455, 201, 22))
        self.dataSwitches_2.setFont(font2)
        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setEnabled(False)
        self.comboBox_3.setGeometry(QRect(280, 455, 201, 22))
        self.comboBox_3.setFont(font2)
        self.dataType = QComboBox(self.groupBox)
        self.dataType.setObjectName(u"dataType")
        self.dataType.setEnabled(False)
        self.dataType.setGeometry(QRect(70, 50, 411, 22))
        self.dataType.setFont(font2)
        self.ID_lineEdit = QLineEdit(self.groupBox)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")
        self.ID_lineEdit.setEnabled(False)
        self.ID_lineEdit.setGeometry(QRect(70, 20, 411, 22))
        self.ID_lineEdit.setReadOnly(True)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QRect(10, 20, 51, 22))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.comboBox_5 = QComboBox(self.tab_2)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setEnabled(False)
        self.comboBox_5.setGeometry(QRect(10, 20, 151, 22))
        self.comboBox_6 = QComboBox(self.tab_2)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setGeometry(QRect(175, 20, 151, 22))
        self.comboBox_7 = QComboBox(self.tab_2)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setEnabled(False)
        self.comboBox_7.setGeometry(QRect(340, 20, 151, 22))
        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 60, 481, 461))
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(750, 410, 431, 151))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.showButton = QPushButton(self.centralwidget)
        self.showButton.setObjectName(u"showButton")
        self.showButton.setGeometry(QRect(150, 540, 61, 24))
        self.hideUnimportantCheck = QCheckBox(self.centralwidget)
        self.hideUnimportantCheck.setObjectName(u"hideUnimportantCheck")
        self.hideUnimportantCheck.setGeometry(QRect(750, 10, 181, 21))
        self.gridCheck = QCheckBox(self.centralwidget)
        self.gridCheck.setObjectName(u"gridCheck")
        self.gridCheck.setGeometry(QRect(1100, 10, 81, 21))
        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setEnabled(True)
        self.gridWidget.setGeometry(QRect(740, 40, 450, 360))
        self.line = QFrame(self.gridWidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(1, 45, 449, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.gridWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1, 90, 449, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.gridWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1, 135, 449, 3))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.gridWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(1, 180, 449, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.gridWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(1, 225, 449, 3))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.gridWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(1, 270, 449, 3))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.gridWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(1, 315, 449, 3))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.gridWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(45, 1, 3, 359))
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_9 = QFrame(self.gridWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(90, 1, 3, 359))
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_10 = QFrame(self.gridWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(135, 1, 3, 359))
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_11 = QFrame(self.gridWidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(180, 1, 3, 359))
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_12 = QFrame(self.gridWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(225, 1, 3, 359))
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.line_13 = QFrame(self.gridWidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(270, 1, 3, 359))
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.line_14 = QFrame(self.gridWidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(315, 1, 3, 359))
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.line_15 = QFrame(self.gridWidget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(360, 1, 3, 359))
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.line_16 = QFrame(self.gridWidget)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(405, 1, 3, 359))
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.roomFrame = QFrame(self.centralwidget)
        self.roomFrame.setObjectName(u"roomFrame")
        self.roomFrame.setGeometry(QRect(740, 40, 450, 360))
        self.roomFrame.setFrameShape(QFrame.Box)
        self.roomFrame.setFrameShadow(QFrame.Plain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.label_2.raise_()
        self.listWidget.raise_()
        self.addButton.raise_()
        self.delButton.raise_()
        self.label.raise_()
        self.showButton.raise_()
        self.hideUnimportantCheck.raise_()
        self.gridCheck.raise_()
        self.gridWidget.raise_()
        self.roomFrame.raise_()
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1200, 22))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(4)
        self.comboBox_2.setCurrentIndex(4)
        self.comboBox_4.setCurrentIndex(4)
        self.comboBox_3.setCurrentIndex(4)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"&Save As", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"&Close", None))
        self.actionActors.setText(QCoreApplication.translate("MainWindow", u"&Actors", None))
        self.actionPoints.setText(QCoreApplication.translate("MainWindow", u"&Points", None))
        self.actionRails.setText(QCoreApplication.translate("MainWindow", u"Rails", None))
        self.actionGrid.setText(QCoreApplication.translate("MainWindow", u"&Grid", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Actors", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.delButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Switches", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Flag", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Global Flag", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Hardcoded Value", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Panel Flag", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Unused", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Flag", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Global Flag", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Hardcoded Value", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Panel Flag", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Unused", None))

        self.label_27.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Flag", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Global Flag", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Hardcoded Value", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Panel Flag", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Unused", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Flag", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Global Flag", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Hardcoded Value", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Panel Flag", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Unused", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main Data", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Is Enemy Actor:  False", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Is Enemy Actor:  True", None))

        self.comboBox_5.setCurrentText(QCoreApplication.translate("MainWindow", u"Is Enemy Actor:  False", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Checks For Kills:  False", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Checks For Kills:  True", None))

        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"+Enemies Tile:  False", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"+Enemies Tile:  True", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Link Data (Saving not supported)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Positions:\n"
"    X = left -> right \n"
"    Y = down -> up (gravity)\n"
"    Z = forward -> backwards\n"
"\n"
" When focused on a position, arrow keys will move it by 1 tile (a change of 1.5)\n"
"\n"
" When focused on a rotation, the Y rotation is what you will usually want to edit\n"
" It will make it face in the direction of the arrow key", None))
        self.showButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.hideUnimportantCheck.setText(QCoreApplication.translate("MainWindow", u"Hide Objects Without Sprites", None))
        self.gridCheck.setText(QCoreApplication.translate("MainWindow", u"Show Grid", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

