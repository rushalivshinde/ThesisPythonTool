# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainW.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import test_rc
import icon_rc

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        if not SecondWindow.objectName():
            SecondWindow.setObjectName(u"SecondWindow")
        SecondWindow.resize(675, 767)
        self.btn_place = QPushButton(SecondWindow)
        self.btn_place.setObjectName(u"btn_place")
        self.btn_place.setGeometry(QRect(270, 690, 131, 51))
        self.btn_move = QPushButton(SecondWindow)
        self.btn_move.setObjectName(u"btn_move")
        self.btn_move.setGeometry(QRect(190, 190, 251, 171))
        self.btn_move.setStyleSheet(u"#btn_move {\n"
"background-color: transparent;\n"
"border-image: url(:/addIcons/store.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.charno = QComboBox(SecondWindow)
        self.charno.setObjectName(u"charno")
        self.charno.setGeometry(QRect(20, 140, 121, 21))
        self.charno.setEditable(False)
        self.label = QLabel(SecondWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 121, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label_2 = QLabel(SecondWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 120, 121, 21))
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.encno = QComboBox(SecondWindow)
        self.encno.setObjectName(u"encno")
        self.encno.setGeometry(QRect(370, 140, 121, 21))
        self.encno.setEditable(False)
        self.label_4 = QLabel(SecondWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 141, 21))
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(SecondWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 30, 221, 21))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(SecondWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 70, 521, 31))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setWordWrap(True)
        self.label_8 = QLabel(SecondWindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 90, 581, 31))
        self.label_8.setFont(font2)
        self.label_8.setWordWrap(True)
        self.label_10 = QLabel(SecondWindow)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 660, 381, 31))
        self.label_10.setFont(font2)
        self.label_10.setWordWrap(True)
        self.genBox = QGroupBox(SecondWindow)
        self.genBox.setObjectName(u"genBox")
        self.genBox.setGeometry(QRect(10, 370, 151, 271))
        self.verticalLayout = QVBoxLayout(self.genBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ethnBox = QGroupBox(SecondWindow)
        self.ethnBox.setObjectName(u"ethnBox")
        self.ethnBox.setGeometry(QRect(170, 370, 151, 271))
        self.verticalLayout_2 = QVBoxLayout(self.ethnBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.roleBox = QGroupBox(SecondWindow)
        self.roleBox.setObjectName(u"roleBox")
        self.roleBox.setGeometry(QRect(330, 370, 151, 271))
        self.verticalLayout_3 = QVBoxLayout(self.roleBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tempBox = QGroupBox(SecondWindow)
        self.tempBox.setObjectName(u"tempBox")
        self.tempBox.setGeometry(QRect(490, 370, 161, 271))
        self.verticalLayout_4 = QVBoxLayout(self.tempBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.retranslateUi(SecondWindow)
        self.charno.currentIndexChanged.connect(SecondWindow.update_char_number)

        QMetaObject.connectSlotsByName(SecondWindow)
    # setupUi

    def retranslateUi(self, SecondWindow):
        SecondWindow.setWindowTitle(QCoreApplication.translate("SecondWindow", u"Character Importer", None))
        self.btn_place.setText(QCoreApplication.translate("SecondWindow", u"Place Actors", None))
        self.btn_move.setText("")
        self.charno.setCurrentText("")
        self.label.setText(QCoreApplication.translate("SecondWindow", u"No. of Characters:", None))
        self.label_2.setText(QCoreApplication.translate("SecondWindow", u"No. of Encounters:", None))
        self.encno.setCurrentText("")
        self.label_4.setText(QCoreApplication.translate("SecondWindow", u"Select Environment:", None))
        self.label_5.setText(QCoreApplication.translate("SecondWindow", u"Character Importer:", None))
        self.label_6.setText(QCoreApplication.translate("SecondWindow", u"* Number of Encounters states how many Characters you want the player the interact with.", None))
        self.label_8.setText(QCoreApplication.translate("SecondWindow", u"* Please note: Number of Encounter points cannot be more than the Number of Characters.", None))
        self.label_10.setText(QCoreApplication.translate("SecondWindow", u"*Temperment Scale: Left - Happy, Middle - neutral, Right - Angry", None))
        self.genBox.setTitle(QCoreApplication.translate("SecondWindow", u"genBox", None))
        self.ethnBox.setTitle(QCoreApplication.translate("SecondWindow", u"ethnBox", None))
        self.roleBox.setTitle(QCoreApplication.translate("SecondWindow", u"roleBox", None))
        self.tempBox.setTitle(QCoreApplication.translate("SecondWindow", u"tempBox", None))
    # retranslateUi

