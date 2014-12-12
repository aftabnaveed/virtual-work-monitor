#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
#from SaveScreenshotThread import SaveScreenshotThread


class Deewa(QtGui.QWidget):
    def __init__(self):
        super(Deewa, self).__init__()
        self.deewaLabel = QtGui.QLabel()
        self.deewaLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.deewaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deewaLabel.setMinimumSize(240, 160)

        #self.createOptionsGroupBox()
        #self.createButtonsLayout()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.deewaLabel)
        #mainLayout.addWidget(self.optionsGroupBox)
        #mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Screenshot")
        self.resize(300, 200)




if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    screenshot = Deewa()
    screenshot.show()                    
    sys.exit(app.exec_())
