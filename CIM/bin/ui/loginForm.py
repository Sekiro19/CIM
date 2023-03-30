# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginROPOSJ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_loginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(473, 294)
        self.verticalLayout = QVBoxLayout(loginForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(loginForm)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"#mainFrame.QFrame {border-radius: 10px;\n"
"border : 4px solid rgb(48, 67, 106);\n"
"}\n"
"#loginFrame.QFrame {background-color: rgb(248, 250, 255);\n"
"border-top-right-radius: 6px;\n"
"border-bottom-right-radius: 6px;\n"
"}\n"
"#leftFrame.QFrame{\n"
"background-color: rgb(6, 35, 100);\n"
"border-top-left-radius: 6px;\n"
"border-bottom-left-radius: 6px;\n"
"}\n"
"/*QComboBox*/\n"
"QComboBox{\n"
"	color: rgb(90, 90, 90);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 30px; \n"
"	background-image: url(:/icons/bin/ui/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "90, 90, 90);\n"
"	border-radius: 0px;\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	padding: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"/*QLineEdit*/\n"
"QLineEdit {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QLineEdit:focus {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"/*QPushButton*/\n"
"QPushButton {\n"
"	background-color: rgb(6, 35, 100);\n"
"	border-radius: 5px;\n"
"	font: 14pt \"Calibri\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(9, 53, 148);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}\n"
"")
        self.mainFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.mainFrame)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMinimumSize(QSize(215, 0))
        self.leftFrame.setStyleSheet(u"")
        self.leftFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.leftFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 130))
        self.logo.setMaximumSize(QSize(16777215, 130))
        self.logo.setStyleSheet(u"image: url(:/icons/bin/ui/icons/logo.svg);")

        self.verticalLayout_6.addWidget(self.logo)

        self.label_7 = QLabel(self.leftFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(45, 62))
        self.label_7.setStyleSheet(u"font: 700 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_7)


        self.horizontalLayout_7.addWidget(self.leftFrame)

        self.loginFrame = QFrame(self.mainFrame)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setStyleSheet(u"")
        self.loginFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.loginFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.cBoxPost = QComboBox(self.loginFrame)
        self.cBoxPost.addItem("")
        self.cBoxPost.addItem("")
        self.cBoxPost.addItem("")
        self.cBoxPost.addItem("")
        self.cBoxPost.setObjectName(u"cBoxPost")
        self.cBoxPost.setMinimumSize(QSize(0, 35))
        self.cBoxPost.setMaximumSize(QSize(16777215, 35))
        self.cBoxPost.setStyleSheet(u"")
        self.cBoxPost.setEditable(False)

        self.gridLayout.addWidget(self.cBoxPost, 5, 0, 1, 3)

        self.label_50 = QLabel(self.loginFrame)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 20))
        self.label_50.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout.addWidget(self.label_50, 3, 0, 1, 1)

        self.checkBoxShowPassword = QCheckBox(self.loginFrame)
        self.checkBoxShowPassword.setObjectName(u"checkBoxShowPassword")
        self.checkBoxShowPassword.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxShowPassword.setStyleSheet(u"/*QCheckBox*/\n"
"QCheckBox {font: 12pt \"Arial\";}\n"
"QCheckBox::indicator {\n"
"    border: 2px solid rgb(103, 103, 103);\n"
"    background: rgb(6, 35, 100);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"	border-radius: 10px;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid rgb(141, 141, 141);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(186, 251, 0);\n"
"}")
        self.checkBoxShowPassword.setCheckable(True)
        self.checkBoxShowPassword.setChecked(False)
        self.checkBoxShowPassword.setTristate(False)

        self.gridLayout.addWidget(self.checkBoxShowPassword, 8, 0, 1, 3)

        self.btnConnect = QPushButton(self.loginFrame)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setMinimumSize(QSize(120, 35))
        self.btnConnect.setMaximumSize(QSize(120, 35))
        self.btnConnect.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnConnect, 9, 2, 1, 1)

        self.label_51 = QLabel(self.loginFrame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 20))
        self.label_51.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout.addWidget(self.label_51, 6, 0, 1, 3)

        self.editPassword = QLineEdit(self.loginFrame)
        self.editPassword.setObjectName(u"editPassword")
        self.editPassword.setMinimumSize(QSize(0, 35))
        self.editPassword.setMaximumSize(QSize(16777215, 35))
        self.editPassword.setStyleSheet(u"")
        self.editPassword.setEchoMode(QLineEdit.Password)
        self.editPassword.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.editPassword, 7, 0, 1, 3)

        self.label_52 = QLabel(self.loginFrame)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 20))
        self.label_52.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout.addWidget(self.label_52, 1, 0, 1, 1)

        self.cBoxServerName = QComboBox(self.loginFrame)
        self.cBoxServerName.setObjectName(u"cBoxServerName")
        self.cBoxServerName.setMinimumSize(QSize(0, 35))
        self.cBoxServerName.setMaximumSize(QSize(16777215, 35))
        self.cBoxServerName.setStyleSheet(u"")
        self.cBoxServerName.setEditable(True)

        self.gridLayout.addWidget(self.cBoxServerName, 2, 0, 1, 3)

        self.btnClose = QPushButton(self.loginFrame)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(30, 30))
        self.btnClose.setMaximumSize(QSize(30, 30))
        self.btnClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClose.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	image: url(:/icons/bin/ui/icons/icons8-close-window-50.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnClose, 1, 2, 1, 1, Qt.AlignRight)


        self.horizontalLayout_7.addWidget(self.loginFrame)


        self.verticalLayout.addWidget(self.mainFrame)


        self.retranslateUi(loginForm)

        self.cBoxPost.setCurrentIndex(0)
        self.cBoxServerName.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(QCoreApplication.translate("loginForm", u"Form", None))
        self.logo.setText("")
        self.label_7.setText(QCoreApplication.translate("loginForm", u"Compact Inventory Monitor", None))
        self.cBoxPost.setItemText(0, QCoreApplication.translate("loginForm", u"Gestionnaire de stock", None))
        self.cBoxPost.setItemText(1, QCoreApplication.translate("loginForm", u"Superviseur de l'inventaire", None))
        self.cBoxPost.setItemText(2, QCoreApplication.translate("loginForm", u"Coordonnateur du service client\u00e8le", None))
        self.cBoxPost.setItemText(3, QCoreApplication.translate("loginForm", u"dbo", None))

        self.cBoxPost.setPlaceholderText("")
        self.label_50.setText(QCoreApplication.translate("loginForm", u"Post de travail", None))
        self.checkBoxShowPassword.setText(QCoreApplication.translate("loginForm", u"Afficher le mot de passe", None))
        self.btnConnect.setText(QCoreApplication.translate("loginForm", u"connexion", None))
        self.label_51.setText(QCoreApplication.translate("loginForm", u"Mot de pass", None))
        self.label_52.setText(QCoreApplication.translate("loginForm", u"Server Name", None))
        self.cBoxServerName.setCurrentText("")
        self.cBoxServerName.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.btnClose.setToolTip(QCoreApplication.translate("loginForm", u"Ferm\u00e9e", None))
#endif // QT_CONFIG(tooltip)
        self.btnClose.setText("")
    # retranslateUi

