# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hamburgue.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import file_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QSize(500, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_sup = QFrame(self.centralwidget)
        self.frame_sup.setObjectName(u"frame_sup")
        self.frame_sup.setMaximumSize(QSize(16777215, 45))
        self.frame_sup.setStyleSheet(u"background-color: rgb(110, 110, 110);")
        self.frame_sup.setFrameShape(QFrame.NoFrame)
        self.frame_sup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_sup)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame_error = QFrame(self.frame_sup)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setMaximumSize(QSize(450, 16777215))
        self.frame_error.setStyleSheet(u"background-color: rgb(236, 85, 88);\n"
"border-radius: 5px;")
        self.frame_error.setFrameShape(QFrame.NoFrame)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.label_error = QLabel(self.frame_error)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setMinimumSize(QSize(450, 0))
        self.label_error.setMaximumSize(QSize(450, 16777215))
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.botao_sair = QPushButton(self.frame_error)
        self.botao_sair.setObjectName(u"botao_sair")
        self.botao_sair.setMaximumSize(QSize(25, 25))
        self.botao_sair.setStyleSheet(u"Qpushbutton{\n"
" border-radius: 5px;\n"
"}\n"
"Qpushbutton:hover{\n"
" 	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.botao_sair)


        self.horizontalLayout_2.addWidget(self.frame_error)


        self.verticalLayout.addWidget(self.frame_sup)

        self.frame_med = QFrame(self.centralwidget)
        self.frame_med.setObjectName(u"frame_med")
        self.frame_med.setStyleSheet(u"background-color: rgb(110, 110, 110);")
        self.frame_med.setFrameShape(QFrame.NoFrame)
        self.frame_med.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_med)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 2, 0, 0)
        self._interior = QFrame(self.frame_med)
        self._interior.setObjectName(u"_interior")
        self._interior.setMaximumSize(QSize(450, 550))
        font = QFont()
        font.setPointSize(14)
        self._interior.setFont(font)
        self._interior.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"border-radius: 10px;")
        self._interior.setFrameShape(QFrame.NoFrame)
        self._interior.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self._interior)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(160, 20, 120, 80))
        self.frame.setStyleSheet(u"image: url(:/logo/Dugui_1.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.campo_user = QLineEdit(self._interior)
        self.campo_user.setObjectName(u"campo_user")
        self.campo_user.setGeometry(QRect(30, 200, 390, 50))
        font1 = QFont()
        font1.setFamily(u"Trebuchet MS")
        font1.setPointSize(14)
        self.campo_user.setFont(font1)
        self.campo_user.setMouseTracking(False)
        self.campo_user.setLayoutDirection(Qt.LeftToRight)
        self.campo_user.setStyleSheet(u"QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.campo_user.setMaxLength(35)
        self.campo_user.setCursorPosition(0)
        self.campo_senha = QLineEdit(self._interior)
        self.campo_senha.setObjectName(u"campo_senha")
        self.campo_senha.setGeometry(QRect(30, 290, 390, 50))
        self.campo_senha.setFont(font1)
        self.campo_senha.setMouseTracking(False)
        self.campo_senha.setLayoutDirection(Qt.LeftToRight)
        self.campo_senha.setStyleSheet(u"QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.campo_senha.setMaxLength(18)
        self.campo_senha.setCursorPosition(0)
        self.campo_entrar = QLineEdit(self._interior)
        self.campo_entrar.setObjectName(u"campo_entrar")
        self.campo_entrar.setGeometry(QRect(30, 380, 180, 50))
        self.campo_entrar.setFont(font1)
        self.campo_entrar.setMouseTracking(False)
        self.campo_entrar.setLayoutDirection(Qt.LeftToRight)
        self.campo_entrar.setStyleSheet(u"QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(20, 255, 130);\n"
"}\n"
"")
        self.campo_entrar.setMaxLength(18)
        self.campo_entrar.setCursorPosition(6)
        self.campo_entrar.setAlignment(Qt.AlignCenter)
        self.campo_senha_3 = QLineEdit(self._interior)
        self.campo_senha_3.setObjectName(u"campo_senha_3")
        self.campo_senha_3.setGeometry(QRect(240, 380, 180, 50))
        self.campo_senha_3.setFont(font1)
        self.campo_senha_3.setMouseTracking(False)
        self.campo_senha_3.setLayoutDirection(Qt.LeftToRight)
        self.campo_senha_3.setStyleSheet(u"QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(20, 255, 130);\n"
"}\n"
"")
        self.campo_senha_3.setMaxLength(18)
        self.campo_senha_3.setCursorPosition(9)
        self.campo_senha_3.setAlignment(Qt.AlignCenter)
        self.label_login = QLabel(self._interior)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(140, 130, 171, 41))
        font2 = QFont()
        font2.setFamily(u"Trebuchet MS")
        font2.setPointSize(16)
        self.label_login.setFont(font2)
        self.label_login.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self._interior)


        self.verticalLayout.addWidget(self.frame_med)

        self.frame_inf = QFrame(self.centralwidget)
        self.frame_inf.setObjectName(u"frame_inf")
        self.frame_inf.setMaximumSize(QSize(16777215, 30))
        self.frame_inf.setStyleSheet(u"background-color: rgb(110, 110, 110);")
        self.frame_inf.setFrameShape(QFrame.NoFrame)
        self.frame_inf.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_inf)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 3, 161, 20))
        font3 = QFont()
        font3.setFamily(u"Trebuchet MS")
        font3.setPointSize(9)
        self.label.setFont(font3)

        self.verticalLayout.addWidget(self.frame_inf)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hamburgueria DuGui", None))
        self.label_error.setText(QCoreApplication.translate("MainWindow", u"Login ou senha errados", None))
        self.botao_sair.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.campo_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.campo_senha.setInputMask("")
        self.campo_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.campo_entrar.setInputMask("")
        self.campo_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.campo_entrar.setPlaceholderText("")
        self.campo_senha_3.setInputMask("")
        self.campo_senha_3.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.campo_senha_3.setPlaceholderText("")
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"Tela de Login", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Feynman Technology", None))
    # retranslateUi

