
from PySide6.QtWidgets import QWidget, QComboBox, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
#from pyqttry import MainWindow

loader = QUiLoader()

class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setWindowTitle("Player Characteristics")
        self.load_ui()
        self.widget.setParent(self)
        #self.getIndex = MainWindow()

        gen1 = self.widget.findChild(QComboBox, 'gen1')
        gen1.addItems(["Female", "Male"])


        gen2 = self.widget.findChild(QComboBox, 'gen2')
        gen2.addItems(["Female", "Male"])


        gen3 = self.widget.findChild(QComboBox, 'gen3')
        gen3.addItems(["Female", "Male"])


      #  if self.getIndex.activated(index=1):
       #     gen3 = self.widget.setEnabled(False)
        #else: gen3 = self.widget.setEnabled(True)


    def load_ui(self):
        path = 'D:\\UE\\pyqt\\Win2.ui'
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.widget = loader.load(file)
        file.close()

