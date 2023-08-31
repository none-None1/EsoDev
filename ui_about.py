# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutdqoZpk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import img_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, version):
        self.version = version
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("EsoDev.png"))
        MainWindow.resize(739, 544)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName("img")
        self.img.setGeometry(QRect(150, 30, 391, 301))
        self.img.setPixmap(QPixmap(":/img/EsoDev.png"))
        self.img.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(80, 390, 491, 31))
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.img.setText("")
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow", "EsoDev " + self.version + " Esoteric Language IDE", None
            )
        )

    # retranslateUi
