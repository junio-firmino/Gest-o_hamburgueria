# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqt Hamburgue.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_sup = QtWidgets.QFrame(self.centralwidget)
        self.frame_sup.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_sup.setStyleSheet("background-color: rgb(110, 110, 110);")
        self.frame_sup.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_sup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sup.setObjectName("frame_sup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_sup)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.frame_sup)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(236, 85, 88);\n"
"border-radius: 5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setMinimumSize(QtCore.QSize(450, 0))
        self.label_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.botao_sair = QtWidgets.QPushButton(self.frame_error)
        self.botao_sair.setMaximumSize(QtCore.QSize(25, 25))
        self.botao_sair.setStyleSheet("Qpushbutton{\n"
" border-radius: 5px;\n"
"}\n"
"Qpushbutton:hover{\n"
"     background-color: rgb(0, 0, 0);\n"
"}")
        self.botao_sair.setObjectName("botao_sair")
        self.horizontalLayout_3.addWidget(self.botao_sair)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.frame_sup)
        self.frame_med = QtWidgets.QFrame(self.centralwidget)
        self.frame_med.setStyleSheet("background-color: rgb(110, 110, 110);")
        self.frame_med.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_med.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_med.setObjectName("frame_med")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_med)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._interior = QtWidgets.QFrame(self.frame_med)
        self._interior.setMaximumSize(QtCore.QSize(450, 550))
        font = QtGui.QFont()
        font.setPointSize(14)
        self._interior.setFont(font)
        self._interior.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"border-radius: 10px;")
        self._interior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._interior.setFrameShadow(QtWidgets.QFrame.Raised)
        self._interior.setObjectName("_interior")
        self.frame = QtWidgets.QFrame(self._interior)
        self.frame.setGeometry(QtCore.QRect(160, 20, 120, 80))
        self.frame.setStyleSheet("image: url(:/logo/Dugui_1.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.campo_user = QtWidgets.QLineEdit(self._interior)
        self.campo_user.setGeometry(QtCore.QRect(30, 200, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.campo_user.setFont(font)
        self.campo_user.setMouseTracking(False)
        self.campo_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.campo_user.setStyleSheet("QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.campo_user.setMaxLength(35)
        self.campo_user.setCursorPosition(0)
        self.campo_user.setObjectName("campo_user")
        self.campo_senha = QtWidgets.QLineEdit(self._interior)
        self.campo_senha.setGeometry(QtCore.QRect(30, 290, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.campo_senha.setFont(font)
        self.campo_senha.setMouseTracking(False)
        self.campo_senha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.campo_senha.setStyleSheet("QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.campo_senha.setInputMask("")
        self.campo_senha.setMaxLength(18)
        self.campo_senha.setCursorPosition(0)
        self.campo_senha.setObjectName("campo_senha")
        self.campo_entrar = QtWidgets.QLineEdit(self._interior)
        self.campo_entrar.setGeometry(QtCore.QRect(30, 380, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.campo_entrar.setFont(font)
        self.campo_entrar.setMouseTracking(False)
        self.campo_entrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.campo_entrar.setStyleSheet("QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(20, 255, 130);\n"
"}\n"
"")
        self.campo_entrar.setInputMask("")
        self.campo_entrar.setMaxLength(18)
        self.campo_entrar.setCursorPosition(6)
        self.campo_entrar.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_entrar.setPlaceholderText("")
        self.campo_entrar.setObjectName("campo_entrar")
        self.campo_senha_3 = QtWidgets.QLineEdit(self._interior)
        self.campo_senha_3.setGeometry(QtCore.QRect(240, 380, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.campo_senha_3.setFont(font)
        self.campo_senha_3.setMouseTracking(False)
        self.campo_senha_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.campo_senha_3.setStyleSheet("QLineEdit {\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(20, 255, 130);\n"
"}\n"
"")
        self.campo_senha_3.setInputMask("")
        self.campo_senha_3.setMaxLength(18)
        self.campo_senha_3.setCursorPosition(9)
        self.campo_senha_3.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_senha_3.setPlaceholderText("")
        self.campo_senha_3.setObjectName("campo_senha_3")
        self.label_login = QtWidgets.QLabel(self._interior)
        self.label_login.setGeometry(QtCore.QRect(140, 130, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_login.setObjectName("label_login")
        self.horizontalLayout.addWidget(self._interior)
        self.verticalLayout.addWidget(self.frame_med)
        self.frame_inf = QtWidgets.QFrame(self.centralwidget)
        self.frame_inf.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_inf.setStyleSheet("background-color: rgb(110, 110, 110);")
        self.frame_inf.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_inf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inf.setObjectName("frame_inf")
        self.label = QtWidgets.QLabel(self.frame_inf)
        self.label.setGeometry(QtCore.QRect(180, 3, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame_inf)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hamburgueria DuGui"))
        self.label_error.setText(_translate("MainWindow", "Login ou senha errados"))
        self.botao_sair.setText(_translate("MainWindow", "X"))
        self.campo_user.setPlaceholderText(_translate("MainWindow", "Usuário"))
        self.campo_senha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.campo_entrar.setText(_translate("MainWindow", "Entrar"))
        self.campo_senha_3.setText(_translate("MainWindow", "Cadastrar"))
        self.label_login.setText(_translate("MainWindow", "Tela de Login"))
        self.label.setText(_translate("MainWindow", "Feynman Technology"))
#import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
