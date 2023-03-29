# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceIZuoiV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icones_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(722, 412)
        MainWindow.setMinimumSize(QSize(722, 412))
        MainWindow.setMaximumSize(QSize(722, 412))
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 681, 50))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #d9d9d9;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cb_detectar = QComboBox(self.widget)
        self.cb_detectar.addItem("")
        self.cb_detectar.addItem("")
        self.cb_detectar.addItem("")
        self.cb_detectar.setObjectName(u"cb_detectar")
        self.cb_detectar.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_detectar.setStyleSheet(u"            QComboBox {\n"
"                background-color: white;\n"
"				font: 8pt \"Roboto\";\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                min-width: 6em;\n"
"            }\n"
"\n"
"            QComboBox::drop-down {\n"
"                subcontrol-origin: padding;\n"
"                subcontrol-position: top right;\n"
"                width: 15px;\n"
"\n"
"                border-left-width: 1px;\n"
"                border-left-color: gray;\n"
"                \n"
"            }\n"
"\n"
"            QComboBox::down-arrow {\n"
"				\n"
"				image: url(:/icones/setinha.png);\n"
"                width: 16px;\n"
"                height: 16px;\n"
"            }\n"
"\n"
"            QComboBox QAbstractItemView {\n"
"                border: 1px solid gray;\n"
"                selection-background-color: black;\n"
"                background-color: white;\n"
"            }")

        self.horizontalLayout_2.addWidget(self.cb_detectar, 0, Qt.AlignLeft)

        self.btn_trocar_lang = QPushButton(self.widget)
        self.btn_trocar_lang.setObjectName(u"btn_trocar_lang")
        self.btn_trocar_lang.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trocar_lang.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"outline: 0;\n"
"color: #e3e3e3;\n"
"}\n"
"\n"
"QPushButton#btn_trocar_lang:pressed {\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icones/trocar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_trocar_lang.setIcon(icon)
        self.btn_trocar_lang.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_trocar_lang, 0, Qt.AlignHCenter)

        self.cb_traduzido = QComboBox(self.widget)
        self.cb_traduzido.addItem("")
        self.cb_traduzido.addItem("")
        self.cb_traduzido.addItem("")
        self.cb_traduzido.setObjectName(u"cb_traduzido")
        self.cb_traduzido.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_traduzido.setStyleSheet(u"            QComboBox {\n"
"                background-color: white;\n"
"				font: 8pt \"Roboto\";\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                min-width: 6em;\n"
"            }\n"
"\n"
"            QComboBox::drop-down {\n"
"                subcontrol-origin: padding;\n"
"                subcontrol-position: top right;\n"
"                width: 15px;\n"
"\n"
"                border-left-width: 1px;\n"
"                border-left-color: gray;\n"
"                \n"
"            }\n"
"\n"
"            QComboBox::down-arrow {\n"
"				\n"
"				image: url(:/icones/setinha.png);\n"
"                width: 16px;\n"
"                height: 16px;\n"
"            }\n"
"\n"
"            QComboBox QAbstractItemView {\n"
"                border: 1px solid gray;\n"
"                selection-background-color: black;\n"
"                background-color: white;\n"
"            }")

        self.horizontalLayout_2.addWidget(self.cb_traduzido, 0, Qt.AlignRight)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 120, 681, 281))
        self.widget_2.setMinimumSize(QSize(681, 281))
        self.widget_2.setMaximumSize(QSize(681, 281))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(217, 217, 217);\n"
"border-left-color: rgb(217, 217, 217);\n"
"border-bottom-color: rgb(217, 217, 217);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pte_traduzir = QPlainTextEdit(self.widget_2)
        self.pte_traduzir.setObjectName(u"pte_traduzir")
        self.pte_traduzir.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #b9b9b9;")

        self.horizontalLayout.addWidget(self.pte_traduzir)

        self.btn_traduzir = QPushButton(self.widget_2)
        self.btn_traduzir.setObjectName(u"btn_traduzir")
        self.btn_traduzir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_traduzir.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Roboto\";\n"
"	color: #fff;\n"
"	outline: 0;\n"
"	border: 5px solid #343434;\n"
"	background-color: rgb(52, 52, 52);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #000000;\n"
"	border: 5px solid #8d8d8d;\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_traduzir:pressed {\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"	color: #000000;\n"
"	border: 5px solid #fff;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_traduzir)

        self.pte_traduzido = QPlainTextEdit(self.widget_2)
        self.pte_traduzido.setObjectName(u"pte_traduzido")
        self.pte_traduzido.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #b9b9b9;")
        self.pte_traduzido.setReadOnly(True)

        self.horizontalLayout.addWidget(self.pte_traduzido)

        self.lb_titulo = QLabel(self.centralwidget)
        self.lb_titulo.setObjectName(u"lb_titulo")
        self.lb_titulo.setGeometry(QRect(290, 20, 121, 31))
        self.lb_titulo.setStyleSheet(u"font: 25pt \"Roboto Thin\";")
        self.btn_copiar_traduzido = QPushButton(self.centralwidget)
        self.btn_copiar_traduzido.setObjectName(u"btn_copiar_traduzido")
        self.btn_copiar_traduzido.setGeometry(QRect(660, 360, 31, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_copiar_traduzido.sizePolicy().hasHeightForWidth())
        self.btn_copiar_traduzido.setSizePolicy(sizePolicy)
        self.btn_copiar_traduzido.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copiar_traduzido.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"outline: 0;\n"
"color: #e3e3e3;\n"
"}\n"
"\n"
"QPushButton#btn_copiar_traduzido:pressed {\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icones/copiar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copiar_traduzido.setIcon(icon1)
        self.btn_copiar_traduzido.setIconSize(QSize(25, 25))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cb_detectar.setItemText(0, QCoreApplication.translate("MainWindow", u"Portugu\u00eas", None))
        self.cb_detectar.setItemText(1, QCoreApplication.translate("MainWindow", u"Ingl\u00eas", None))
        self.cb_detectar.setItemText(2, QCoreApplication.translate("MainWindow", u"Espanhol", None))

        self.btn_trocar_lang.setText("")
        self.cb_traduzido.setItemText(0, QCoreApplication.translate("MainWindow", u"Ingl\u00eas", None))
        self.cb_traduzido.setItemText(1, QCoreApplication.translate("MainWindow", u"Portugu\u00eas", None))
        self.cb_traduzido.setItemText(2, QCoreApplication.translate("MainWindow", u"Espanhol", None))

        self.pte_traduzir.setPlainText("")
        self.pte_traduzir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escreva ou cole o texto", None))
        self.btn_traduzir.setText(QCoreApplication.translate("MainWindow", u"Traduzir", None))
        self.pte_traduzido.setPlainText("")
        self.lb_titulo.setText(QCoreApplication.translate("MainWindow", u"Tradutor", None))
        self.btn_copiar_traduzido.setText("")
    # retranslateUi

