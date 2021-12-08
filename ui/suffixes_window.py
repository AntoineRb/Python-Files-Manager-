# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_suffixes.ui'
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
        Form.resize(371, 630)
        self.le_suffix = QLineEdit(Form)
        self.le_suffix.setObjectName(u"le_suffix")
        self.le_suffix.setGeometry(QRect(120, 120, 231, 20))
        self.le_dir = QLineEdit(Form)
        self.le_dir.setObjectName(u"le_dir")
        self.le_dir.setGeometry(QRect(120, 150, 231, 20))
        self.btn_add_values = QPushButton(Form)
        self.btn_add_values.setObjectName(u"btn_add_values")
        self.btn_add_values.setGeometry(QRect(10, 120, 91, 51))
        self.btn_delete = QPushButton(Form)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(110, 570, 141, 41))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_delete.setFont(font)
        self.lw_show_suffixes = QListWidget(Form)
        self.lw_show_suffixes.setObjectName(u"lw_show_suffixes")
        self.lw_show_suffixes.setGeometry(QRect(10, 260, 351, 291))
        self.lw_show_suffixes.setProperty("isWrapping", False)
        self.lw_show_suffixes.setUniformItemSizes(False)
        self.lw_show_suffixes.setSelectionRectVisible(False)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 180, 351, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_title = QLabel(Form)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 20, 331, 31))
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        self.label_title.setFont(font1)
        self.label_add_values = QLabel(Form)
        self.label_add_values.setObjectName(u"label_add_values")
        self.label_add_values.setGeometry(QRect(20, 80, 271, 31))
        font2 = QFont()
        font2.setFamily(u"Verdana")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setWeight(50)
        self.label_add_values.setFont(font2)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 60, 351, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_show_suffixes = QLabel(Form)
        self.label_show_suffixes.setObjectName(u"label_show_suffixes")
        self.label_show_suffixes.setGeometry(QRect(20, 200, 331, 31))
        self.label_show_suffixes.setFont(font2)
        self.label_show_suffixes_exemple = QLabel(Form)
        self.label_show_suffixes_exemple.setObjectName(u"label_show_suffixes_exemple")
        self.label_show_suffixes_exemple.setGeometry(QRect(120, 230, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Verdana")
        font3.setPointSize(10)
        font3.setItalic(True)
        self.label_show_suffixes_exemple.setFont(font3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.le_suffix.setPlaceholderText("")
        self.btn_add_values.setText(QCoreApplication.translate("Form", u"Ajouter \u00e0 la liste", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"Supprimer de la liste", None))
        self.label_title.setText(QCoreApplication.translate("Form", u"Liste des extensions de fichiers ", None))
        self.label_add_values.setText(QCoreApplication.translate("Form", u"Ajouter un type de fichier \u00e0 la liste :", None))
        self.label_show_suffixes.setText(QCoreApplication.translate("Form", u"Liste des fichiers et de leurs dossiers cibles :", None))
        self.label_show_suffixes_exemple.setText(QCoreApplication.translate("Form", u"Dossier \u2b05 Fichier", None))
    # retranslateUi

