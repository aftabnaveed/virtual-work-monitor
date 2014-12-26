

from PyQt4 import QtCore, QtGui
import time

class SaveScreenshotThread(QtCore.QThread):    
    capture = QtCore.pyqtSignal(object)
    gui = None

    def __init__(self, gui):
        QtCore.QThread.__init__(self)
        self.gui = gui

    def run(self):
        print "Saving " + self.gui.fileName
        self.gui.saveScreenshotButton.setDisabled(True)
        self.capture.emit(self.gui)
        #self.gui.show()



class MainGui(QtGui.QWidget):
  
    fileName = 'screenshot' 

    def __init__(self):
       super(MainGui, self).__init__() 
       self.screenshotLabel = QtGui.QLabel()
       self.screenshotLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
       self.screenshotLabel.setAlignment(QtCore.Qt.AlignCenter)
       self.screenshotLabel.setMinimumSize(240, 160)

       self.timer = QtCore.QTimer()
       self.timer.timeout.connect(self.captureAndSaveScreen)

       #enabling below would execute the time only once,  
       #self.timer.setSingleShot(True)
       self.timer.start(5000)

    def createOptionsGroupBox(self):
        optionsGroupBox = QtGui.QGroupBox("Options")
        
        self.delaySpinBox = QtGui.QSpinBox()
        self.delaySpinBox.setSuffix(" s")
        self.delaySpinBox.setMaximum(60)

        self.delayBoxLabel = QtGui.QLabel("Screenshot Delay")

        self.hideThisWindowCheckBox = QtGui.QCheckBox("Hide This Window")



        optionsGroupBoxLayout = QtGui.QGridLayout()
        optionsGroupBoxLayout.addWidget(self.delayBoxLabel, 0, 0)
        optionsGroupBoxLayout.addWidget(self.delaySpinBox, 0, 1)
        optionsGroupBoxLayout.addWidget(self.hideThisWindowCheckBox, 1, 0, 1, 2)

        optionsGroupBox.setLayout(optionsGroupBoxLayout)

        return optionsGroupBox


    def createButtonsLayout(self):
        self.newScreenshotButton = self.createButton("New Screenshot", self.newScreenshot)
        self.saveScreenshotButton = self.createButton("Save Screenshot", self.saveScreenshot)
        self.quitScreenshotButton = self.createButton("Quit", self.close)
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.newScreenshotButton)
        self.buttonsLayout.addWidget(self.saveScreenshotButton)
        self.buttonsLayout.addWidget(self.quitScreenshotButton)
        return self.buttonsLayout


    def shootScreen(self):
        #if self.delaySpinBox.value() != 0:
        QtGui.qApp.beep()

        self.originalPixmap = None
        self.originalPixmap = QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())
        return self.updateScreenshotLabel()

    def updateScreenshotLabel(self):
        self.screenshotLabel.setPixmap(self.originalPixmap.scaled(self.screenshotLabel.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        return self.screenshotLabel


    

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

    
    def newScreenshot(self):
        pass
        
    def saveScreenshot(self):
        format = 'png'
        initialPath = QtCore.QDir.currentPath() + "untitled." + format

        #fileName = QtGui.QFileDialog.getSaveFileName(self, "Save As", initialPath, "%s Files(*.%s);;All Files(*)" % (format.upper(), format))
        self.saveThread = SaveScreenshotThread(self)
        self.saveThread.capture.connect(self.captureAndSaveScreen)
        self.saveThread.start()


    def captureAndSaveScreen(self):
        
        self.fileName =  "screenshot_" + str(time.time()) + ".png"
        self.originalPixmap = None
        self.originalPixmap = QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())
        self.originalPixmap.save(self.fileName, 'png')
        self.saveScreenshotButton.setDisabled(False)
        
    def quitScreenshotButton(self):
        pass    
