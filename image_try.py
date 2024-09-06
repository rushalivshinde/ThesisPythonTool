
import cv2
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QMessageBox
from PySide6.QtGui import QImage, QPixmap, QColor, QPen
from PySide6.QtCore import Qt, QPoint

def screen_to_unreal_world_3d(screen_point, viewer):
  # Define screen resolution and scaling factor
  screen_width = viewer.image_width
  screen_height = viewer.image_height

  # Convert screen coordinates to NDC (-1 to 1) for X, Y, and Z dimensions
  ndc_x = 2 * screen_point.x() / screen_width 
  ndc_y = 2 * screen_point.y() / screen_height 

  # Assuming Z coordinate is 0 in the screen-space (e.g., a top-down view)
  ndc_z = 0.0

  # Define Unreal Engine world scale based on desired units
  unreal_world_scale_x = screen_width * 1.4
  unreal_world_scale_y = screen_height * 1.4 # Or screen_height / 2 depending on your preference

  # Convert NDC to world coordinates in Unreal Engine for X, Y, and Z dimensions
  unreal_x = ndc_x * unreal_world_scale_x
  unreal_y = ndc_y * unreal_world_scale_y
  unreal_z = ndc_z

  return unreal_x, unreal_y, unreal_z


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.image_path = "D:\\UE\\pyqt\\QT\\store.png"  # Path to your image
        self.cv_image = cv2.imread(self.image_path)
        self.image_height, self.image_width, _ = self.cv_image.shape
        self.encno_combobox = None

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setSceneRect(0, 0, self.image_width, self.image_height)
        self.setCentralWidget(self.view)

        self.load_image()
        self.add_point_button = QPushButton("Add Point")
        self.add_point_button.clicked.connect(self.add_point)
        self.add_point_button.setCheckable(True)
        self.add_point_mode = False
        self.points = []


        self.scene.mousePressEvent = self.mousePressEvent

    def set_encno_combobox(self, encno_combobox):
        self.encno_combobox = encno_combobox

    def load_image(self):
        qimage = QImage(self.cv_image.data, self.image_width, self.image_height,
                        self.cv_image.strides[0], QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qimage)
        self.scene.addPixmap(pixmap)

    def mousePressEvent(self, event):
        if self.add_point_mode and self.encno_combobox:
        # Convert the event's position to a QPoint and then map it to scene coordinates
            pos_point = event.position().toPoint()  # This converts the position to QPoint
            pos_scene = self.view.mapToScene(pos_point)
            encno_value = int(self.encno_combobox.currentText())
            if len(self.points) >= encno_value:
                QMessageBox.warning(self, "Warning", "The maximum number of points for this encounter has been reached.")
                return
            self.draw_point(pos_scene)
            winpt = (QPoint(int(pos_scene.x()), int(pos_scene.y())))
            print("Window points: ", winpt)
            scrpt = screen_to_unreal_world_3d(QPoint(int(pos_scene.x()), int(pos_scene.y())),self)
            print("Screen to Unreal: ", scrpt)
            if scrpt not in self.points:  # Ensure uniqueness before adding
                self.points.append(scrpt)

    def add_point(self):
        print("add pt")
        self.add_point_mode = not self.add_point_mode
        self.add_point_button.setChecked(self.add_point_mode)
            
    def draw_point(self, pos):
        radius = 3
        pen = QPen(QColor(Qt.white))
        brush = QColor(Qt.white)
        self.scene.addEllipse(pos.x() - radius, pos.y() - radius, radius * 2, radius * 2, pen, brush)
    
    def get_points(self):
        print("Getting points...")
        return self.points




