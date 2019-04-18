import Settings
import Commands

always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import Clinostat_UI

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, Clinostat_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def frame_spin_select(self):
        Settings.frame_RPM=self.frame_spinBox.value()
        temp = "2~"+str(int(round(60/(Settings.frame_RPM*0.351488))))
        print(temp)
        Settings.sendCMD(address,temp)
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        Settings.init()
        self.frameErgz_pushButton.clicked.connect(lambda: Commands.ergz_frame(self))
        self.frame_spinBox.valueChanged.connect(lambda: self.frame_spin_select())
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
