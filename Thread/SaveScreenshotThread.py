

from PyQt4 import QtCore

class SaveSchreenshotThread(QtCore.QThread):
    
    capture = QtCore.pyqtSignal(object)
    screenshot = None
    imageFormat = 'png'
    fileName = None
    pixelMap = None

    def __init__(self, screenshot, pixelMap, fileName, imageFormat='png'):
        QtCore.__init__(self)
        self.screenshot = screenshot
        self.imageFormat = imageFormat
        self.fileName = fileName
        self.pixelMap = pixelMap

    def run(self):
        self.capture.emit(self.screenshot, self.filenName, self.imageFormat)
