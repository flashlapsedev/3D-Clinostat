import Settings
import Commands

#always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
 
# This is our window from QtCreator
import Clinostat_UI

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, Clinostat_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def frame_slider_select(self):
        #if(Settings.LINKED):
            #Commands.linked_change(self)
        #else:
        Commands.frame_slider_change(self)

    def frame_spin_select(self):
        Commands.frame_spin_select(self)

    def reverse_frame_select(self):

        if(Settings.frame_dir==0):
            self.frameReverse_pushButton.setIcon(Settings.reverse)
        else:
            self.frameReverse_pushButton.setIcon(Settings.forward)
        Commands.reverse_frame_select(self)
            
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        Settings.init()
        self.frameErgz_pushButton.clicked.connect(lambda: Commands.ergz_frame(self))

        self.frame_spinBox.valueChanged.connect(lambda: self.frame_spin_select())

        self.frame_verticalSlider.valueChanged.connect(lambda: self.frame_slider_select())

        self.frameReverse_pushButton.clicked.connect(lambda: self.reverse_frame_select())


# I feel better having one of these
def main():
 # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
 # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
