#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from Thread import SaveScreenshotThread
from MainGui import MainGui

class Deewa(QtGui.QWidget):
    def __init__(self):
        super(Deewa, self).__init__()

        self.gui = MainGui()
        self.screenshotLabel = self.gui.shootScreen()
        self.optionsGroupBox = self.gui.createOptionsGroupBox()
        self.buttonsLayout = self.gui.createButtonsLayout()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.screenshotLabel)
        mainLayout.addWidget(self.optionsGroupBox)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)


        self.setWindowTitle("Work Monitor")
        self.resize(300, 200)






if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    screenshot = Deewa()
    screenshot.show()                    
    sys.exit(app.exec_())
