import unreal
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QComboBox, QPushButton, QWidget, QSlider, QMessageBox, QVBoxLayout
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from image_try import ImageViewer
import icon_rc
import random


loader = QUiLoader()

@unreal.uclass()
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.load_ui()
        self.widget.setParent(self)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout) 
        
        self.btn_place = self.widget.findChild(QPushButton, 'btn_place')
        self.btn_place.clicked.connect(self.click_button)
        self.btn_move = self.widget.findChild(QPushButton, 'btn_move')
        self.btn_move.clicked.connect(self.move_button)
        self.image_viewer = ImageViewer()

        charno = self.widget.findChild(QComboBox, 'charno')
        charno.addItems(["1", "2", "3","4","5","6"])
        charno.currentIndexChanged.connect(self.update_char_number)
        self.current_char_number = 1  # Default to 1 character

        self.points_drawn = 0

        encno = self.widget.findChild(QComboBox, 'encno')
        encno.addItems(["1", "2", "3","4","5","6"])
        encno.currentIndexChanged.connect(self.check_encounter_charNo)

        gen_box = self.widget.findChild(QtWidgets.QGroupBox, 'genBox')
        self.gen_layout = gen_box.layout()   

        ethn_box = self.widget.findChild(QtWidgets.QGroupBox, 'ethnBox')
        self.ethn_layout = ethn_box.layout()   

        role_box = self.widget.findChild(QtWidgets.QGroupBox, 'roleBox')
        self.role_layout = role_box.layout()   

        temp_box = self.widget.findChild(QtWidgets.QGroupBox, 'tempBox')
        self.temp_layout = temp_box.layout()   

        #initial_char_number = int(charno.currentText())
        self.create_character_widgets(self.current_char_number)


        
    def update_char_number(self, index):
        charno = self.widget.findChild(QComboBox, 'charno')  # Fix attribute name here
        current_char_number = int(charno.itemText(index))
        self.create_character_widgets(current_char_number)
        self.points_drawn = 0
                
    def create_character_widgets(self, num_characters):

        for layout in [self.gen_layout, self.ethn_layout, self.role_layout, self.temp_layout]:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().setParent(None)

        self.gen_combos = []
        self.ethn_combos = []
        self.role_combos = []
        self.temp_sliders = []
 

        for i in range(len(self.gen_combos), num_characters):
            gen_combo = QComboBox(self)
            gen_combo.addItems(["Female", "Male"])
            gen_combo.setObjectName(f'gen{i+1}')
            self.gen_layout.addWidget(gen_combo)
            self.gen_combos.append(gen_combo)


        for i in range(len(self.ethn_combos), num_characters):
            ethn_combo = QComboBox(self)
            ethn_combo.addItems(["Light", "Dark"])
            ethn_combo.setObjectName(f'ethn{i+1}')
            self.ethn_layout.addWidget(ethn_combo)
            self.ethn_combos.append(ethn_combo)


        # Create and add role combo boxes
        for i in range(len(self.role_combos), num_characters):
            role_combo = QComboBox(self)
            role_combo.addItems(["Salesman", "Clerk", "Bystander"])
            role_combo.setObjectName(f'role{i+1}')
            self.role_layout.addWidget(role_combo)
            self.role_combos.append(role_combo)


        # Create and add temp sliders
        for i in range(len(self.temp_sliders), num_characters):
            temp_slider = QSlider(Qt.Horizontal, self)
            temp_slider.setObjectName(f'temp{i+1}')
            temp_slider.setMinimum(0)
            temp_slider.setMaximum(2)  # Adjust maximum size as needed
            temp_slider.setTickPosition(QSlider.TicksBelow)  # Hide ticks
            self.temp_layout.addWidget(temp_slider)
            self.temp_sliders.append(temp_slider)
            

    def check_encounter_charNo(self):
        encno = self.widget.findChild(QComboBox, 'encno')
        charNo = self.widget.findChild(QComboBox, 'charno')

        enc_points = int(encno.currentText())
        char_points = int(charNo.currentText())

        if enc_points > char_points:
            # If encounter points exceed navigation points, show a message box
            QMessageBox.warning(self.widget, "Warning", "Number of Encounter points cannot be more than the Number of Characters.")
            # You can also reset the selection to the maximum possible value
            encno.setCurrentIndex(charNo.currentIndex())
            unreal.log(charNo.currentIndex())



    def move_button(self):
        print("Button Clicked")
        self.image_viewer.show()
        self.image_viewer.add_point_button.show()
        self.image_viewer.add_point_button.move(220, 60)
        unreal.EditorLevelLibrary.load_level("Game/levels/LowEndClothesStore")
        

    def load_ui(self):
        path = 'D:\\UE\\pyqt\\MainW.ui'
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.widget = loader.load(file)
        file.close()



# Call this function with the relevant data to send to Unreal Engine

    def click_button(self):
        charno = self.widget.findChild(QComboBox, 'charno')
        encno = self.widget.findChild(QComboBox, 'encno')

        char_points = int(charno.currentText())
        enc_points = int(encno.currentText())

        gen_combos = [self.widget.findChild(QComboBox, f'gen{i+1}') for i in range(int(charno.currentText()))]

        points = self.image_viewer.get_points()
        unreal.log("Character Points: {}".format(char_points))
        unreal.log("Encounter Points: {}".format(enc_points))
        unreal.log("Gen Combos: {}".format([combo.currentText() for combo in gen_combos]))
        unreal.log("Points: {}".format(points))
        send_data_to_unreal('Female')

@unreal.ufunction(staticmethod, meta=dict(CallableWithoutWorldContext="true"))
def send_data_to_unreal(gender):
    # Call the exposed function in your Unreal Engine Python plugin
    unreal.MyPlugin.spawn_actor_with_properties(gender)
       

def openWindow():
    """
    Create tool window.
    """
    if QtWidgets.QApplication.instance():
        # Find and close any existing instances of the tool window
        for win in QtWidgets.QApplication.topLevelWidgets():
            if isinstance(win, MainWindow):  # Check if the widget is an instance of MainWindow
                win.close()

    else:
        QtWidgets.QApplication(sys.argv)

    # load UI into QApp instance
    MainWindow.window = MainWindow()
    MainWindow.window.setWindowTitle('Sample Tool')
    MainWindow.window.setFixedSize(660, 750)
    unreal.parent_external_window_to_slate(MainWindow.window.winId(), unreal.SlateParentWindowSearchMethod.ACTIVE_WINDOW)
    MainWindow.window.show()

    encno = MainWindow.window.widget.findChild(QComboBox, 'encno')
    MainWindow.window.image_viewer.set_encno_combobox(encno)


openWindow()
unreal.log("Pls")