# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clinostat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 29, 310, 310))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../_image/Background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.Lighting_tab = QtWidgets.QWidget()
        self.Lighting_tab.setObjectName("Lighting_tab")
        self.BRT_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.BRT_spinBox.setGeometry(QtCore.QRect(30, 360, 61, 22))
        self.BRT_spinBox.setMinimum(1)
        self.BRT_spinBox.setMaximum(255)
        self.BRT_spinBox.setProperty("value", 50)
        self.BRT_spinBox.setObjectName("BRT_spinBox")
        self.BRT_lable = QtWidgets.QLabel(self.Lighting_tab)
        self.BRT_lable.setGeometry(QtCore.QRect(30, 330, 81, 31))
        self.BRT_lable.setObjectName("BRT_lable")
        self.frame = QtWidgets.QFrame(self.Lighting_tab)
        self.frame.setGeometry(QtCore.QRect(10, 10, 391, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.coreImage = QtWidgets.QLabel(self.frame)
        self.coreImage.setGeometry(QtCore.QRect(20, -40, 350, 350))
        self.coreImage.setText("")
        self.coreImage.setPixmap(QtGui.QPixmap("../_image/Core.png"))
        self.coreImage.setScaledContents(True)
        self.coreImage.setObjectName("coreImage")
        self.bottomColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.bottomColor_comboBox.setGeometry(QtCore.QRect(280, 30, 91, 21))
        self.bottomColor_comboBox.setObjectName("bottomColor_comboBox")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.bottomColor_comboBox.addItem("")
        self.IR_pushButton = QtWidgets.QPushButton(self.frame)
        self.IR_pushButton.setGeometry(QtCore.QRect(10, 260, 141, 31))
        self.IR_pushButton.setObjectName("IR_pushButton")
        self.rightColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.rightColor_comboBox.setGeometry(QtCore.QRect(280, 230, 91, 21))
        self.rightColor_comboBox.setObjectName("rightColor_comboBox")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.rightColor_comboBox.addItem("")
        self.leftColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.leftColor_comboBox.setGeometry(QtCore.QRect(10, 220, 91, 21))
        self.leftColor_comboBox.setObjectName("leftColor_comboBox")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.leftColor_comboBox.addItem("")
        self.topColor_comboBox = QtWidgets.QComboBox(self.frame)
        self.topColor_comboBox.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.topColor_comboBox.setObjectName("topColor_comboBox")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.topColor_comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(self.Lighting_tab)
        self.label_8.setGeometry(QtCore.QRect(200, 310, 141, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Lighting_tab)
        self.label_9.setGeometry(QtCore.QRect(270, 340, 21, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Lighting_tab)
        self.label_10.setGeometry(QtCore.QRect(170, 340, 21, 21))
        self.label_10.setObjectName("label_10")
        self.G_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.G_spinBox.setGeometry(QtCore.QRect(290, 340, 61, 22))
        self.G_spinBox.setMaximum(255)
        self.G_spinBox.setObjectName("G_spinBox")
        self.label_11 = QtWidgets.QLabel(self.Lighting_tab)
        self.label_11.setGeometry(QtCore.QRect(170, 370, 21, 21))
        self.label_11.setObjectName("label_11")
        self.B_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.B_spinBox.setGeometry(QtCore.QRect(190, 370, 61, 22))
        self.B_spinBox.setMaximum(255)
        self.B_spinBox.setObjectName("B_spinBox")
        self.R_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.R_spinBox.setGeometry(QtCore.QRect(190, 340, 61, 22))
        self.R_spinBox.setMaximum(255)
        self.R_spinBox.setObjectName("R_spinBox")
        self.label_12 = QtWidgets.QLabel(self.Lighting_tab)
        self.label_12.setGeometry(QtCore.QRect(270, 370, 21, 21))
        self.label_12.setObjectName("label_12")
        self.W_spinBox = QtWidgets.QSpinBox(self.Lighting_tab)
        self.W_spinBox.setGeometry(QtCore.QRect(290, 370, 61, 22))
        self.W_spinBox.setMaximum(255)
        self.W_spinBox.setObjectName("W_spinBox")
        self.tabWidget.addTab(self.Lighting_tab, "")
        self.Frame_tab = QtWidgets.QWidget()
        self.Frame_tab.setObjectName("Frame_tab")
        self.frame_verticalSlider = QtWidgets.QSlider(self.Frame_tab)
        self.frame_verticalSlider.setGeometry(QtCore.QRect(85, 20, 21, 311))
        self.frame_verticalSlider.setMinimum(3)
        self.frame_verticalSlider.setMaximum(15)
        self.frame_verticalSlider.setTracking(True)
        self.frame_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.frame_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_verticalSlider.setTickInterval(1)
        self.frame_verticalSlider.setObjectName("frame_verticalSlider")
        self.frame_spinBox = QtWidgets.QSpinBox(self.Frame_tab)
        self.frame_spinBox.setGeometry(QtCore.QRect(45, 350, 101, 31))
        self.frame_spinBox.setMinimum(3)
        self.frame_spinBox.setMaximum(15)
        self.frame_spinBox.setObjectName("frame_spinBox")
        self.frame_label = QtWidgets.QLabel(self.Frame_tab)
        self.frame_label.setGeometry(QtCore.QRect(45, 330, 101, 21))
        self.frame_label.setObjectName("frame_label")
        self.frame_2 = QtWidgets.QFrame(self.Frame_tab)
        self.frame_2.setGeometry(QtCore.QRect(200, 10, 201, 321))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frameCD_spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.frameCD_spinBox.setGeometry(QtCore.QRect(40, 50, 121, 22))
        self.frameCD_spinBox.setPrefix("")
        self.frameCD_spinBox.setMinimum(-200)
        self.frameCD_spinBox.setMaximum(200)
        self.frameCD_spinBox.setObjectName("frameCD_spinBox")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 121, 21))
        self.label_2.setObjectName("label_2")
        self.framePW_spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.framePW_spinBox.setGeometry(QtCore.QRect(40, 100, 121, 22))
        self.framePW_spinBox.setPrefix("")
        self.framePW_spinBox.setMinimum(1)
        self.framePW_spinBox.setMaximum(1000)
        self.framePW_spinBox.setProperty("value", 2)
        self.framePW_spinBox.setObjectName("framePW_spinBox")
        self.framePI_spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.framePI_spinBox.setGeometry(QtCore.QRect(40, 150, 121, 22))
        self.framePI_spinBox.setMinimum(1)
        self.framePI_spinBox.setMaximum(10000000)
        self.framePI_spinBox.setProperty("value", 380)
        self.framePI_spinBox.setObjectName("framePI_spinBox")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 121, 21))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 10, 121, 21))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(40, 180, 121, 21))
        self.label_13.setObjectName("label_13")
        self.frameApply_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.frameApply_pushButton.setGeometry(QtCore.QRect(30, 280, 141, 21))
        self.frameApply_pushButton.setObjectName("frameApply_pushButton")
        self.frameMS_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.frameMS_comboBox.setGeometry(QtCore.QRect(40, 200, 121, 22))
        self.frameMS_comboBox.setObjectName("frameMS_comboBox")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameMS_comboBox.addItem("")
        self.frameReset_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.frameReset_pushButton.setGeometry(QtCore.QRect(30, 250, 141, 21))
        self.frameReset_pushButton.setObjectName("frameReset_pushButton")
        self.frameErgz_pushButton = QtWidgets.QPushButton(self.Frame_tab)
        self.frameErgz_pushButton.setGeometry(QtCore.QRect(210, 350, 141, 41))
        self.frameErgz_pushButton.setObjectName("frameErgz_pushButton")
        self.frameReverse_pushButton = QtWidgets.QPushButton(self.Frame_tab)
        self.frameReverse_pushButton.setGeometry(QtCore.QRect(120, 290, 30, 30))
        self.frameReverse_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frameReverse_pushButton.setIcon(icon1)
        self.frameReverse_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.frameReverse_pushButton.setObjectName("frameReverse_pushButton")
        self.frameLink_pushButton = QtWidgets.QPushButton(self.Frame_tab)
        self.frameLink_pushButton.setGeometry(QtCore.QRect(360, 355, 30, 30))
        self.frameLink_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frameLink_pushButton.setIcon(icon2)
        self.frameLink_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.frameLink_pushButton.setObjectName("frameLink_pushButton")
        self.tabWidget.addTab(self.Frame_tab, "")
        self.Core_tab = QtWidgets.QWidget()
        self.Core_tab.setObjectName("Core_tab")
        self.core_verticalSlider = QtWidgets.QSlider(self.Core_tab)
        self.core_verticalSlider.setGeometry(QtCore.QRect(85, 20, 21, 311))
        self.core_verticalSlider.setMinimum(3)
        self.core_verticalSlider.setMaximum(15)
        self.core_verticalSlider.setTracking(True)
        self.core_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.core_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.core_verticalSlider.setTickInterval(1)
        self.core_verticalSlider.setObjectName("core_verticalSlider")
        self.coreReverse_pushButton = QtWidgets.QPushButton(self.Core_tab)
        self.coreReverse_pushButton.setGeometry(QtCore.QRect(120, 290, 30, 30))
        self.coreReverse_pushButton.setText("")
        self.coreReverse_pushButton.setIcon(icon1)
        self.coreReverse_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.coreReverse_pushButton.setObjectName("coreReverse_pushButton")
        self.frame_3 = QtWidgets.QFrame(self.Core_tab)
        self.frame_3.setGeometry(QtCore.QRect(200, 10, 201, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.coreCD_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.coreCD_spinBox.setGeometry(QtCore.QRect(40, 50, 121, 22))
        self.coreCD_spinBox.setPrefix("")
        self.coreCD_spinBox.setMinimum(-200)
        self.coreCD_spinBox.setMaximum(200)
        self.coreCD_spinBox.setObjectName("coreCD_spinBox")
        self.label_62 = QtWidgets.QLabel(self.frame_3)
        self.label_62.setGeometry(QtCore.QRect(40, 30, 121, 21))
        self.label_62.setObjectName("label_62")
        self.corePW_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.corePW_spinBox.setGeometry(QtCore.QRect(40, 100, 121, 22))
        self.corePW_spinBox.setPrefix("")
        self.corePW_spinBox.setMinimum(1)
        self.corePW_spinBox.setMaximum(1000)
        self.corePW_spinBox.setProperty("value", 2)
        self.corePW_spinBox.setObjectName("corePW_spinBox")
        self.corePI_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.corePI_spinBox.setGeometry(QtCore.QRect(40, 150, 121, 22))
        self.corePI_spinBox.setMinimum(1)
        self.corePI_spinBox.setMaximum(10000000)
        self.corePI_spinBox.setProperty("value", 380)
        self.corePI_spinBox.setObjectName("corePI_spinBox")
        self.label_63 = QtWidgets.QLabel(self.frame_3)
        self.label_63.setGeometry(QtCore.QRect(40, 80, 121, 21))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.frame_3)
        self.label_64.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.frame_3)
        self.label_65.setGeometry(QtCore.QRect(40, 10, 121, 21))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.frame_3)
        self.label_66.setGeometry(QtCore.QRect(40, 180, 121, 21))
        self.label_66.setObjectName("label_66")
        self.coreApply_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.coreApply_pushButton.setGeometry(QtCore.QRect(30, 280, 141, 21))
        self.coreApply_pushButton.setObjectName("coreApply_pushButton")
        self.coreMS_comboBox = QtWidgets.QComboBox(self.frame_3)
        self.coreMS_comboBox.setGeometry(QtCore.QRect(40, 200, 121, 22))
        self.coreMS_comboBox.setObjectName("coreMS_comboBox")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreMS_comboBox.addItem("")
        self.coreReset_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.coreReset_pushButton.setGeometry(QtCore.QRect(30, 250, 141, 21))
        self.coreReset_pushButton.setObjectName("coreReset_pushButton")
        self.label_68 = QtWidgets.QLabel(self.Core_tab)
        self.label_68.setGeometry(QtCore.QRect(45, 330, 101, 21))
        self.label_68.setObjectName("label_68")
        self.core_spinBox = QtWidgets.QSpinBox(self.Core_tab)
        self.core_spinBox.setGeometry(QtCore.QRect(45, 350, 101, 31))
        self.core_spinBox.setMinimum(3)
        self.core_spinBox.setMaximum(15)
        self.core_spinBox.setProperty("value", 3)
        self.core_spinBox.setObjectName("core_spinBox")
        self.coreErgz_pushButton = QtWidgets.QPushButton(self.Core_tab)
        self.coreErgz_pushButton.setGeometry(QtCore.QRect(210, 350, 141, 41))
        self.coreErgz_pushButton.setObjectName("coreErgz_pushButton")
        self.coreLink_pushButton = QtWidgets.QPushButton(self.Core_tab)
        self.coreLink_pushButton.setGeometry(QtCore.QRect(360, 355, 30, 30))
        self.coreLink_pushButton.setText("")
        self.coreLink_pushButton.setIcon(icon2)
        self.coreLink_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.coreLink_pushButton.setObjectName("coreLink_pushButton")
        self.tabWidget.addTab(self.Core_tab, "")
        self.IMAGING_tab = QtWidgets.QWidget()
        self.IMAGING_tab.setObjectName("IMAGING_tab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.IMAGING_tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 391, 331))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_Title = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Title.setObjectName("Image_Title")
        self.verticalLayout.addWidget(self.Image_Title)
        self.IST_Editor = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.IST_Editor.setEnabled(True)
        self.IST_Editor.setObjectName("IST_Editor")
        self.verticalLayout.addWidget(self.IST_Editor)
        self.Image_Interval = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Interval.setObjectName("Image_Interval")
        self.verticalLayout.addWidget(self.Image_Interval)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.ICI_spinBox.setEnabled(False)
        self.ICI_spinBox.setMaximum(9999999)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout.addWidget(self.ICI_spinBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_Duration = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Duration.setObjectName("Image_Duration")
        self.verticalLayout_2.addWidget(self.Image_Duration)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.ISD_spinBox.setEnabled(False)
        self.ISD_spinBox.setMaximum(9999999)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.layoutWidget = QtWidgets.QWidget(self.IMAGING_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 350, 411, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Progress_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Progress_Label.setObjectName("Progress_Label")
        self.verticalLayout_6.addWidget(self.Progress_Label)
        self.Progress_Bar = QtWidgets.QProgressBar(self.layoutWidget)
        self.Progress_Bar.setEnabled(False)
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setObjectName("Progress_Bar")
        self.verticalLayout_6.addWidget(self.Progress_Bar)
        self.tabWidget.addTab(self.IMAGING_tab, "")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 350, 81, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.JPG = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.JPG.setChecked(True)
        self.JPG.setObjectName("JPG")
        self.verticalLayout_12.addWidget(self.JPG)
        self.PNG = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.PNG.setObjectName("PNG")
        self.verticalLayout_12.addWidget(self.PNG)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(620, 350, 161, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Snapshot = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Snapshot.setEnabled(True)
        self.Snapshot.setObjectName("Snapshot")
        self.verticalLayout_13.addWidget(self.Snapshot)
        self.Cooling = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Cooling.setEnabled(True)
        self.Cooling.setObjectName("Cooling")
        self.verticalLayout_13.addWidget(self.Cooling)
        self.startImaging_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startImaging_pushButton.setEnabled(False)
        self.startImaging_pushButton.setGeometry(QtCore.QRect(609, 410, 171, 31))
        self.startImaging_pushButton.setObjectName("startImaging_pushButton")
        self.music_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.music_pushButton.setGeometry(QtCore.QRect(560, 350, 51, 51))
        self.music_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../_image/DS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_pushButton.setIcon(icon3)
        self.music_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.music_pushButton.setObjectName("music_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setEnabled(False)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate_Timelapse = QtWidgets.QAction(MainWindow)
        self.actionCreate_Timelapse.setObjectName("actionCreate_Timelapse")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.frameMS_comboBox.setCurrentIndex(7)
        self.coreMS_comboBox.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.BRT_lable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Brightness:</span></p></body></html>"))
        self.bottomColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.bottomColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.bottomColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.bottomColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.bottomColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.bottomColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.IR_pushButton.setText(_translate("MainWindow", "INFRARED:OFF"))
        self.rightColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.rightColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.rightColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.rightColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.rightColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.rightColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.leftColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.leftColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.leftColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.leftColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.leftColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.leftColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.topColor_comboBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.topColor_comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.topColor_comboBox.setItemText(2, _translate("MainWindow", "GREEN"))
        self.topColor_comboBox.setItemText(3, _translate("MainWindow", "BLUE"))
        self.topColor_comboBox.setItemText(4, _translate("MainWindow", "WHITE"))
        self.topColor_comboBox.setItemText(5, _translate("MainWindow", "CUSTOM"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Custom RGBW:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">G:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">B:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">W:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Lighting_tab), _translate("MainWindow", "LIGHTING"))
        self.frame_spinBox.setSuffix(_translate("MainWindow", " RPM"))
        self.frame_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">FRAME</span></p></body></html>"))
        self.frameCD_spinBox.setSuffix(_translate("MainWindow", " mA"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Current Offset:</p></body></html>"))
        self.framePW_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.framePI_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Width:</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Interval:</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Expert Controls</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Microstepping:</p></body></html>"))
        self.frameApply_pushButton.setText(_translate("MainWindow", "APPLY"))
        self.frameMS_comboBox.setCurrentText(_translate("MainWindow", "128"))
        self.frameMS_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.frameMS_comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.frameMS_comboBox.setItemText(2, _translate("MainWindow", "4"))
        self.frameMS_comboBox.setItemText(3, _translate("MainWindow", "8"))
        self.frameMS_comboBox.setItemText(4, _translate("MainWindow", "16"))
        self.frameMS_comboBox.setItemText(5, _translate("MainWindow", "32"))
        self.frameMS_comboBox.setItemText(6, _translate("MainWindow", "64"))
        self.frameMS_comboBox.setItemText(7, _translate("MainWindow", "128"))
        self.frameReset_pushButton.setText(_translate("MainWindow", "RESET"))
        self.frameErgz_pushButton.setText(_translate("MainWindow", "ENERGIZE COILS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Frame_tab), _translate("MainWindow", "FRAME"))
        self.coreCD_spinBox.setSuffix(_translate("MainWindow", " mA"))
        self.label_62.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Current Offset:</p></body></html>"))
        self.corePW_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.corePI_spinBox.setSuffix(_translate("MainWindow", " ms"))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Width:</p></body></html>"))
        self.label_64.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pulse Interval:</p></body></html>"))
        self.label_65.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Expert Controls</span></p></body></html>"))
        self.label_66.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Microstepping:</p></body></html>"))
        self.coreApply_pushButton.setText(_translate("MainWindow", "APPLY"))
        self.coreMS_comboBox.setCurrentText(_translate("MainWindow", "128"))
        self.coreMS_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.coreMS_comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.coreMS_comboBox.setItemText(2, _translate("MainWindow", "4"))
        self.coreMS_comboBox.setItemText(3, _translate("MainWindow", "8"))
        self.coreMS_comboBox.setItemText(4, _translate("MainWindow", "16"))
        self.coreMS_comboBox.setItemText(5, _translate("MainWindow", "32"))
        self.coreMS_comboBox.setItemText(6, _translate("MainWindow", "64"))
        self.coreMS_comboBox.setItemText(7, _translate("MainWindow", "128"))
        self.coreReset_pushButton.setText(_translate("MainWindow", "RESET"))
        self.label_68.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CORE</span></p></body></html>"))
        self.core_spinBox.setSuffix(_translate("MainWindow", " RPM"))
        self.coreErgz_pushButton.setText(_translate("MainWindow", "ENERGIZE COILS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Core_tab), _translate("MainWindow", "CORE"))
        self.Image_Title.setText(_translate("MainWindow", "Image Sequence Title"))
        self.Image_Interval.setText(_translate("MainWindow", "Image Capture Interval"))
        self.ICI_spinBox.setSuffix(_translate("MainWindow", " s"))
        self.Image_Duration.setText(_translate("MainWindow", "Image Sequence Duration"))
        self.ISD_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.Progress_Label.setText(_translate("MainWindow", "Progress:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IMAGING_tab), _translate("MainWindow", "IMAGING"))
        self.JPG.setText(_translate("MainWindow", "JPG"))
        self.PNG.setText(_translate("MainWindow", "PNG"))
        self.Snapshot.setText(_translate("MainWindow", "SNAPSHOT"))
        self.Cooling.setText(_translate("MainWindow", "COOLING:OFF"))
        self.startImaging_pushButton.setText(_translate("MainWindow", "START IMAGING"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))

