from PyQt5.QtCore import QObject, pyqtSlot
from utils.write_log import writeExceptionToFile

class PickUpKeyController(QObject):
    def __init__(self, user):
        super().__init__()
        pass