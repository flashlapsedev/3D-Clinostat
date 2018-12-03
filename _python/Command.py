import Settings
from time import sleep
from PyQt5.QtCore import QThread

def top_color_change(self):
    temp = self.topColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~0~8~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~0~8~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~0~8~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~0~8~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~0~8~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~"+str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~0~8~0~0~0~0", 'UTF-8'))

def left_color_change(self):
    temp = self.leftColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~8~15~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~8~15~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~8~15~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~8~15~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~8~15~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~8~15~0~0~0~0", 'UTF-8'))

def right_color_change(self):
    temp = self.rightColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~15~23~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~15~23~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~15~23~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~15~23~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~15~23~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~15~23~0~0~0~0", 'UTF-8'))

def bottom_color_change(self):
    temp = self.bottomColor_comboBox.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~23~30~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~23~30~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~23~30~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~23~30~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~23~30~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~23~30~0~0~0~0", 'UTF-8'))

def IR_trigger(self):

    if not Settings.IR_STAT:
        Settings.ASD.write(bytes('5', 'UTF-8'))
        Settings.IR_STAT=True
    
    else:
        Settings.ASD.write(bytes('6', 'UTF-8'))
        Settings.IR_STAT=False




