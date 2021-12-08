# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filesMAR_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(561, 352)
        self.btn_start_manage = QPushButton(Form)
        self.btn_start_manage.setObjectName(u"btn_start_manage")
        self.btn_start_manage.setGeometry(QRect(20, 290, 131, 41))
        font = QFont()
        font.setFamily(u"Verdana")
        self.btn_start_manage.setFont(font)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 250, 521, 23))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(17, 210, 531, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.le_show_dir_path = QLineEdit(Form)
        self.le_show_dir_path.setObjectName(u"le_show_dir_path")
        self.le_show_dir_path.setGeometry(QRect(220, 160, 321, 20))
        self.le_show_dir_path.setFrame(False)
        self.btn_choose_dir_path = QToolButton(Form)
        self.btn_choose_dir_path.setObjectName(u"btn_choose_dir_path")
        self.btn_choose_dir_path.setGeometry(QRect(190, 160, 25, 19))
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(170, 120, 20, 81))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.btn_manage_suffixes = QPushButton(Form)
        self.btn_manage_suffixes.setObjectName(u"btn_manage_suffixes")
        self.btn_manage_suffixes.setGeometry(QRect(20, 150, 131, 41))
        self.btn_manage_suffixes.setFont(font)
        self.btn_manage_suffixes.setFlat(False)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 90, 531, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 110, 231, 31))
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 211, 31))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 30, 171, 31))
        font2 = QFont()
        font2.setFamily(u"Verdana")
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.btn_request = QPushButton(Form)
        self.btn_request.setObjectName(u"btn_request")
        self.btn_request.setGeometry(QRect(20, 10, 61, 23))
        self.btn_request.setFont(font)
        self.btn_request.setFlat(False)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 60, 51, 20))
        font3 = QFont()
        font3.setFamily(u"Verdana")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)

        self.retranslateUi(Form)

        self.btn_request.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_start_manage.setText(QCoreApplication.translate("Form", u"D\u00e9marrer le tri", None))
        self.btn_choose_dir_path.setText(QCoreApplication.translate("Form", u"...", None))
        self.btn_manage_suffixes.setText(QCoreApplication.translate("Form", u"G\u00e9rer les fichiers", None))
        self.label.setText(QCoreApplication.translate("Form", u"Chemin vers le dossier \u00e0 trier :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Gestion des fichiers :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"FilesMAR", None))
        self.btn_request.setText(QCoreApplication.translate("Form", u"Requ\u00eate", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"By AR", None))
    # retranslateUi

