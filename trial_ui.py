# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trial.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)
#import test_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(712, 508)
        self.btn_printActors = QPushButton(Dialog)
        self.btn_printActors.setObjectName(u"btn_printActors")
        self.btn_printActors.setGeometry(QRect(20, 10, 93, 28))
        self.btn_close = QPushButton(Dialog)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(210, 10, 93, 28))
        self.map_1 = QPushButton(Dialog)
        self.map_1.setObjectName(u"map_1")
        self.map_1.setGeometry(QRect(20, 280, 311, 201))
        self.map_1.setMouseTracking(True)
        self.map_1.setStyleSheet(u"#upLeft {\n"
"background-color: transparent;\n"
"border-image: url(:/newPrefix/image.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#upLeft:pressed\n"
"{\n"
"   border-image: url(:/newPrefix/image.png);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_printActors.setText(QCoreApplication.translate("Dialog", u"Print Actors", None))
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.map_1.setText("")
    # retranslateUi

