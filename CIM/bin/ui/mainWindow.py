# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowMOvKpc.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDateEdit, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTableView, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 517)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.styles = QFrame(self.centralwidget)
        self.styles.setObjectName(u"styles")
        self.styles.setLayoutDirection(Qt.LeftToRight)
        self.styles.setAutoFillBackground(False)
        self.styles.setStyleSheet(u"#styles.QFrame {background-color: rgb(6, 35, 100);}\n"
"#topFrame.QFrame {background-color: rgb(255, 255, 255);}\n"
"#midFrame.QFrame {background-color: rgb(248, 250, 255);}\n"
"#logo {image: url(:/icons/bin/ui/icons/logo.svg);}\n"
"/*_______________Fixed_Styles______________*/\n"
"QLabel {font: 12pt \"Arial\";}\n"
"/*QPlainTextEdit*/\n"
"QPlainTextEdit {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
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
""
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
"/*QDoubleSpinBox*/\n"
""
                        "QDoubleSpinBox, QSpinBox {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QDoubleSpinBox:focus, QSpinBox:focus {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-top.png);\n"
"}\n"
"QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-bottom.png);\n"
"}\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button, QSpinBox::up-button, QSpinBox::down-button {\n"
"    background: transparent;\n"
"}\n"
"/*QDateEdit*/\n"
"QDateEdit, QDateTimeEdit{\n"
"	color: rgb(90, 90, 90);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	padding: 5px;\n"
"}\n"
"QDateEdit:hover, QDateTimeEdit:hover{\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 13"
                        "2, 159);\n"
"}\n"
"QDateEdit::up-arrow, QDateTimeEdit::up-arrow{\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-top.png);\n"
"}\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow{\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-bottom.png);\n"
"}\n"
"QDateEdit::up-button, QDateEdit::down-button, QDateTimeEdit::up-button, QDateTimeEdit::down-button {\n"
"    background: transparent;\n"
"}\n"
"/*QToolBox*/\n"
"QToolBox QPushButton {\n"
"	background-color: transparent;\n"
"    color: rgb(220,220,220);\n"
"	font: 600 12pt \"Segoe UI\";\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"QToolBox QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QToolBox QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QToolBox::tab {\n"
"	border-radius: none;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"    color: rgb(137, 156, 176);\n"
"	padding-left: 10px;\n"
"	background-repeat: none;\n"
"\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
""
                        "	color: rgb(255, 255, 255);\n"
"	background-color: rgb(48, 67, 106);\n"
"	border-left: 4px solid rgb(0, 249, 248);\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"	background-color: rgb(48, 67, 106);\n"
"}\n"
"/*QCheckBox*/\n"
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
"}\n"
"/*QScrollArea*/\n"
"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"QScrollArea > QWidget > QScrollBar { background: palette(base); }\n"
"/*QScrollBar*/\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {background-color: rgb(9, 52, 147);}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
""
                        "    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(6, 35, 100);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"	width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {background: none;}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {background: none;}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin:"
                        " 21px 0 21px 0;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"    background: rgb(6, 35, 100);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/*QTableView QHeaderView::section {padding-right: auto;}*/\n"
"QTableView {\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"QHeaderView {font: 400 15pt \"Segoe UI\";}\n"
"\n"
"QHeaderView::section:h"
                        "orizontal {\n"
"	background-color: rgb(248, 250, 255);\n"
"	border: none;\n"
"	font: 400 11pt \"Segoe UI\";\n"
"}\n"
"QTableView::item {\n"
"	padding-left: 15px;\n"
"	border-bottom: 1px solid rgb(235, 235, 235);\n"
"}\n"
"QTableView::item:selected {\n"
"	background-color: rgba(248, 250, 255, 127);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.styles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.styles)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideFrame = QFrame(self.styles)
        self.sideFrame.setObjectName(u"sideFrame")
        self.sideFrame.setMinimumSize(QSize(230, 0))
        self.sideFrame.setMaximumSize(QSize(230, 16777215))
        self.sideFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sideFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sideBtnFrame = QFrame(self.sideFrame)
        self.sideBtnFrame.setObjectName(u"sideBtnFrame")
        self.sideBtnFrame.setStyleSheet(u"")
        self.sideBtnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sideBtnFrame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.sideBtnFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 70))
        self.logo.setMaximumSize(QSize(16777215, 70))
        self.logo.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.logo)

        self.label = QLabel(self.sideBtnFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(45, 62))
        self.label.setStyleSheet(u"font: 700 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignTop)

        self.toolBox = QToolBox(self.sideBtnFrame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 300))
        self.toolBox.setMaximumSize(QSize(16777215, 325))
        self.tabDepot = QWidget()
        self.tabDepot.setObjectName(u"tabDepot")
        self.tabDepot.setGeometry(QRect(0, 0, 230, 88))
        self.tabDepot.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.tabDepot)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnPageProduit = QPushButton(self.tabDepot)
        self.btnPageProduit.setObjectName(u"btnPageProduit")
        self.btnPageProduit.setMaximumSize(QSize(16777215, 25))
        self.btnPageProduit.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/bin/ui/icons/icons8-yogurt-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageProduit.setIcon(icon)
        self.btnPageProduit.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.btnPageProduit)

        self.btnPageStock = QPushButton(self.tabDepot)
        self.btnPageStock.setObjectName(u"btnPageStock")
        self.btnPageStock.setMaximumSize(QSize(16777215, 25))
        self.btnPageStock.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/bin/ui/icons/icons8-warehouse-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageStock.setIcon(icon1)
        self.btnPageStock.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.btnPageStock)

        self.btnPageInv = QPushButton(self.tabDepot)
        self.btnPageInv.setObjectName(u"btnPageInv")
        self.btnPageInv.setMaximumSize(QSize(16777215, 25))
        self.btnPageInv.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/bin/ui/icons/icons8-inventory-management-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageInv.setIcon(icon2)
        self.btnPageInv.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.btnPageInv)

        self.btnPageMS = QPushButton(self.tabDepot)
        self.btnPageMS.setObjectName(u"btnPageMS")
        self.btnPageMS.setMaximumSize(QSize(16777215, 25))
        self.btnPageMS.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/bin/ui/icons/icons8-left-and-right-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageMS.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.btnPageMS)

        self.toolBox.addItem(self.tabDepot, u"D\u00e9p\u00f4t ")
        self.tabClient = QWidget()
        self.tabClient.setObjectName(u"tabClient")
        self.tabClient.setGeometry(QRect(0, 0, 230, 66))
        self.verticalLayout_17 = QVBoxLayout(self.tabClient)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btnPageClient = QPushButton(self.tabClient)
        self.btnPageClient.setObjectName(u"btnPageClient")
        self.btnPageClient.setMaximumSize(QSize(16777215, 25))
        self.btnPageClient.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/bin/ui/icons/icons8-user-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageClient.setIcon(icon4)

        self.verticalLayout_17.addWidget(self.btnPageClient, 0, Qt.AlignTop)

        self.toolBox.addItem(self.tabClient, u"Client")
        self.tabCmd = QWidget()
        self.tabCmd.setObjectName(u"tabCmd")
        self.tabCmd.setGeometry(QRect(0, 0, 230, 66))
        self.verticalLayout_31 = QVBoxLayout(self.tabCmd)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.btnPageCmd = QPushButton(self.tabCmd)
        self.btnPageCmd.setObjectName(u"btnPageCmd")
        self.btnPageCmd.setMaximumSize(QSize(16777215, 25))
        self.btnPageCmd.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/bin/ui/icons/icons8-purchase-order-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageCmd.setIcon(icon5)

        self.verticalLayout_31.addWidget(self.btnPageCmd)

        self.btnPageInsertCmd = QPushButton(self.tabCmd)
        self.btnPageInsertCmd.setObjectName(u"btnPageInsertCmd")
        self.btnPageInsertCmd.setMaximumSize(QSize(16777215, 25))
        self.btnPageInsertCmd.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_31.addWidget(self.btnPageInsertCmd, 0, Qt.AlignTop)

        self.toolBox.addItem(self.tabCmd, u"Commande")
        self.tabFac = QWidget()
        self.tabFac.setObjectName(u"tabFac")
        self.tabFac.setGeometry(QRect(0, 0, 230, 66))
        self.verticalLayout_32 = QVBoxLayout(self.tabFac)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.btnPageFacture = QPushButton(self.tabFac)
        self.btnPageFacture.setObjectName(u"btnPageFacture")
        self.btnPageFacture.setMaximumSize(QSize(16777215, 25))
        self.btnPageFacture.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/bin/ui/icons/icons8-cheque-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageFacture.setIcon(icon6)

        self.verticalLayout_32.addWidget(self.btnPageFacture)

        self.btnPageInsertFacture = QPushButton(self.tabFac)
        self.btnPageInsertFacture.setObjectName(u"btnPageInsertFacture")
        self.btnPageInsertFacture.setMaximumSize(QSize(16777215, 25))
        self.btnPageInsertFacture.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_32.addWidget(self.btnPageInsertFacture, 0, Qt.AlignTop)

        self.toolBox.addItem(self.tabFac, u"Facture")
        self.tabLiv = QWidget()
        self.tabLiv.setObjectName(u"tabLiv")
        self.tabLiv.setGeometry(QRect(0, 0, 230, 66))
        self.verticalLayout_38 = QVBoxLayout(self.tabLiv)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.btnPageLiv = QPushButton(self.tabLiv)
        self.btnPageLiv.setObjectName(u"btnPageLiv")
        self.btnPageLiv.setMaximumSize(QSize(16777215, 25))
        self.btnPageLiv.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/bin/ui/icons/icons8-deliver-food-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageLiv.setIcon(icon7)

        self.verticalLayout_38.addWidget(self.btnPageLiv)

        self.btnPageInsertLiv = QPushButton(self.tabLiv)
        self.btnPageInsertLiv.setObjectName(u"btnPageInsertLiv")
        self.btnPageInsertLiv.setMinimumSize(QSize(0, 0))
        self.btnPageInsertLiv.setMaximumSize(QSize(16777215, 25))
        self.btnPageInsertLiv.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_38.addWidget(self.btnPageInsertLiv, 0, Qt.AlignTop)

        self.toolBox.addItem(self.tabLiv, u"Livraison")
        self.tabTools = QWidget()
        self.tabTools.setObjectName(u"tabTools")
        self.tabTools.setGeometry(QRect(0, 0, 230, 66))
        self.verticalLayout_48 = QVBoxLayout(self.tabTools)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.btnPageCharts = QPushButton(self.tabTools)
        self.btnPageCharts.setObjectName(u"btnPageCharts")
        self.btnPageCharts.setMaximumSize(QSize(16777215, 25))
        self.btnPageCharts.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/bin/ui/icons/icons8-combo-chart-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageCharts.setIcon(icon8)
        self.btnPageCharts.setIconSize(QSize(16, 16))

        self.verticalLayout_48.addWidget(self.btnPageCharts, 0, Qt.AlignTop)

        self.btnPageReport = QPushButton(self.tabTools)
        self.btnPageReport.setObjectName(u"btnPageReport")
        self.btnPageReport.setMaximumSize(QSize(16777215, 25))
        self.btnPageReport.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/bin/ui/icons/icons8-document-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageReport.setIcon(icon9)
        self.btnPageReport.setIconSize(QSize(16, 16))

        self.verticalLayout_48.addWidget(self.btnPageReport, 0, Qt.AlignTop)

        self.toolBox.addItem(self.tabTools, u"Tools")

        self.verticalLayout_4.addWidget(self.toolBox, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.sideBtnFrame, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sideFrame)

        self.mainFrame = QFrame(self.styles)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 3, 6, 6)
        self.topFrame = QFrame(self.mainFrame)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMinimumSize(QSize(0, 50))
        self.topFrame.setMaximumSize(QSize(16777215, 40))
        self.topFrame.setStyleSheet(u"")
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.btnRollback = QPushButton(self.topFrame)
        self.btnRollback.setObjectName(u"btnRollback")
        self.btnRollback.setMinimumSize(QSize(40, 40))
        self.btnRollback.setMaximumSize(QSize(40, 40))
        self.btnRollback.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRollback.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	image: url(:/icons/bin/ui/icons/icons8-rollback-100.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnRollback)

        self.btnLoad = QPushButton(self.topFrame)
        self.btnLoad.setObjectName(u"btnLoad")
        self.btnLoad.setMinimumSize(QSize(40, 40))
        self.btnLoad.setMaximumSize(QSize(40, 40))
        self.btnLoad.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoad.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	image: url(:/icons/bin/ui/icons/icons8-database-migration-100.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnLoad)

        self.btnConnect = QPushButton(self.topFrame)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setMinimumSize(QSize(40, 40))
        self.btnConnect.setMaximumSize(QSize(40, 40))
        self.btnConnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConnect.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	image: url(:/icons/bin/ui/icons/icons8-sql-100.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnConnect)


        self.verticalLayout_2.addWidget(self.topFrame)

        self.midFrame = QFrame(self.mainFrame)
        self.midFrame.setObjectName(u"midFrame")
        self.midFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.midFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.midFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageProduit = QWidget()
        self.pageProduit.setObjectName(u"pageProduit")
        self.pageProduit.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.pageProduit)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pageProduit)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 762, 173))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 15, -1, -1)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, -1, 15, -1)
        self.editFilterProduit = QLineEdit(self.frame_2)
        self.editFilterProduit.setObjectName(u"editFilterProduit")
        self.editFilterProduit.setMinimumSize(QSize(300, 35))
        self.editFilterProduit.setMaximumSize(QSize(300, 16777215))
        self.editFilterProduit.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.editFilterProduit)

        self.cboxFilterProduit = QComboBox(self.frame_2)
        self.cboxFilterProduit.setObjectName(u"cboxFilterProduit")
        self.cboxFilterProduit.setMinimumSize(QSize(170, 35))
        self.cboxFilterProduit.setMaximumSize(QSize(170, 35))
        self.cboxFilterProduit.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.cboxFilterProduit)

        self.btnRechProduit = QPushButton(self.frame_2)
        self.btnRechProduit.setObjectName(u"btnRechProduit")
        self.btnRechProduit.setMinimumSize(QSize(110, 35))
        self.btnRechProduit.setMaximumSize(QSize(110, 35))
        self.btnRechProduit.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.btnRechProduit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btnPageProduitInsert = QPushButton(self.frame_2)
        self.btnPageProduitInsert.setObjectName(u"btnPageProduitInsert")
        self.btnPageProduitInsert.setMinimumSize(QSize(110, 35))
        self.btnPageProduitInsert.setMaximumSize(QSize(110, 35))
        self.btnPageProduitInsert.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.btnPageProduitInsert)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 9, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(14, 0, 14, 5)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.label_91 = QLabel(self.frame_4)
        self.label_91.setObjectName(u"label_91")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy1)
        self.label_91.setMinimumSize(QSize(100, 0))
        self.label_91.setMaximumSize(QSize(100, 16777215))
        self.label_91.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_91.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_91, 0, Qt.AlignLeft)

        self.sboxProduitFetchRows = QSpinBox(self.frame_4)
        self.sboxProduitFetchRows.setObjectName(u"sboxProduitFetchRows")
        self.sboxProduitFetchRows.setEnabled(True)
        self.sboxProduitFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxProduitFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxProduitFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxProduitFetchRows.setMinimum(0)
        self.sboxProduitFetchRows.setMaximum(999999999)
        self.sboxProduitFetchRows.setValue(100)

        self.horizontalLayout_5.addWidget(self.sboxProduitFetchRows)

        self.label_92 = QLabel(self.frame_4)
        self.label_92.setObjectName(u"label_92")
        sizePolicy1.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy1)
        self.label_92.setMinimumSize(QSize(50, 0))
        self.label_92.setMaximumSize(QSize(27, 16777215))
        self.label_92.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_92.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_92, 0, Qt.AlignLeft)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        self.refreshProduit = QPushButton(self.frame_4)
        self.refreshProduit.setObjectName(u"refreshProduit")
        self.refreshProduit.setMinimumSize(QSize(20, 20))
        self.refreshProduit.setMaximumSize(QSize(20, 20))
        self.refreshProduit.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshProduit.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.refreshProduit)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.tableViewProduit = QTableView(self.frame)
        self.tableViewProduit.setObjectName(u"tableViewProduit")
        self.tableViewProduit.setStyleSheet(u"")
        self.tableViewProduit.setFrameShape(QFrame.NoFrame)
        self.tableViewProduit.setFrameShadow(QFrame.Plain)
        self.tableViewProduit.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewProduit.setTabKeyNavigation(True)
        self.tableViewProduit.setProperty("showDropIndicator", False)
        self.tableViewProduit.setDragDropOverwriteMode(False)
        self.tableViewProduit.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewProduit.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewProduit.setTextElideMode(Qt.ElideNone)
        self.tableViewProduit.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewProduit.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewProduit.setShowGrid(False)
        self.tableViewProduit.setSortingEnabled(True)
        self.tableViewProduit.setWordWrap(False)
        self.tableViewProduit.setCornerButtonEnabled(False)
        self.tableViewProduit.horizontalHeader().setHighlightSections(False)
        self.tableViewProduit.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewProduit.horizontalHeader().setStretchLastSection(True)
        self.tableViewProduit.verticalHeader().setVisible(False)
        self.tableViewProduit.verticalHeader().setHighlightSections(False)

        self.verticalLayout_9.addWidget(self.tableViewProduit)


        self.verticalLayout_8.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.pageProduit)
        self.pageCommande = QWidget()
        self.pageCommande.setObjectName(u"pageCommande")
        self.verticalLayout_29 = QVBoxLayout(self.pageCommande)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.pageCommande)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"")
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setFrameShadow(QFrame.Plain)
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 752, 295))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 15, -1, -1)
        self.frame_17 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setMaximumSize(QSize(16777215, 190))
        self.frame_17.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_17.setFrameShadow(QFrame.Plain)
        self.verticalLayout_27 = QVBoxLayout(self.frame_17)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.editFilterCmd = QLineEdit(self.frame_17)
        self.editFilterCmd.setObjectName(u"editFilterCmd")
        self.editFilterCmd.setMinimumSize(QSize(300, 35))
        self.editFilterCmd.setMaximumSize(QSize(300, 16777215))
        self.editFilterCmd.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.editFilterCmd)

        self.cboxFilterCmd = QComboBox(self.frame_17)
        self.cboxFilterCmd.setObjectName(u"cboxFilterCmd")
        self.cboxFilterCmd.setMinimumSize(QSize(170, 35))
        self.cboxFilterCmd.setMaximumSize(QSize(170, 35))
        self.cboxFilterCmd.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.cboxFilterCmd)

        self.btnRechCmd = QPushButton(self.frame_17)
        self.btnRechCmd.setObjectName(u"btnRechCmd")
        self.btnRechCmd.setMinimumSize(QSize(110, 35))
        self.btnRechCmd.setMaximumSize(QSize(110, 35))
        self.btnRechCmd.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btnRechCmd)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.btnPageCmdInsert = QPushButton(self.frame_17)
        self.btnPageCmdInsert.setObjectName(u"btnPageCmdInsert")
        self.btnPageCmdInsert.setMinimumSize(QSize(110, 35))
        self.btnPageCmdInsert.setMaximumSize(QSize(110, 35))
        self.btnPageCmdInsert.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btnPageCmdInsert)


        self.verticalLayout_27.addLayout(self.horizontalLayout_12)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.dateDCCmdFilterT1 = QDateEdit(self.frame_17)
        self.dateDCCmdFilterT1.setObjectName(u"dateDCCmdFilterT1")
        self.dateDCCmdFilterT1.setEnabled(True)
        self.dateDCCmdFilterT1.setMinimumSize(QSize(0, 35))
        self.dateDCCmdFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDCCmdFilterT1.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDCCmdFilterT1.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_2.addWidget(self.dateDCCmdFilterT1, 1, 4, 1, 1)

        self.checkBoxDCfilterCmd = QCheckBox(self.frame_17)
        self.checkBoxDCfilterCmd.setObjectName(u"checkBoxDCfilterCmd")
        self.checkBoxDCfilterCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDCfilterCmd.setStyleSheet(u"")
        self.checkBoxDCfilterCmd.setCheckable(True)
        self.checkBoxDCfilterCmd.setChecked(True)
        self.checkBoxDCfilterCmd.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBoxDCfilterCmd, 0, 3, 1, 2, Qt.AlignLeft|Qt.AlignTop)

        self.line_7 = QFrame(self.frame_17)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(3, 0))
        self.line_7.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 0, 2, 3, 1)

        self.label_54 = QLabel(self.frame_17)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(20, 16777215))
        self.label_54.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_54, 1, 3, 1, 1)

        self.checkBoxQfilterCmd = QCheckBox(self.frame_17)
        self.checkBoxQfilterCmd.setObjectName(u"checkBoxQfilterCmd")
        self.checkBoxQfilterCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxQfilterCmd.setStyleSheet(u"")
        self.checkBoxQfilterCmd.setCheckable(True)
        self.checkBoxQfilterCmd.setChecked(True)
        self.checkBoxQfilterCmd.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBoxQfilterCmd, 0, 6, 1, 2)

        self.line_4 = QFrame(self.frame_17)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(3, 0))
        self.line_4.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 0, 5, 3, 1)

        self.label_55 = QLabel(self.frame_17)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(30, 16777215))
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_55, 2, 6, 1, 1)

        self.dateDCCmdFilterT2 = QDateEdit(self.frame_17)
        self.dateDCCmdFilterT2.setObjectName(u"dateDCCmdFilterT2")
        self.dateDCCmdFilterT2.setEnabled(True)
        self.dateDCCmdFilterT2.setMinimumSize(QSize(0, 35))
        self.dateDCCmdFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDCCmdFilterT2.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDCCmdFilterT2.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_2.addWidget(self.dateDCCmdFilterT2, 2, 4, 1, 1)

        self.label_32 = QLabel(self.frame_17)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 20))
        self.label_32.setStyleSheet(u"")
        self.label_32.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_32, 0, 8, 1, 2)

        self.label_57 = QLabel(self.frame_17)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(20, 16777215))
        self.label_57.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_57, 2, 3, 1, 1)

        self.label_58 = QLabel(self.frame_17)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(30, 16777215))
        self.label_58.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_58, 1, 6, 1, 1)

        self.cboxUQCmdFilter = QComboBox(self.frame_17)
        self.cboxUQCmdFilter.addItem("")
        self.cboxUQCmdFilter.addItem("")
        self.cboxUQCmdFilter.addItem("")
        self.cboxUQCmdFilter.setObjectName(u"cboxUQCmdFilter")
        self.cboxUQCmdFilter.setEnabled(True)
        self.cboxUQCmdFilter.setMinimumSize(QSize(110, 35))
        self.cboxUQCmdFilter.setMaximumSize(QSize(110, 35))
        self.cboxUQCmdFilter.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.cboxUQCmdFilter, 1, 8, 1, 2)

        self.sboxQCmdFilterMin = QSpinBox(self.frame_17)
        self.sboxQCmdFilterMin.setObjectName(u"sboxQCmdFilterMin")
        self.sboxQCmdFilterMin.setEnabled(True)
        self.sboxQCmdFilterMin.setMinimumSize(QSize(0, 35))
        self.sboxQCmdFilterMin.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQCmdFilterMin.setMinimum(0)
        self.sboxQCmdFilterMin.setMaximum(999999999)

        self.gridLayout_2.addWidget(self.sboxQCmdFilterMin, 1, 7, 1, 1)

        self.sboxQCmdFilterMax = QSpinBox(self.frame_17)
        self.sboxQCmdFilterMax.setObjectName(u"sboxQCmdFilterMax")
        self.sboxQCmdFilterMax.setEnabled(True)
        self.sboxQCmdFilterMax.setMinimumSize(QSize(0, 35))
        self.sboxQCmdFilterMax.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQCmdFilterMax.setMinimum(0)
        self.sboxQCmdFilterMax.setMaximum(999999999)

        self.gridLayout_2.addWidget(self.sboxQCmdFilterMax, 2, 7, 1, 1)

        self.cboxCalcCmd = QComboBox(self.frame_17)
        self.cboxCalcCmd.addItem("")
        self.cboxCalcCmd.addItem("")
        self.cboxCalcCmd.setObjectName(u"cboxCalcCmd")
        self.cboxCalcCmd.setEnabled(True)
        self.cboxCalcCmd.setMinimumSize(QSize(110, 35))
        self.cboxCalcCmd.setMaximumSize(QSize(16777215, 35))
        self.cboxCalcCmd.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.cboxCalcCmd, 1, 0, 1, 2)

        self.btnCalcCmd = QPushButton(self.frame_17)
        self.btnCalcCmd.setObjectName(u"btnCalcCmd")
        self.btnCalcCmd.setMinimumSize(QSize(110, 35))
        self.btnCalcCmd.setMaximumSize(QSize(16777215, 35))
        self.btnCalcCmd.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btnCalcCmd, 2, 0, 1, 2)

        self.label_53 = QLabel(self.frame_17)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(16777215, 20))
        self.label_53.setStyleSheet(u"")
        self.label_53.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_53, 0, 0, 1, 2)


        self.verticalLayout_27.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_2)


        self.verticalLayout_26.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QSize(0, 0))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_18)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 9, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setSpacing(9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(14, 0, 14, 5)
        self.label_59 = QLabel(self.frame_19)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_13.addWidget(self.label_59, 0, Qt.AlignLeft)

        self.label_93 = QLabel(self.frame_19)
        self.label_93.setObjectName(u"label_93")
        sizePolicy1.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy1)
        self.label_93.setMinimumSize(QSize(100, 0))
        self.label_93.setMaximumSize(QSize(16777215, 16777215))
        self.label_93.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_93.setWordWrap(False)

        self.horizontalLayout_13.addWidget(self.label_93, 0, Qt.AlignLeft)

        self.sboxCmdFetchRows = QSpinBox(self.frame_19)
        self.sboxCmdFetchRows.setObjectName(u"sboxCmdFetchRows")
        self.sboxCmdFetchRows.setEnabled(True)
        self.sboxCmdFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxCmdFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxCmdFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxCmdFetchRows.setMinimum(0)
        self.sboxCmdFetchRows.setMaximum(999999999)
        self.sboxCmdFetchRows.setValue(10)

        self.horizontalLayout_13.addWidget(self.sboxCmdFetchRows, 0, Qt.AlignLeft)

        self.label_94 = QLabel(self.frame_19)
        self.label_94.setObjectName(u"label_94")
        sizePolicy1.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy1)
        self.label_94.setMinimumSize(QSize(50, 0))
        self.label_94.setMaximumSize(QSize(27, 16777215))
        self.label_94.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_94.setWordWrap(False)

        self.horizontalLayout_13.addWidget(self.label_94, 0, Qt.AlignLeft)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.checkBoxViewTypeCmd = QCheckBox(self.frame_19)
        self.checkBoxViewTypeCmd.setObjectName(u"checkBoxViewTypeCmd")
        self.checkBoxViewTypeCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxViewTypeCmd.setStyleSheet(u"")
        self.checkBoxViewTypeCmd.setCheckable(True)
        self.checkBoxViewTypeCmd.setChecked(False)
        self.checkBoxViewTypeCmd.setTristate(False)

        self.horizontalLayout_13.addWidget(self.checkBoxViewTypeCmd)

        self.label_60 = QLabel(self.frame_19)
        self.label_60.setObjectName(u"label_60")
        sizePolicy1.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy1)
        self.label_60.setMinimumSize(QSize(68, 0))
        self.label_60.setMaximumSize(QSize(20, 16777215))
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_60)

        self.vBoxShowColsCmd = QVBoxLayout()
        self.vBoxShowColsCmd.setObjectName(u"vBoxShowColsCmd")

        self.horizontalLayout_13.addLayout(self.vBoxShowColsCmd)

        self.refreshCmd = QPushButton(self.frame_19)
        self.refreshCmd.setObjectName(u"refreshCmd")
        self.refreshCmd.setMinimumSize(QSize(20, 20))
        self.refreshCmd.setMaximumSize(QSize(20, 20))
        self.refreshCmd.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshCmd.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.refreshCmd)


        self.verticalLayout_28.addWidget(self.frame_19)

        self.tableViewCmd = QTableView(self.frame_18)
        self.tableViewCmd.setObjectName(u"tableViewCmd")
        self.tableViewCmd.setStyleSheet(u"")
        self.tableViewCmd.setFrameShape(QFrame.NoFrame)
        self.tableViewCmd.setFrameShadow(QFrame.Plain)
        self.tableViewCmd.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewCmd.setTabKeyNavigation(True)
        self.tableViewCmd.setProperty("showDropIndicator", False)
        self.tableViewCmd.setDragDropOverwriteMode(False)
        self.tableViewCmd.setAlternatingRowColors(False)
        self.tableViewCmd.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewCmd.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewCmd.setTextElideMode(Qt.ElideNone)
        self.tableViewCmd.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewCmd.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewCmd.setShowGrid(False)
        self.tableViewCmd.setSortingEnabled(True)
        self.tableViewCmd.setWordWrap(False)
        self.tableViewCmd.setCornerButtonEnabled(False)
        self.tableViewCmd.horizontalHeader().setHighlightSections(False)
        self.tableViewCmd.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewCmd.horizontalHeader().setStretchLastSection(True)
        self.tableViewCmd.verticalHeader().setVisible(False)
        self.tableViewCmd.verticalHeader().setHighlightSections(False)

        self.verticalLayout_28.addWidget(self.tableViewCmd)


        self.verticalLayout_26.addWidget(self.frame_18)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_29.addWidget(self.scrollArea_5)

        self.stackedWidget.addWidget(self.pageCommande)
        self.pageInsertCommande = QWidget()
        self.pageInsertCommande.setObjectName(u"pageInsertCommande")
        self.verticalLayout_30 = QVBoxLayout(self.pageInsertCommande)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_20 = QFrame(self.pageInsertCommande)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setMinimumSize(QSize(640, 440))
        self.frame_20.setMaximumSize(QSize(640, 440))
        self.frame_20.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.frame_20)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(6)
        self.gridLayout_8.setContentsMargins(-1, -1, -1, 9)
        self.btnInsertCmd = QPushButton(self.frame_20)
        self.btnInsertCmd.setObjectName(u"btnInsertCmd")
        self.btnInsertCmd.setMinimumSize(QSize(110, 35))
        self.btnInsertCmd.setMaximumSize(QSize(110, 35))
        self.btnInsertCmd.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.btnInsertCmd, 5, 4, 1, 1)

        self.cBoxModePaiementCmdInsert = QComboBox(self.frame_20)
        self.cBoxModePaiementCmdInsert.addItem("")
        self.cBoxModePaiementCmdInsert.addItem("")
        self.cBoxModePaiementCmdInsert.addItem("")
        self.cBoxModePaiementCmdInsert.addItem("")
        self.cBoxModePaiementCmdInsert.addItem("")
        self.cBoxModePaiementCmdInsert.setObjectName(u"cBoxModePaiementCmdInsert")
        self.cBoxModePaiementCmdInsert.setMinimumSize(QSize(0, 35))
        self.cBoxModePaiementCmdInsert.setMaximumSize(QSize(16777215, 35))
        self.cBoxModePaiementCmdInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cBoxModePaiementCmdInsert.setEditable(False)

        self.gridLayout_8.addWidget(self.cBoxModePaiementCmdInsert, 5, 1, 1, 1)

        self.labelInsertCmd = QLabel(self.frame_20)
        self.labelInsertCmd.setObjectName(u"labelInsertCmd")
        self.labelInsertCmd.setMaximumSize(QSize(16777215, 70))
        self.labelInsertCmd.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelInsertCmd.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.labelInsertCmd, 0, 0, 1, 6)

        self.tableWidgetCmd = QTableWidget(self.frame_20)
        if (self.tableWidgetCmd.columnCount() < 4):
            self.tableWidgetCmd.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidgetCmd.setObjectName(u"tableWidgetCmd")
        self.tableWidgetCmd.setFrameShape(QFrame.NoFrame)
        self.tableWidgetCmd.setProperty("showDropIndicator", False)
        self.tableWidgetCmd.setDragDropOverwriteMode(False)
        self.tableWidgetCmd.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidgetCmd.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetCmd.setTextElideMode(Qt.ElideNone)
        self.tableWidgetCmd.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetCmd.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetCmd.setGridStyle(Qt.NoPen)
        self.tableWidgetCmd.setSortingEnabled(True)
        self.tableWidgetCmd.setWordWrap(False)
        self.tableWidgetCmd.setCornerButtonEnabled(False)
        self.tableWidgetCmd.setRowCount(0)
        self.tableWidgetCmd.horizontalHeader().setVisible(True)
        self.tableWidgetCmd.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetCmd.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidgetCmd.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidgetCmd.horizontalHeader().setHighlightSections(False)
        self.tableWidgetCmd.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidgetCmd.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetCmd.verticalHeader().setVisible(False)
        self.tableWidgetCmd.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetCmd.verticalHeader().setMinimumSectionSize(40)
        self.tableWidgetCmd.verticalHeader().setDefaultSectionSize(40)
        self.tableWidgetCmd.verticalHeader().setHighlightSections(False)

        self.gridLayout_8.addWidget(self.tableWidgetCmd, 10, 0, 3, 6)

        self.btnUpdateCmd = QPushButton(self.frame_20)
        self.btnUpdateCmd.setObjectName(u"btnUpdateCmd")
        self.btnUpdateCmd.setMinimumSize(QSize(110, 35))
        self.btnUpdateCmd.setMaximumSize(QSize(110, 35))
        self.btnUpdateCmd.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.btnUpdateCmd, 5, 5, 1, 1)

        self.btnSubRowCmd = QPushButton(self.frame_20)
        self.btnSubRowCmd.setObjectName(u"btnSubRowCmd")
        self.btnSubRowCmd.setMinimumSize(QSize(35, 35))
        self.btnSubRowCmd.setMaximumSize(QSize(35, 35))
        self.btnSubRowCmd.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.btnSubRowCmd, 5, 3, 1, 1)

        self.cBoxCodeClientCmdInsert = QComboBox(self.frame_20)
        self.cBoxCodeClientCmdInsert.setObjectName(u"cBoxCodeClientCmdInsert")
        self.cBoxCodeClientCmdInsert.setMinimumSize(QSize(0, 35))
        self.cBoxCodeClientCmdInsert.setMaximumSize(QSize(16777215, 35))
        self.cBoxCodeClientCmdInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cBoxCodeClientCmdInsert.setEditable(True)

        self.gridLayout_8.addWidget(self.cBoxCodeClientCmdInsert, 5, 0, 1, 1)

        self.label_66 = QLabel(self.frame_20)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777215, 20))
        self.label_66.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_8.addWidget(self.label_66, 1, 1, 1, 1)

        self.btnAddRowCmd = QPushButton(self.frame_20)
        self.btnAddRowCmd.setObjectName(u"btnAddRowCmd")
        self.btnAddRowCmd.setMinimumSize(QSize(35, 35))
        self.btnAddRowCmd.setMaximumSize(QSize(35, 35))
        self.btnAddRowCmd.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.btnAddRowCmd, 5, 2, 1, 1)

        self.label_62 = QLabel(self.frame_20)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(16777215, 20))
        self.label_62.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_8.addWidget(self.label_62, 1, 0, 1, 1)


        self.verticalLayout_30.addWidget(self.frame_20, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageInsertCommande)
        self.pageFacture = QWidget()
        self.pageFacture.setObjectName(u"pageFacture")
        self.verticalLayout_36 = QVBoxLayout(self.pageFacture)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.pageFacture)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u"")
        self.scrollArea_6.setFrameShape(QFrame.NoFrame)
        self.scrollArea_6.setFrameShadow(QFrame.Plain)
        self.scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 773, 295))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 15, -1, -1)
        self.frame_21 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 190))
        self.frame_21.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_21.setFrameShadow(QFrame.Plain)
        self.verticalLayout_34 = QVBoxLayout(self.frame_21)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.editFilterFacture = QLineEdit(self.frame_21)
        self.editFilterFacture.setObjectName(u"editFilterFacture")
        self.editFilterFacture.setMinimumSize(QSize(300, 35))
        self.editFilterFacture.setMaximumSize(QSize(300, 16777215))
        self.editFilterFacture.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_14.addWidget(self.editFilterFacture)

        self.cboxFilterFacture = QComboBox(self.frame_21)
        self.cboxFilterFacture.setObjectName(u"cboxFilterFacture")
        self.cboxFilterFacture.setMinimumSize(QSize(170, 35))
        self.cboxFilterFacture.setMaximumSize(QSize(170, 35))
        self.cboxFilterFacture.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.cboxFilterFacture)

        self.btnRechFacture = QPushButton(self.frame_21)
        self.btnRechFacture.setObjectName(u"btnRechFacture")
        self.btnRechFacture.setMinimumSize(QSize(110, 35))
        self.btnRechFacture.setMaximumSize(QSize(110, 35))
        self.btnRechFacture.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btnRechFacture)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.btnPageFactureInsert = QPushButton(self.frame_21)
        self.btnPageFactureInsert.setObjectName(u"btnPageFactureInsert")
        self.btnPageFactureInsert.setMinimumSize(QSize(110, 35))
        self.btnPageFactureInsert.setMaximumSize(QSize(110, 35))
        self.btnPageFactureInsert.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btnPageFactureInsert)


        self.verticalLayout_34.addLayout(self.horizontalLayout_14)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(15)
        self.gridLayout_9.setContentsMargins(-1, 5, -1, -1)
        self.dateDFFactureFilterT1 = QDateEdit(self.frame_21)
        self.dateDFFactureFilterT1.setObjectName(u"dateDFFactureFilterT1")
        self.dateDFFactureFilterT1.setEnabled(True)
        self.dateDFFactureFilterT1.setMinimumSize(QSize(0, 35))
        self.dateDFFactureFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDFFactureFilterT1.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDFFactureFilterT1.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_9.addWidget(self.dateDFFactureFilterT1, 1, 4, 1, 1)

        self.checkBoxDFfilterFacture = QCheckBox(self.frame_21)
        self.checkBoxDFfilterFacture.setObjectName(u"checkBoxDFfilterFacture")
        self.checkBoxDFfilterFacture.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDFfilterFacture.setStyleSheet(u"")
        self.checkBoxDFfilterFacture.setCheckable(True)
        self.checkBoxDFfilterFacture.setChecked(True)
        self.checkBoxDFfilterFacture.setTristate(False)

        self.gridLayout_9.addWidget(self.checkBoxDFfilterFacture, 0, 3, 1, 2, Qt.AlignLeft|Qt.AlignTop)

        self.line_8 = QFrame(self.frame_21)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(3, 0))
        self.line_8.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_8, 0, 2, 3, 1)

        self.label_56 = QLabel(self.frame_21)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(20, 16777215))
        self.label_56.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_56, 1, 3, 1, 1)

        self.checkBoxQfilterFacture = QCheckBox(self.frame_21)
        self.checkBoxQfilterFacture.setObjectName(u"checkBoxQfilterFacture")
        self.checkBoxQfilterFacture.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxQfilterFacture.setStyleSheet(u"")
        self.checkBoxQfilterFacture.setCheckable(True)
        self.checkBoxQfilterFacture.setChecked(True)
        self.checkBoxQfilterFacture.setTristate(False)

        self.gridLayout_9.addWidget(self.checkBoxQfilterFacture, 0, 6, 1, 2)

        self.line_9 = QFrame(self.frame_21)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(3, 0))
        self.line_9.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_9, 0, 5, 3, 1)

        self.label_61 = QLabel(self.frame_21)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(30, 16777215))
        self.label_61.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_61, 2, 6, 1, 1)

        self.dateDFFactureFilterT2 = QDateEdit(self.frame_21)
        self.dateDFFactureFilterT2.setObjectName(u"dateDFFactureFilterT2")
        self.dateDFFactureFilterT2.setEnabled(True)
        self.dateDFFactureFilterT2.setMinimumSize(QSize(0, 35))
        self.dateDFFactureFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDFFactureFilterT2.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDFFactureFilterT2.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_9.addWidget(self.dateDFFactureFilterT2, 2, 4, 1, 1)

        self.label_63 = QLabel(self.frame_21)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 20))
        self.label_63.setStyleSheet(u"")
        self.label_63.setScaledContents(False)

        self.gridLayout_9.addWidget(self.label_63, 0, 8, 1, 2)

        self.label_64 = QLabel(self.frame_21)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(20, 16777215))
        self.label_64.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_64, 2, 3, 1, 1)

        self.label_65 = QLabel(self.frame_21)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(30, 16777215))
        self.label_65.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_65, 1, 6, 1, 1)

        self.cboxUQFactureFilter = QComboBox(self.frame_21)
        self.cboxUQFactureFilter.addItem("")
        self.cboxUQFactureFilter.addItem("")
        self.cboxUQFactureFilter.addItem("")
        self.cboxUQFactureFilter.setObjectName(u"cboxUQFactureFilter")
        self.cboxUQFactureFilter.setEnabled(True)
        self.cboxUQFactureFilter.setMinimumSize(QSize(110, 35))
        self.cboxUQFactureFilter.setMaximumSize(QSize(110, 35))
        self.cboxUQFactureFilter.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.cboxUQFactureFilter, 1, 8, 1, 2)

        self.sboxQFactureFilterMin = QSpinBox(self.frame_21)
        self.sboxQFactureFilterMin.setObjectName(u"sboxQFactureFilterMin")
        self.sboxQFactureFilterMin.setEnabled(True)
        self.sboxQFactureFilterMin.setMinimumSize(QSize(0, 35))
        self.sboxQFactureFilterMin.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQFactureFilterMin.setMinimum(0)
        self.sboxQFactureFilterMin.setMaximum(999999999)

        self.gridLayout_9.addWidget(self.sboxQFactureFilterMin, 1, 7, 1, 1)

        self.sboxQFactureFilterMax = QSpinBox(self.frame_21)
        self.sboxQFactureFilterMax.setObjectName(u"sboxQFactureFilterMax")
        self.sboxQFactureFilterMax.setEnabled(True)
        self.sboxQFactureFilterMax.setMinimumSize(QSize(0, 35))
        self.sboxQFactureFilterMax.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQFactureFilterMax.setMinimum(0)
        self.sboxQFactureFilterMax.setMaximum(999999999)

        self.gridLayout_9.addWidget(self.sboxQFactureFilterMax, 2, 7, 1, 1)

        self.cboxCalcFacture = QComboBox(self.frame_21)
        self.cboxCalcFacture.addItem("")
        self.cboxCalcFacture.setObjectName(u"cboxCalcFacture")
        self.cboxCalcFacture.setEnabled(True)
        self.cboxCalcFacture.setMinimumSize(QSize(0, 35))
        self.cboxCalcFacture.setMaximumSize(QSize(215, 35))
        self.cboxCalcFacture.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.cboxCalcFacture, 1, 0, 1, 2)

        self.btnCalcFacture = QPushButton(self.frame_21)
        self.btnCalcFacture.setObjectName(u"btnCalcFacture")
        self.btnCalcFacture.setMinimumSize(QSize(0, 35))
        self.btnCalcFacture.setMaximumSize(QSize(215, 35))
        self.btnCalcFacture.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.btnCalcFacture, 2, 0, 1, 2)

        self.label_67 = QLabel(self.frame_21)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(16777215, 20))
        self.label_67.setStyleSheet(u"")
        self.label_67.setScaledContents(False)

        self.gridLayout_9.addWidget(self.label_67, 0, 0, 1, 2)


        self.verticalLayout_34.addLayout(self.gridLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_4)


        self.verticalLayout_33.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QSize(0, 0))
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_22)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 9, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setSpacing(9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(14, 0, 14, 5)
        self.label_68 = QLabel(self.frame_23)
        self.label_68.setObjectName(u"label_68")
        sizePolicy2.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy2)
        self.label_68.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_15.addWidget(self.label_68, 0, Qt.AlignLeft)

        self.label_95 = QLabel(self.frame_23)
        self.label_95.setObjectName(u"label_95")
        sizePolicy1.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy1)
        self.label_95.setMinimumSize(QSize(100, 0))
        self.label_95.setMaximumSize(QSize(100, 16777215))
        self.label_95.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_95.setWordWrap(False)

        self.horizontalLayout_15.addWidget(self.label_95, 0, Qt.AlignLeft)

        self.sboxFactureFetchRows = QSpinBox(self.frame_23)
        self.sboxFactureFetchRows.setObjectName(u"sboxFactureFetchRows")
        self.sboxFactureFetchRows.setEnabled(True)
        self.sboxFactureFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxFactureFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxFactureFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxFactureFetchRows.setMinimum(0)
        self.sboxFactureFetchRows.setMaximum(999999999)
        self.sboxFactureFetchRows.setValue(10)

        self.horizontalLayout_15.addWidget(self.sboxFactureFetchRows)

        self.label_96 = QLabel(self.frame_23)
        self.label_96.setObjectName(u"label_96")
        sizePolicy1.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy1)
        self.label_96.setMinimumSize(QSize(50, 0))
        self.label_96.setMaximumSize(QSize(16777215, 16777215))
        self.label_96.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_96.setWordWrap(False)

        self.horizontalLayout_15.addWidget(self.label_96)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)

        self.checkBoxViewTypeFacture = QCheckBox(self.frame_23)
        self.checkBoxViewTypeFacture.setObjectName(u"checkBoxViewTypeFacture")
        self.checkBoxViewTypeFacture.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxViewTypeFacture.setStyleSheet(u"")
        self.checkBoxViewTypeFacture.setCheckable(True)
        self.checkBoxViewTypeFacture.setChecked(False)
        self.checkBoxViewTypeFacture.setTristate(False)

        self.horizontalLayout_15.addWidget(self.checkBoxViewTypeFacture)

        self.label_69 = QLabel(self.frame_23)
        self.label_69.setObjectName(u"label_69")
        sizePolicy1.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy1)
        self.label_69.setMinimumSize(QSize(68, 0))
        self.label_69.setMaximumSize(QSize(20, 16777215))
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_69)

        self.vBoxShowColsFacture = QVBoxLayout()
        self.vBoxShowColsFacture.setObjectName(u"vBoxShowColsFacture")

        self.horizontalLayout_15.addLayout(self.vBoxShowColsFacture)

        self.refreshFacture = QPushButton(self.frame_23)
        self.refreshFacture.setObjectName(u"refreshFacture")
        self.refreshFacture.setMinimumSize(QSize(20, 20))
        self.refreshFacture.setMaximumSize(QSize(20, 20))
        self.refreshFacture.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshFacture.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.refreshFacture)


        self.verticalLayout_35.addWidget(self.frame_23)

        self.tableViewFacture = QTableView(self.frame_22)
        self.tableViewFacture.setObjectName(u"tableViewFacture")
        self.tableViewFacture.setStyleSheet(u"")
        self.tableViewFacture.setFrameShape(QFrame.NoFrame)
        self.tableViewFacture.setFrameShadow(QFrame.Plain)
        self.tableViewFacture.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewFacture.setTabKeyNavigation(True)
        self.tableViewFacture.setProperty("showDropIndicator", False)
        self.tableViewFacture.setDragDropOverwriteMode(False)
        self.tableViewFacture.setAlternatingRowColors(False)
        self.tableViewFacture.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewFacture.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewFacture.setTextElideMode(Qt.ElideNone)
        self.tableViewFacture.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewFacture.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewFacture.setShowGrid(False)
        self.tableViewFacture.setSortingEnabled(True)
        self.tableViewFacture.setWordWrap(False)
        self.tableViewFacture.setCornerButtonEnabled(False)
        self.tableViewFacture.horizontalHeader().setHighlightSections(False)
        self.tableViewFacture.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewFacture.horizontalHeader().setStretchLastSection(True)
        self.tableViewFacture.verticalHeader().setVisible(False)
        self.tableViewFacture.verticalHeader().setHighlightSections(False)

        self.verticalLayout_35.addWidget(self.tableViewFacture)


        self.verticalLayout_33.addWidget(self.frame_22)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_36.addWidget(self.scrollArea_6)

        self.stackedWidget.addWidget(self.pageFacture)
        self.pageMS = QWidget()
        self.pageMS.setObjectName(u"pageMS")
        self.verticalLayout_46 = QVBoxLayout(self.pageMS)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_8 = QScrollArea(self.pageMS)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setStyleSheet(u"")
        self.scrollArea_8.setFrameShape(QFrame.NoFrame)
        self.scrollArea_8.setFrameShadow(QFrame.Plain)
        self.scrollArea_8.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 636, 303))
        self.verticalLayout_44 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, 15, -1, -1)
        self.frame_32 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setMaximumSize(QSize(16777215, 190))
        self.frame_32.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_32.setFrameShadow(QFrame.Plain)
        self.verticalLayout_47 = QVBoxLayout(self.frame_32)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.editFilterMS = QLineEdit(self.frame_32)
        self.editFilterMS.setObjectName(u"editFilterMS")
        self.editFilterMS.setMinimumSize(QSize(300, 35))
        self.editFilterMS.setMaximumSize(QSize(300, 16777215))
        self.editFilterMS.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_23.addWidget(self.editFilterMS)

        self.cboxFilterMS = QComboBox(self.frame_32)
        self.cboxFilterMS.setObjectName(u"cboxFilterMS")
        self.cboxFilterMS.setMinimumSize(QSize(170, 35))
        self.cboxFilterMS.setMaximumSize(QSize(170, 35))
        self.cboxFilterMS.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_23.addWidget(self.cboxFilterMS)

        self.btnRechMs = QPushButton(self.frame_32)
        self.btnRechMs.setObjectName(u"btnRechMs")
        self.btnRechMs.setMinimumSize(QSize(110, 35))
        self.btnRechMs.setMaximumSize(QSize(110, 35))
        self.btnRechMs.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.btnRechMs)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_9)


        self.verticalLayout_47.addLayout(self.horizontalLayout_23)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(9)
        self.gridLayout_14.setVerticalSpacing(10)
        self.gridLayout_14.setContentsMargins(-1, 5, -1, -1)
        self.dateDMsFilterT2 = QDateEdit(self.frame_32)
        self.dateDMsFilterT2.setObjectName(u"dateDMsFilterT2")
        self.dateDMsFilterT2.setEnabled(True)
        self.dateDMsFilterT2.setMinimumSize(QSize(150, 35))
        self.dateDMsFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDMsFilterT2.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDMsFilterT2.setDateTime(QDateTime(QDate(2022, 12, 1), QTime(0, 0, 0)))

        self.gridLayout_14.addWidget(self.dateDMsFilterT2, 3, 3, 1, 1, Qt.AlignLeft)

        self.checkBoxDfilterMs = QCheckBox(self.frame_32)
        self.checkBoxDfilterMs.setObjectName(u"checkBoxDfilterMs")
        self.checkBoxDfilterMs.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDfilterMs.setStyleSheet(u"")
        self.checkBoxDfilterMs.setCheckable(True)
        self.checkBoxDfilterMs.setChecked(True)
        self.checkBoxDfilterMs.setTristate(False)

        self.gridLayout_14.addWidget(self.checkBoxDfilterMs, 0, 2, 2, 2)

        self.line_17 = QFrame(self.frame_32)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setMinimumSize(QSize(3, 0))
        self.line_17.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line_17, 0, 1, 4, 1)

        self.label_113 = QLabel(self.frame_32)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(20, 0))
        self.label_113.setMaximumSize(QSize(20, 16777215))
        self.label_113.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_113, 3, 2, 1, 1)

        self.dateDMsFilterT1 = QDateEdit(self.frame_32)
        self.dateDMsFilterT1.setObjectName(u"dateDMsFilterT1")
        self.dateDMsFilterT1.setEnabled(True)
        self.dateDMsFilterT1.setMinimumSize(QSize(150, 35))
        self.dateDMsFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDMsFilterT1.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDMsFilterT1.setDateTime(QDateTime(QDate(2022, 12, 2), QTime(0, 0, 0)))

        self.gridLayout_14.addWidget(self.dateDMsFilterT1, 2, 3, 1, 1, Qt.AlignLeft)

        self.label_112 = QLabel(self.frame_32)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(20, 0))
        self.label_112.setMaximumSize(QSize(20, 16777215))
        self.label_112.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_112, 2, 2, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_14)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_6)


        self.verticalLayout_44.addWidget(self.frame_32)

        self.frame_30 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_30)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 9, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_19.setSpacing(9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(14, 0, 14, 5)
        self.label_86 = QLabel(self.frame_31)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_19.addWidget(self.label_86, 0, Qt.AlignLeft)

        self.label_99 = QLabel(self.frame_31)
        self.label_99.setObjectName(u"label_99")
        sizePolicy1.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy1)
        self.label_99.setMinimumSize(QSize(100, 0))
        self.label_99.setMaximumSize(QSize(100, 16777215))
        self.label_99.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_99.setWordWrap(False)

        self.horizontalLayout_19.addWidget(self.label_99, 0, Qt.AlignLeft)

        self.sboxMsFetchRows = QSpinBox(self.frame_31)
        self.sboxMsFetchRows.setObjectName(u"sboxMsFetchRows")
        self.sboxMsFetchRows.setEnabled(True)
        self.sboxMsFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxMsFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxMsFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxMsFetchRows.setMinimum(0)
        self.sboxMsFetchRows.setMaximum(999999999)
        self.sboxMsFetchRows.setValue(10)

        self.horizontalLayout_19.addWidget(self.sboxMsFetchRows)

        self.label_100 = QLabel(self.frame_31)
        self.label_100.setObjectName(u"label_100")
        sizePolicy1.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy1)
        self.label_100.setMinimumSize(QSize(50, 0))
        self.label_100.setMaximumSize(QSize(27, 16777215))
        self.label_100.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_100.setWordWrap(False)

        self.horizontalLayout_19.addWidget(self.label_100)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_12)

        self.refreshMs = QPushButton(self.frame_31)
        self.refreshMs.setObjectName(u"refreshMs")
        self.refreshMs.setMinimumSize(QSize(20, 20))
        self.refreshMs.setMaximumSize(QSize(20, 20))
        self.refreshMs.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshMs.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.refreshMs)


        self.verticalLayout_45.addWidget(self.frame_31)

        self.tableViewMS = QTableView(self.frame_30)
        self.tableViewMS.setObjectName(u"tableViewMS")
        self.tableViewMS.setStyleSheet(u"")
        self.tableViewMS.setFrameShape(QFrame.NoFrame)
        self.tableViewMS.setFrameShadow(QFrame.Plain)
        self.tableViewMS.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewMS.setTabKeyNavigation(True)
        self.tableViewMS.setProperty("showDropIndicator", False)
        self.tableViewMS.setDragDropOverwriteMode(False)
        self.tableViewMS.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewMS.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewMS.setTextElideMode(Qt.ElideNone)
        self.tableViewMS.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewMS.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewMS.setShowGrid(False)
        self.tableViewMS.setSortingEnabled(True)
        self.tableViewMS.setWordWrap(False)
        self.tableViewMS.setCornerButtonEnabled(False)
        self.tableViewMS.horizontalHeader().setHighlightSections(False)
        self.tableViewMS.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewMS.horizontalHeader().setStretchLastSection(True)
        self.tableViewMS.verticalHeader().setVisible(False)
        self.tableViewMS.verticalHeader().setHighlightSections(False)

        self.verticalLayout_45.addWidget(self.tableViewMS)


        self.verticalLayout_44.addWidget(self.frame_30)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_46.addWidget(self.scrollArea_8)

        self.stackedWidget.addWidget(self.pageMS)
        self.pageLiv = QWidget()
        self.pageLiv.setObjectName(u"pageLiv")
        self.verticalLayout_42 = QVBoxLayout(self.pageLiv)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.pageLiv)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u"")
        self.scrollArea_7.setFrameShape(QFrame.NoFrame)
        self.scrollArea_7.setFrameShadow(QFrame.Plain)
        self.scrollArea_7.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1051, 303))
        self.verticalLayout_39 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 15, -1, -1)
        self.frame_25 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 0))
        self.frame_25.setMaximumSize(QSize(16777215, 190))
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_25.setFrameShadow(QFrame.Plain)
        self.verticalLayout_40 = QVBoxLayout(self.frame_25)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.editFilterLiv = QLineEdit(self.frame_25)
        self.editFilterLiv.setObjectName(u"editFilterLiv")
        self.editFilterLiv.setMinimumSize(QSize(300, 35))
        self.editFilterLiv.setMaximumSize(QSize(300, 16777215))
        self.editFilterLiv.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_16.addWidget(self.editFilterLiv)

        self.cboxFilterLiv = QComboBox(self.frame_25)
        self.cboxFilterLiv.setObjectName(u"cboxFilterLiv")
        self.cboxFilterLiv.setMinimumSize(QSize(170, 35))
        self.cboxFilterLiv.setMaximumSize(QSize(170, 35))
        self.cboxFilterLiv.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.cboxFilterLiv)

        self.btnRechLiv = QPushButton(self.frame_25)
        self.btnRechLiv.setObjectName(u"btnRechLiv")
        self.btnRechLiv.setMinimumSize(QSize(110, 35))
        self.btnRechLiv.setMaximumSize(QSize(110, 35))
        self.btnRechLiv.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.btnRechLiv)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.btnPageLivInsert = QPushButton(self.frame_25)
        self.btnPageLivInsert.setObjectName(u"btnPageLivInsert")
        self.btnPageLivInsert.setMinimumSize(QSize(110, 35))
        self.btnPageLivInsert.setMaximumSize(QSize(110, 35))
        self.btnPageLivInsert.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.btnPageLivInsert)


        self.verticalLayout_40.addLayout(self.horizontalLayout_16)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(9)
        self.gridLayout_11.setVerticalSpacing(10)
        self.gridLayout_11.setContentsMargins(-1, 5, -1, -1)
        self.cboxUQRLivFilter = QComboBox(self.frame_25)
        self.cboxUQRLivFilter.addItem("")
        self.cboxUQRLivFilter.addItem("")
        self.cboxUQRLivFilter.addItem("")
        self.cboxUQRLivFilter.setObjectName(u"cboxUQRLivFilter")
        self.cboxUQRLivFilter.setEnabled(True)
        self.cboxUQRLivFilter.setMinimumSize(QSize(110, 35))
        self.cboxUQRLivFilter.setMaximumSize(QSize(110, 35))
        self.cboxUQRLivFilter.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.cboxUQRLivFilter, 2, 13, 1, 1)

        self.sboxQLivFilterMax = QSpinBox(self.frame_25)
        self.sboxQLivFilterMax.setObjectName(u"sboxQLivFilterMax")
        self.sboxQLivFilterMax.setEnabled(True)
        self.sboxQLivFilterMax.setMinimumSize(QSize(0, 35))
        self.sboxQLivFilterMax.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQLivFilterMax.setMinimum(0)
        self.sboxQLivFilterMax.setMaximum(999999999)

        self.gridLayout_11.addWidget(self.sboxQLivFilterMax, 3, 7, 1, 1)

        self.label_82 = QLabel(self.frame_25)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(16777215, 20))
        self.label_82.setStyleSheet(u"")
        self.label_82.setScaledContents(False)

        self.gridLayout_11.addWidget(self.label_82, 0, 13, 1, 1)

        self.label_76 = QLabel(self.frame_25)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 20))
        self.label_76.setStyleSheet(u"")
        self.label_76.setScaledContents(False)

        self.gridLayout_11.addWidget(self.label_76, 0, 8, 1, 1)

        self.btnCalcLiv = QPushButton(self.frame_25)
        self.btnCalcLiv.setObjectName(u"btnCalcLiv")
        self.btnCalcLiv.setMinimumSize(QSize(110, 35))
        self.btnCalcLiv.setMaximumSize(QSize(16777215, 35))
        self.btnCalcLiv.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.btnCalcLiv, 3, 0, 1, 2)

        self.cboxUQLivFilter = QComboBox(self.frame_25)
        self.cboxUQLivFilter.addItem("")
        self.cboxUQLivFilter.addItem("")
        self.cboxUQLivFilter.addItem("")
        self.cboxUQLivFilter.setObjectName(u"cboxUQLivFilter")
        self.cboxUQLivFilter.setEnabled(True)
        self.cboxUQLivFilter.setMinimumSize(QSize(110, 35))
        self.cboxUQLivFilter.setMaximumSize(QSize(110, 35))
        self.cboxUQLivFilter.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.cboxUQLivFilter, 2, 8, 1, 1)

        self.line_12 = QFrame(self.frame_25)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setMinimumSize(QSize(3, 0))
        self.line_12.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_12, 0, 9, 4, 1)

        self.line_11 = QFrame(self.frame_25)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(3, 0))
        self.line_11.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_11, 0, 5, 4, 1)

        self.dateDLLivFilterT1 = QDateEdit(self.frame_25)
        self.dateDLLivFilterT1.setObjectName(u"dateDLLivFilterT1")
        self.dateDLLivFilterT1.setEnabled(True)
        self.dateDLLivFilterT1.setMinimumSize(QSize(0, 35))
        self.dateDLLivFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDLLivFilterT1.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDLLivFilterT1.setDateTime(QDateTime(QDate(2022, 12, 2), QTime(0, 0, 0)))

        self.gridLayout_11.addWidget(self.dateDLLivFilterT1, 2, 4, 1, 1)

        self.checkBoxDLfilterLiv = QCheckBox(self.frame_25)
        self.checkBoxDLfilterLiv.setObjectName(u"checkBoxDLfilterLiv")
        self.checkBoxDLfilterLiv.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDLfilterLiv.setStyleSheet(u"")
        self.checkBoxDLfilterLiv.setCheckable(True)
        self.checkBoxDLfilterLiv.setChecked(True)
        self.checkBoxDLfilterLiv.setTristate(False)

        self.gridLayout_11.addWidget(self.checkBoxDLfilterLiv, 0, 3, 1, 2, Qt.AlignLeft|Qt.AlignTop)

        self.sboxQLivFilterMin = QSpinBox(self.frame_25)
        self.sboxQLivFilterMin.setObjectName(u"sboxQLivFilterMin")
        self.sboxQLivFilterMin.setEnabled(True)
        self.sboxQLivFilterMin.setMinimumSize(QSize(0, 35))
        self.sboxQLivFilterMin.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQLivFilterMin.setMinimum(0)
        self.sboxQLivFilterMin.setMaximum(999999999)

        self.gridLayout_11.addWidget(self.sboxQLivFilterMin, 2, 7, 1, 1)

        self.dateDLLivFilterT2 = QDateEdit(self.frame_25)
        self.dateDLLivFilterT2.setObjectName(u"dateDLLivFilterT2")
        self.dateDLLivFilterT2.setEnabled(True)
        self.dateDLLivFilterT2.setMinimumSize(QSize(0, 35))
        self.dateDLLivFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDLLivFilterT2.setStyleSheet(u"QWidget {background-color: transparent}")
        self.dateDLLivFilterT2.setDateTime(QDateTime(QDate(2022, 12, 2), QTime(0, 0, 0)))

        self.gridLayout_11.addWidget(self.dateDLLivFilterT2, 3, 4, 1, 1)

        self.line_10 = QFrame(self.frame_25)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(3, 0))
        self.line_10.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_10, 0, 2, 4, 1)

        self.label_74 = QLabel(self.frame_25)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(20, 16777215))
        self.label_74.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_74, 2, 3, 1, 1)

        self.cboxCalcLiv = QComboBox(self.frame_25)
        self.cboxCalcLiv.addItem("")
        self.cboxCalcLiv.setObjectName(u"cboxCalcLiv")
        self.cboxCalcLiv.setEnabled(True)
        self.cboxCalcLiv.setMinimumSize(QSize(130, 35))
        self.cboxCalcLiv.setMaximumSize(QSize(16777215, 35))
        self.cboxCalcLiv.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.cboxCalcLiv, 2, 0, 1, 2)

        self.sboxQRLivFilterMin = QSpinBox(self.frame_25)
        self.sboxQRLivFilterMin.setObjectName(u"sboxQRLivFilterMin")
        self.sboxQRLivFilterMin.setEnabled(True)
        self.sboxQRLivFilterMin.setMinimumSize(QSize(0, 35))
        self.sboxQRLivFilterMin.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQRLivFilterMin.setMinimum(0)
        self.sboxQRLivFilterMin.setMaximum(999999999)

        self.gridLayout_11.addWidget(self.sboxQRLivFilterMin, 2, 11, 1, 1)

        self.label_77 = QLabel(self.frame_25)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(20, 16777215))
        self.label_77.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_77, 3, 3, 1, 1)

        self.label_78 = QLabel(self.frame_25)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(30, 16777215))
        self.label_78.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_78, 2, 6, 1, 1)

        self.checkBoxQfilterLiv = QCheckBox(self.frame_25)
        self.checkBoxQfilterLiv.setObjectName(u"checkBoxQfilterLiv")
        self.checkBoxQfilterLiv.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxQfilterLiv.setStyleSheet(u"")
        self.checkBoxQfilterLiv.setCheckable(True)
        self.checkBoxQfilterLiv.setChecked(True)
        self.checkBoxQfilterLiv.setTristate(False)

        self.gridLayout_11.addWidget(self.checkBoxQfilterLiv, 0, 6, 1, 2)

        self.label_75 = QLabel(self.frame_25)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(30, 16777215))
        self.label_75.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_75, 3, 6, 1, 1)

        self.label_84 = QLabel(self.frame_25)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMaximumSize(QSize(30, 16777215))
        self.label_84.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_84, 2, 10, 1, 1)

        self.checkBoxQRfilterLiv = QCheckBox(self.frame_25)
        self.checkBoxQRfilterLiv.setObjectName(u"checkBoxQRfilterLiv")
        self.checkBoxQRfilterLiv.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxQRfilterLiv.setStyleSheet(u"")
        self.checkBoxQRfilterLiv.setCheckable(True)
        self.checkBoxQRfilterLiv.setChecked(True)
        self.checkBoxQRfilterLiv.setTristate(False)

        self.gridLayout_11.addWidget(self.checkBoxQRfilterLiv, 0, 10, 1, 2)

        self.label_85 = QLabel(self.frame_25)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(30, 16777215))
        self.label_85.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_85, 3, 10, 1, 1)

        self.sboxQRLivFilterMax = QSpinBox(self.frame_25)
        self.sboxQRLivFilterMax.setObjectName(u"sboxQRLivFilterMax")
        self.sboxQRLivFilterMax.setEnabled(True)
        self.sboxQRLivFilterMax.setMinimumSize(QSize(0, 35))
        self.sboxQRLivFilterMax.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQRLivFilterMax.setMinimum(0)
        self.sboxQRLivFilterMax.setMaximum(999999999)

        self.gridLayout_11.addWidget(self.sboxQRLivFilterMax, 3, 11, 1, 1)

        self.label_79 = QLabel(self.frame_25)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(16777215, 20))
        self.label_79.setStyleSheet(u"")
        self.label_79.setScaledContents(False)

        self.gridLayout_11.addWidget(self.label_79, 0, 0, 1, 2)


        self.verticalLayout_40.addLayout(self.gridLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_5)


        self.verticalLayout_39.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QSize(0, 0))
        self.frame_26.setMaximumSize(QSize(16777215, 16777215))
        self.frame_26.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_26)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 9, 0, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_17.setSpacing(9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(14, 0, 14, 5)
        self.label_80 = QLabel(self.frame_27)
        self.label_80.setObjectName(u"label_80")
        sizePolicy2.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy2)
        self.label_80.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_17.addWidget(self.label_80, 0, Qt.AlignLeft)

        self.label_101 = QLabel(self.frame_27)
        self.label_101.setObjectName(u"label_101")
        sizePolicy1.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy1)
        self.label_101.setMinimumSize(QSize(100, 0))
        self.label_101.setMaximumSize(QSize(100, 16777215))
        self.label_101.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_101.setWordWrap(False)

        self.horizontalLayout_17.addWidget(self.label_101, 0, Qt.AlignLeft)

        self.sboxLivFetchRows = QSpinBox(self.frame_27)
        self.sboxLivFetchRows.setObjectName(u"sboxLivFetchRows")
        self.sboxLivFetchRows.setEnabled(True)
        self.sboxLivFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxLivFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxLivFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxLivFetchRows.setMinimum(0)
        self.sboxLivFetchRows.setMaximum(999999999)
        self.sboxLivFetchRows.setValue(10)

        self.horizontalLayout_17.addWidget(self.sboxLivFetchRows, 0, Qt.AlignLeft)

        self.label_102 = QLabel(self.frame_27)
        self.label_102.setObjectName(u"label_102")
        sizePolicy1.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy1)
        self.label_102.setMinimumSize(QSize(40, 0))
        self.label_102.setMaximumSize(QSize(40, 16777215))
        self.label_102.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_102.setWordWrap(False)

        self.horizontalLayout_17.addWidget(self.label_102, 0, Qt.AlignLeft)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)

        self.checkBoxViewTypeLiv = QCheckBox(self.frame_27)
        self.checkBoxViewTypeLiv.setObjectName(u"checkBoxViewTypeLiv")
        self.checkBoxViewTypeLiv.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxViewTypeLiv.setStyleSheet(u"")
        self.checkBoxViewTypeLiv.setCheckable(True)
        self.checkBoxViewTypeLiv.setChecked(False)
        self.checkBoxViewTypeLiv.setTristate(False)

        self.horizontalLayout_17.addWidget(self.checkBoxViewTypeLiv)

        self.label_81 = QLabel(self.frame_27)
        self.label_81.setObjectName(u"label_81")
        sizePolicy1.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy1)
        self.label_81.setMinimumSize(QSize(68, 0))
        self.label_81.setMaximumSize(QSize(20, 16777215))
        self.label_81.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_81)

        self.vBoxShowColsLiv = QVBoxLayout()
        self.vBoxShowColsLiv.setObjectName(u"vBoxShowColsLiv")

        self.horizontalLayout_17.addLayout(self.vBoxShowColsLiv)

        self.refreshLiv = QPushButton(self.frame_27)
        self.refreshLiv.setObjectName(u"refreshLiv")
        self.refreshLiv.setMinimumSize(QSize(20, 20))
        self.refreshLiv.setMaximumSize(QSize(20, 20))
        self.refreshLiv.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshLiv.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.refreshLiv)


        self.verticalLayout_41.addWidget(self.frame_27)

        self.tableViewLiv = QTableView(self.frame_26)
        self.tableViewLiv.setObjectName(u"tableViewLiv")
        self.tableViewLiv.setStyleSheet(u"")
        self.tableViewLiv.setFrameShape(QFrame.NoFrame)
        self.tableViewLiv.setFrameShadow(QFrame.Plain)
        self.tableViewLiv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewLiv.setTabKeyNavigation(True)
        self.tableViewLiv.setProperty("showDropIndicator", False)
        self.tableViewLiv.setDragDropOverwriteMode(False)
        self.tableViewLiv.setAlternatingRowColors(False)
        self.tableViewLiv.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewLiv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewLiv.setTextElideMode(Qt.ElideNone)
        self.tableViewLiv.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewLiv.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewLiv.setShowGrid(False)
        self.tableViewLiv.setSortingEnabled(True)
        self.tableViewLiv.setWordWrap(False)
        self.tableViewLiv.setCornerButtonEnabled(False)
        self.tableViewLiv.horizontalHeader().setHighlightSections(False)
        self.tableViewLiv.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewLiv.horizontalHeader().setStretchLastSection(True)
        self.tableViewLiv.verticalHeader().setVisible(False)
        self.tableViewLiv.verticalHeader().setHighlightSections(False)

        self.verticalLayout_41.addWidget(self.tableViewLiv)


        self.verticalLayout_39.addWidget(self.frame_26)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_42.addWidget(self.scrollArea_7)

        self.stackedWidget.addWidget(self.pageLiv)
        self.pageInsertLiv = QWidget()
        self.pageInsertLiv.setObjectName(u"pageInsertLiv")
        self.verticalLayout_43 = QVBoxLayout(self.pageInsertLiv)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_28 = QFrame(self.pageInsertLiv)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy1.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy1)
        self.frame_28.setMinimumSize(QSize(700, 440))
        self.frame_28.setMaximumSize(QSize(700, 440))
        self.frame_28.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_28.setFrameShadow(QFrame.Plain)
        self.gridLayout_12 = QGridLayout(self.frame_28)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(6)
        self.gridLayout_12.setContentsMargins(-1, -1, -1, 9)
        self.tableWidgetLiv = QTableWidget(self.frame_28)
        if (self.tableWidgetLiv.columnCount() < 14):
            self.tableWidgetLiv.setColumnCount(14)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidgetLiv.setHorizontalHeaderItem(13, __qtablewidgetitem17)
        self.tableWidgetLiv.setObjectName(u"tableWidgetLiv")
        self.tableWidgetLiv.setStyleSheet(u"")
        self.tableWidgetLiv.setFrameShape(QFrame.NoFrame)
        self.tableWidgetLiv.setProperty("showDropIndicator", False)
        self.tableWidgetLiv.setDragDropOverwriteMode(False)
        self.tableWidgetLiv.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidgetLiv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetLiv.setTextElideMode(Qt.ElideNone)
        self.tableWidgetLiv.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetLiv.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetLiv.setGridStyle(Qt.NoPen)
        self.tableWidgetLiv.setSortingEnabled(True)
        self.tableWidgetLiv.setWordWrap(False)
        self.tableWidgetLiv.setCornerButtonEnabled(False)
        self.tableWidgetLiv.setRowCount(0)
        self.tableWidgetLiv.horizontalHeader().setVisible(True)
        self.tableWidgetLiv.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetLiv.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidgetLiv.horizontalHeader().setDefaultSectionSize(203)
        self.tableWidgetLiv.horizontalHeader().setHighlightSections(False)
        self.tableWidgetLiv.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidgetLiv.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetLiv.verticalHeader().setVisible(False)
        self.tableWidgetLiv.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetLiv.verticalHeader().setMinimumSectionSize(40)
        self.tableWidgetLiv.verticalHeader().setDefaultSectionSize(40)
        self.tableWidgetLiv.verticalHeader().setHighlightSections(False)

        self.gridLayout_12.addWidget(self.tableWidgetLiv, 15, 0, 3, 14)

        self.btnInsertLiv = QPushButton(self.frame_28)
        self.btnInsertLiv.setObjectName(u"btnInsertLiv")
        self.btnInsertLiv.setMinimumSize(QSize(100, 35))
        self.btnInsertLiv.setMaximumSize(QSize(100, 35))
        self.btnInsertLiv.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.btnInsertLiv, 3, 12, 1, 1)

        self.btnAddRowLiv = QPushButton(self.frame_28)
        self.btnAddRowLiv.setObjectName(u"btnAddRowLiv")
        self.btnAddRowLiv.setMinimumSize(QSize(35, 35))
        self.btnAddRowLiv.setMaximumSize(QSize(35, 35))
        self.btnAddRowLiv.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.btnAddRowLiv, 3, 10, 1, 1)

        self.btnUpdateLiv = QPushButton(self.frame_28)
        self.btnUpdateLiv.setObjectName(u"btnUpdateLiv")
        self.btnUpdateLiv.setMinimumSize(QSize(100, 35))
        self.btnUpdateLiv.setMaximumSize(QSize(100, 35))
        self.btnUpdateLiv.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.btnUpdateLiv, 3, 13, 1, 1)

        self.btnSubRowLiv = QPushButton(self.frame_28)
        self.btnSubRowLiv.setObjectName(u"btnSubRowLiv")
        self.btnSubRowLiv.setMinimumSize(QSize(35, 35))
        self.btnSubRowLiv.setMaximumSize(QSize(35, 35))
        self.btnSubRowLiv.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.btnSubRowLiv, 3, 11, 1, 1)

        self.editAddrLivInsert = QLineEdit(self.frame_28)
        self.editAddrLivInsert.setObjectName(u"editAddrLivInsert")
        self.editAddrLivInsert.setMinimumSize(QSize(229, 35))
        self.editAddrLivInsert.setMaximumSize(QSize(250, 35))
        self.editAddrLivInsert.setStyleSheet(u"")
        self.editAddrLivInsert.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.editAddrLivInsert, 3, 0, 1, 1)

        self.label_83 = QLabel(self.frame_28)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMaximumSize(QSize(16777215, 20))
        self.label_83.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_12.addWidget(self.label_83, 1, 0, 1, 3)

        self.labelInsertLiv = QLabel(self.frame_28)
        self.labelInsertLiv.setObjectName(u"labelInsertLiv")
        self.labelInsertLiv.setMaximumSize(QSize(16777215, 50))
        self.labelInsertLiv.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelInsertLiv.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.labelInsertLiv, 0, 0, 1, 14)

        self.cboxCodeCmdLivAdd = QComboBox(self.frame_28)
        self.cboxCodeCmdLivAdd.addItem("")
        self.cboxCodeCmdLivAdd.setObjectName(u"cboxCodeCmdLivAdd")
        sizePolicy.setHeightForWidth(self.cboxCodeCmdLivAdd.sizePolicy().hasHeightForWidth())
        self.cboxCodeCmdLivAdd.setSizePolicy(sizePolicy)
        self.cboxCodeCmdLivAdd.setMinimumSize(QSize(0, 35))
        self.cboxCodeCmdLivAdd.setMaximumSize(QSize(200, 35))
        self.cboxCodeCmdLivAdd.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")
        self.cboxCodeCmdLivAdd.setEditable(True)

        self.gridLayout_12.addWidget(self.cboxCodeCmdLivAdd, 3, 1, 1, 9)


        self.verticalLayout_43.addWidget(self.frame_28, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageInsertLiv)
        self.pageAnalyseChart = QWidget()
        self.pageAnalyseChart.setObjectName(u"pageAnalyseChart")
        self.horizontalLayout_2 = QHBoxLayout(self.pageAnalyseChart)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 12, -1, -1)
        self.frame_33 = QFrame(self.pageAnalyseChart)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setMinimumSize(QSize(346, 0))
        self.frame_33.setMaximumSize(QSize(300, 16777215))
        self.frame_33.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_33.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_49 = QVBoxLayout(self.frame_33)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_10 = QScrollArea(self.frame_33)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setFrameShape(QFrame.NoFrame)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 338, 501))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.btnAnaCountDisplay = QPushButton(self.scrollAreaWidgetContents_10)
        self.btnAnaCountDisplay.setObjectName(u"btnAnaCountDisplay")
        self.btnAnaCountDisplay.setMinimumSize(QSize(0, 35))
        self.btnAnaCountDisplay.setMaximumSize(QSize(320, 35))
        self.btnAnaCountDisplay.setStyleSheet(u"")

        self.gridLayout_15.addWidget(self.btnAnaCountDisplay, 10, 1, 1, 5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.labelInsertFacture_8 = QLabel(self.scrollAreaWidgetContents_10)
        self.labelInsertFacture_8.setObjectName(u"labelInsertFacture_8")
        sizePolicy1.setHeightForWidth(self.labelInsertFacture_8.sizePolicy().hasHeightForWidth())
        self.labelInsertFacture_8.setSizePolicy(sizePolicy1)
        self.labelInsertFacture_8.setMinimumSize(QSize(0, 0))
        self.labelInsertFacture_8.setMaximumSize(QSize(16777215, 35))
        self.labelInsertFacture_8.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.labelInsertFacture_8.setMidLineWidth(0)
        self.labelInsertFacture_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.labelInsertFacture_8)

        self.dateAnaLoadD1 = QDateEdit(self.scrollAreaWidgetContents_10)
        self.dateAnaLoadD1.setObjectName(u"dateAnaLoadD1")
        self.dateAnaLoadD1.setEnabled(True)
        self.dateAnaLoadD1.setMinimumSize(QSize(100, 35))
        self.dateAnaLoadD1.setMaximumSize(QSize(16777215, 35))
        self.dateAnaLoadD1.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateAnaLoadD1.setDateTime(QDateTime(QDate(2022, 12, 1), QTime(0, 0, 0)))

        self.horizontalLayout_18.addWidget(self.dateAnaLoadD1)

        self.labelInsertFacture_9 = QLabel(self.scrollAreaWidgetContents_10)
        self.labelInsertFacture_9.setObjectName(u"labelInsertFacture_9")
        sizePolicy1.setHeightForWidth(self.labelInsertFacture_9.sizePolicy().hasHeightForWidth())
        self.labelInsertFacture_9.setSizePolicy(sizePolicy1)
        self.labelInsertFacture_9.setMinimumSize(QSize(0, 0))
        self.labelInsertFacture_9.setMaximumSize(QSize(16777215, 35))
        self.labelInsertFacture_9.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.labelInsertFacture_9.setMidLineWidth(0)
        self.labelInsertFacture_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.labelInsertFacture_9)

        self.dateAnaLoadD2 = QDateEdit(self.scrollAreaWidgetContents_10)
        self.dateAnaLoadD2.setObjectName(u"dateAnaLoadD2")
        self.dateAnaLoadD2.setEnabled(True)
        self.dateAnaLoadD2.setMinimumSize(QSize(100, 35))
        self.dateAnaLoadD2.setMaximumSize(QSize(16777215, 35))
        self.dateAnaLoadD2.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateAnaLoadD2.setDateTime(QDateTime(QDate(2022, 12, 1), QTime(0, 0, 0)))

        self.horizontalLayout_18.addWidget(self.dateAnaLoadD2)

        self.btnAnaLoadDf = QPushButton(self.scrollAreaWidgetContents_10)
        self.btnAnaLoadDf.setObjectName(u"btnAnaLoadDf")
        self.btnAnaLoadDf.setMinimumSize(QSize(40, 40))
        self.btnAnaLoadDf.setMaximumSize(QSize(40, 40))
        self.btnAnaLoadDf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnaLoadDf.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	image: url(:/icons/bin/ui/icons/icons8-data-manipulation-language-100.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.btnAnaLoadDf)


        self.gridLayout_15.addLayout(self.horizontalLayout_18, 1, 1, 1, 5)

        self.labelInsertFacture_7 = QLabel(self.scrollAreaWidgetContents_10)
        self.labelInsertFacture_7.setObjectName(u"labelInsertFacture_7")
        sizePolicy1.setHeightForWidth(self.labelInsertFacture_7.sizePolicy().hasHeightForWidth())
        self.labelInsertFacture_7.setSizePolicy(sizePolicy1)
        self.labelInsertFacture_7.setMinimumSize(QSize(0, 0))
        self.labelInsertFacture_7.setMaximumSize(QSize(16777215, 35))
        self.labelInsertFacture_7.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.labelInsertFacture_7.setMidLineWidth(0)
        self.labelInsertFacture_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.labelInsertFacture_7, 0, 1, 1, 5)

        self.labelInsertFacture_6 = QLabel(self.scrollAreaWidgetContents_10)
        self.labelInsertFacture_6.setObjectName(u"labelInsertFacture_6")
        sizePolicy1.setHeightForWidth(self.labelInsertFacture_6.sizePolicy().hasHeightForWidth())
        self.labelInsertFacture_6.setSizePolicy(sizePolicy1)
        self.labelInsertFacture_6.setMinimumSize(QSize(0, 0))
        self.labelInsertFacture_6.setMaximumSize(QSize(16777215, 35))
        self.labelInsertFacture_6.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.labelInsertFacture_6.setMidLineWidth(0)
        self.labelInsertFacture_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.labelInsertFacture_6, 9, 1, 1, 2, Qt.AlignLeft)

        self.line_14 = QFrame(self.scrollAreaWidgetContents_10)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setMaximumSize(QSize(320, 16777215))
        self.line_14.setStyleSheet(u"background-color: rgb(6, 35, 100);")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setFrameShape(QFrame.HLine)

        self.gridLayout_15.addWidget(self.line_14, 11, 1, 1, 5)

        self.cboxAnaTS = QComboBox(self.scrollAreaWidgetContents_10)
        self.cboxAnaTS.addItem("")
        self.cboxAnaTS.addItem("")
        self.cboxAnaTS.setObjectName(u"cboxAnaTS")
        self.cboxAnaTS.setMinimumSize(QSize(0, 35))
        self.cboxAnaTS.setMaximumSize(QSize(320, 35))
        self.cboxAnaTS.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cboxAnaTS.setEditable(False)

        self.gridLayout_15.addWidget(self.cboxAnaTS, 13, 1, 1, 5)

        self.verticalSpacer_7 = QSpacerItem(229, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_7, 16, 1, 1, 5)

        self.editAnaCountValue = QLineEdit(self.scrollAreaWidgetContents_10)
        self.editAnaCountValue.setObjectName(u"editAnaCountValue")
        self.editAnaCountValue.setMinimumSize(QSize(0, 35))
        self.editAnaCountValue.setMaximumSize(QSize(320, 35))
        self.editAnaCountValue.setAutoFillBackground(False)
        self.editAnaCountValue.setClearButtonEnabled(False)

        self.gridLayout_15.addWidget(self.editAnaCountValue, 8, 1, 1, 5)

        self.line_15 = QFrame(self.scrollAreaWidgetContents_10)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setMaximumSize(QSize(319, 16777215))
        self.line_15.setStyleSheet(u"background-color: rgb(6, 35, 100);")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setFrameShape(QFrame.HLine)

        self.gridLayout_15.addWidget(self.line_15, 15, 1, 1, 5)

        self.btnAnaTSDisplay = QPushButton(self.scrollAreaWidgetContents_10)
        self.btnAnaTSDisplay.setObjectName(u"btnAnaTSDisplay")
        self.btnAnaTSDisplay.setMinimumSize(QSize(0, 35))
        self.btnAnaTSDisplay.setMaximumSize(QSize(320, 35))
        self.btnAnaTSDisplay.setStyleSheet(u"")

        self.gridLayout_15.addWidget(self.btnAnaTSDisplay, 14, 1, 1, 5)

        self.line_16 = QFrame(self.scrollAreaWidgetContents_10)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setMaximumSize(QSize(320, 16777215))
        self.line_16.setStyleSheet(u"background-color: rgb(6, 35, 100);")
        self.line_16.setFrameShadow(QFrame.Plain)
        self.line_16.setFrameShape(QFrame.HLine)

        self.gridLayout_15.addWidget(self.line_16, 2, 1, 1, 5)

        self.cboxAnaCountPerDate = QComboBox(self.scrollAreaWidgetContents_10)
        self.cboxAnaCountPerDate.addItem("")
        self.cboxAnaCountPerDate.addItem("")
        self.cboxAnaCountPerDate.addItem("")
        self.cboxAnaCountPerDate.addItem("")
        self.cboxAnaCountPerDate.setObjectName(u"cboxAnaCountPerDate")
        self.cboxAnaCountPerDate.setMinimumSize(QSize(0, 35))
        self.cboxAnaCountPerDate.setMaximumSize(QSize(284, 35))
        self.cboxAnaCountPerDate.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cboxAnaCountPerDate.setEditable(False)

        self.gridLayout_15.addWidget(self.cboxAnaCountPerDate, 7, 2, 1, 4)

        self.checkBoxAnaGroupe = QCheckBox(self.scrollAreaWidgetContents_10)
        self.checkBoxAnaGroupe.setObjectName(u"checkBoxAnaGroupe")
        self.checkBoxAnaGroupe.setMaximumSize(QSize(300, 16777215))
        self.checkBoxAnaGroupe.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxAnaGroupe.setStyleSheet(u"")
        self.checkBoxAnaGroupe.setCheckable(True)
        self.checkBoxAnaGroupe.setChecked(True)
        self.checkBoxAnaGroupe.setTristate(False)

        self.gridLayout_15.addWidget(self.checkBoxAnaGroupe, 5, 1, 1, 5)

        self.labelInsertFacture_5 = QLabel(self.scrollAreaWidgetContents_10)
        self.labelInsertFacture_5.setObjectName(u"labelInsertFacture_5")
        self.labelInsertFacture_5.setMaximumSize(QSize(320, 35))
        self.labelInsertFacture_5.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.labelInsertFacture_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.labelInsertFacture_5, 3, 1, 1, 5)

        self.cboxAnaCountChartType = QComboBox(self.scrollAreaWidgetContents_10)
        self.cboxAnaCountChartType.addItem("")
        self.cboxAnaCountChartType.addItem("")
        self.cboxAnaCountChartType.setObjectName(u"cboxAnaCountChartType")
        self.cboxAnaCountChartType.setMinimumSize(QSize(0, 35))
        self.cboxAnaCountChartType.setMaximumSize(QSize(80, 35))
        self.cboxAnaCountChartType.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cboxAnaCountChartType.setEditable(False)

        self.gridLayout_15.addWidget(self.cboxAnaCountChartType, 9, 3, 1, 1, Qt.AlignLeft)

        self.checkBoxAnaTS = QCheckBox(self.scrollAreaWidgetContents_10)
        self.checkBoxAnaTS.setObjectName(u"checkBoxAnaTS")
        self.checkBoxAnaTS.setMaximumSize(QSize(320, 16777215))
        self.checkBoxAnaTS.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxAnaTS.setStyleSheet(u"")
        self.checkBoxAnaTS.setCheckable(True)
        self.checkBoxAnaTS.setChecked(True)
        self.checkBoxAnaTS.setTristate(False)

        self.gridLayout_15.addWidget(self.checkBoxAnaTS, 12, 1, 1, 5)

        self.line_13 = QFrame(self.scrollAreaWidgetContents_10)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setMaximumSize(QSize(320, 16777215))
        self.line_13.setStyleSheet(u"background-color: rgb(6, 35, 100);")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setFrameShape(QFrame.HLine)

        self.gridLayout_15.addWidget(self.line_13, 4, 1, 1, 5)

        self.labelInsertFacture_4 = QLabel(self.scrollAreaWidgetContents_10)
        self.labelInsertFacture_4.setObjectName(u"labelInsertFacture_4")
        sizePolicy1.setHeightForWidth(self.labelInsertFacture_4.sizePolicy().hasHeightForWidth())
        self.labelInsertFacture_4.setSizePolicy(sizePolicy1)
        self.labelInsertFacture_4.setMaximumSize(QSize(30, 35))
        self.labelInsertFacture_4.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.labelInsertFacture_4.setMidLineWidth(0)
        self.labelInsertFacture_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.labelInsertFacture_4, 7, 1, 1, 1)

        self.cboxAnaCount = QComboBox(self.scrollAreaWidgetContents_10)
        self.cboxAnaCount.addItem("")
        self.cboxAnaCount.addItem("")
        self.cboxAnaCount.addItem("")
        self.cboxAnaCount.addItem("")
        self.cboxAnaCount.addItem("")
        self.cboxAnaCount.addItem("")
        self.cboxAnaCount.setObjectName(u"cboxAnaCount")
        self.cboxAnaCount.setMinimumSize(QSize(0, 35))
        self.cboxAnaCount.setMaximumSize(QSize(320, 35))
        self.cboxAnaCount.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cboxAnaCount.setEditable(False)

        self.gridLayout_15.addWidget(self.cboxAnaCount, 6, 1, 1, 5)

        self.cboxAnaCountFunc = QComboBox(self.scrollAreaWidgetContents_10)
        self.cboxAnaCountFunc.addItem("")
        self.cboxAnaCountFunc.addItem("")
        self.cboxAnaCountFunc.setObjectName(u"cboxAnaCountFunc")
        self.cboxAnaCountFunc.setMinimumSize(QSize(0, 35))
        self.cboxAnaCountFunc.setMaximumSize(QSize(80, 35))
        self.cboxAnaCountFunc.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cboxAnaCountFunc.setEditable(False)

        self.gridLayout_15.addWidget(self.cboxAnaCountFunc, 9, 4, 1, 1)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_49.addWidget(self.scrollArea_10)


        self.horizontalLayout_2.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.pageAnalyseChart)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setMaximumSize(QSize(16777215, 16777215))
        self.frame_34.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_34.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_51 = QVBoxLayout(self.frame_34)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(6, 0, 6, 6)
        self.labelchart = QLabel(self.frame_34)
        self.labelchart.setObjectName(u"labelchart")
        self.labelchart.setMaximumSize(QSize(16777215, 35))
        self.labelchart.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelchart.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.labelchart)

        self.line_3 = QFrame(self.frame_34)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(6, 35, 100);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_51.addWidget(self.line_3)

        self.chartArea = QVBoxLayout()
        self.chartArea.setSpacing(0)
        self.chartArea.setObjectName(u"chartArea")

        self.verticalLayout_51.addLayout(self.chartArea)


        self.horizontalLayout_2.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.pageAnalyseChart)
        self.pageReport = QWidget()
        self.pageReport.setObjectName(u"pageReport")
        self.verticalLayout_52 = QVBoxLayout(self.pageReport)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(9, 15, -1, -1)
        self.frame_29 = QFrame(self.pageReport)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_29.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(15, -1, 15, -1)
        self.label_71 = QLabel(self.frame_29)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(16777215, 20))
        self.label_71.setStyleSheet(u"font: 12pt \"Arial\";")

        self.horizontalLayout_20.addWidget(self.label_71)

        self.cboxRep = QComboBox(self.frame_29)
        self.cboxRep.addItem("")
        self.cboxRep.setObjectName(u"cboxRep")
        self.cboxRep.setMinimumSize(QSize(120, 35))
        self.cboxRep.setMaximumSize(QSize(120, 35))
        self.cboxRep.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.cboxRep)

        self.label_98 = QLabel(self.frame_29)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(16777215, 20))
        self.label_98.setStyleSheet(u"font: 12pt \"Arial\";")

        self.horizontalLayout_20.addWidget(self.label_98)

        self.editRep = QLineEdit(self.frame_29)
        self.editRep.setObjectName(u"editRep")
        self.editRep.setMinimumSize(QSize(130, 35))
        self.editRep.setMaximumSize(QSize(130, 35))
        self.editRep.setAutoFillBackground(False)
        self.editRep.setClearButtonEnabled(False)

        self.horizontalLayout_20.addWidget(self.editRep)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.btnPageRepPrev = QPushButton(self.frame_29)
        self.btnPageRepPrev.setObjectName(u"btnPageRepPrev")
        self.btnPageRepPrev.setMinimumSize(QSize(110, 35))
        self.btnPageRepPrev.setMaximumSize(QSize(110, 35))
        self.btnPageRepPrev.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.btnPageRepPrev)

        self.btnPageRepNav = QPushButton(self.frame_29)
        self.btnPageRepNav.setObjectName(u"btnPageRepNav")
        self.btnPageRepNav.setMinimumSize(QSize(217, 35))
        self.btnPageRepNav.setMaximumSize(QSize(217, 35))
        self.btnPageRepNav.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.btnPageRepNav)


        self.verticalLayout_52.addWidget(self.frame_29)

        self.frame_35 = QFrame(self.pageReport)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setMaximumSize(QSize(16777215, 16777215))
        self.frame_35.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_35)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 9, 0, 0)
        self.reportView = QWebEngineView(self.frame_35)
        self.reportView.setObjectName(u"reportView")
        self.reportView.setTabletTracking(False)
        self.reportView.setAutoFillBackground(False)
        self.reportView.setStyleSheet(u"")
        self.reportView.setZoomFactor(1.000000000000000)

        self.verticalLayout_50.addWidget(self.reportView)


        self.verticalLayout_52.addWidget(self.frame_35)

        self.stackedWidget.addWidget(self.pageReport)
        self.pageInsertFacture = QWidget()
        self.pageInsertFacture.setObjectName(u"pageInsertFacture")
        self.verticalLayout_37 = QVBoxLayout(self.pageInsertFacture)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_24 = QFrame(self.pageInsertFacture)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.frame_24.setMinimumSize(QSize(710, 440))
        self.frame_24.setMaximumSize(QSize(710, 440))
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_24.setFrameShadow(QFrame.Plain)
        self.gridLayout_10 = QGridLayout(self.frame_24)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(6)
        self.gridLayout_10.setContentsMargins(-1, -1, -1, 9)
        self.label_73 = QLabel(self.frame_24)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(16777215, 20))
        self.label_73.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_10.addWidget(self.label_73, 1, 5, 1, 1)

        self.btnSubRowFacture = QPushButton(self.frame_24)
        self.btnSubRowFacture.setObjectName(u"btnSubRowFacture")
        self.btnSubRowFacture.setMinimumSize(QSize(35, 35))
        self.btnSubRowFacture.setMaximumSize(QSize(35, 35))
        self.btnSubRowFacture.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.btnSubRowFacture, 6, 5, 1, 1)

        self.tableWidgetFacture = QTableWidget(self.frame_24)
        if (self.tableWidgetFacture.columnCount() < 7):
            self.tableWidgetFacture.setColumnCount(7)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidgetFacture.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidgetFacture.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidgetFacture.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidgetFacture.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidgetFacture.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidgetFacture.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidgetFacture.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        self.tableWidgetFacture.setObjectName(u"tableWidgetFacture")
        self.tableWidgetFacture.setFrameShape(QFrame.NoFrame)
        self.tableWidgetFacture.setProperty("showDropIndicator", False)
        self.tableWidgetFacture.setDragDropOverwriteMode(False)
        self.tableWidgetFacture.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidgetFacture.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetFacture.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetFacture.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetFacture.setGridStyle(Qt.NoPen)
        self.tableWidgetFacture.setSortingEnabled(True)
        self.tableWidgetFacture.setWordWrap(False)
        self.tableWidgetFacture.setCornerButtonEnabled(False)
        self.tableWidgetFacture.setRowCount(0)
        self.tableWidgetFacture.horizontalHeader().setVisible(True)
        self.tableWidgetFacture.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetFacture.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidgetFacture.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidgetFacture.horizontalHeader().setHighlightSections(False)
        self.tableWidgetFacture.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidgetFacture.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetFacture.verticalHeader().setVisible(False)
        self.tableWidgetFacture.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetFacture.verticalHeader().setMinimumSectionSize(40)
        self.tableWidgetFacture.verticalHeader().setDefaultSectionSize(40)
        self.tableWidgetFacture.verticalHeader().setHighlightSections(False)

        self.gridLayout_10.addWidget(self.tableWidgetFacture, 12, 0, 3, 17)

        self.label_70 = QLabel(self.frame_24)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(16777215, 20))
        self.label_70.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_10.addWidget(self.label_70, 1, 1, 1, 1)

        self.labelInsertFacture = QLabel(self.frame_24)
        self.labelInsertFacture.setObjectName(u"labelInsertFacture")
        self.labelInsertFacture.setMaximumSize(QSize(16777215, 50))
        self.labelInsertFacture.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelInsertFacture.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.labelInsertFacture, 0, 0, 1, 17)

        self.btnAddRowFacture = QPushButton(self.frame_24)
        self.btnAddRowFacture.setObjectName(u"btnAddRowFacture")
        self.btnAddRowFacture.setMinimumSize(QSize(35, 35))
        self.btnAddRowFacture.setMaximumSize(QSize(35, 35))
        self.btnAddRowFacture.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.btnAddRowFacture, 6, 4, 1, 1)

        self.cboxCodeLivFactureAdd = QComboBox(self.frame_24)
        self.cboxCodeLivFactureAdd.addItem("")
        self.cboxCodeLivFactureAdd.setObjectName(u"cboxCodeLivFactureAdd")
        sizePolicy.setHeightForWidth(self.cboxCodeLivFactureAdd.sizePolicy().hasHeightForWidth())
        self.cboxCodeLivFactureAdd.setSizePolicy(sizePolicy)
        self.cboxCodeLivFactureAdd.setMinimumSize(QSize(0, 35))
        self.cboxCodeLivFactureAdd.setMaximumSize(QSize(16777215, 35))
        self.cboxCodeLivFactureAdd.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")
        self.cboxCodeLivFactureAdd.setEditable(True)

        self.gridLayout_10.addWidget(self.cboxCodeLivFactureAdd, 6, 1, 1, 3)

        self.cBoxModePaiementFactureInsert = QComboBox(self.frame_24)
        self.cBoxModePaiementFactureInsert.addItem("")
        self.cBoxModePaiementFactureInsert.addItem("")
        self.cBoxModePaiementFactureInsert.addItem("")
        self.cBoxModePaiementFactureInsert.addItem("")
        self.cBoxModePaiementFactureInsert.addItem("")
        self.cBoxModePaiementFactureInsert.setObjectName(u"cBoxModePaiementFactureInsert")
        self.cBoxModePaiementFactureInsert.setMinimumSize(QSize(0, 35))
        self.cBoxModePaiementFactureInsert.setMaximumSize(QSize(16777215, 35))
        self.cBoxModePaiementFactureInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cBoxModePaiementFactureInsert.setEditable(False)

        self.gridLayout_10.addWidget(self.cBoxModePaiementFactureInsert, 5, 1, 1, 3)

        self.label_72 = QLabel(self.frame_24)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(16777215, 20))
        self.label_72.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_10.addWidget(self.label_72, 1, 6, 1, 1)

        self.btnInsertFacture = QPushButton(self.frame_24)
        self.btnInsertFacture.setObjectName(u"btnInsertFacture")
        self.btnInsertFacture.setMinimumSize(QSize(110, 35))
        self.btnInsertFacture.setMaximumSize(QSize(110, 35))
        self.btnInsertFacture.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.btnInsertFacture, 6, 6, 1, 1)

        self.btnUpdateFacture = QPushButton(self.frame_24)
        self.btnUpdateFacture.setObjectName(u"btnUpdateFacture")
        self.btnUpdateFacture.setMinimumSize(QSize(110, 35))
        self.btnUpdateFacture.setMaximumSize(QSize(110, 35))
        self.btnUpdateFacture.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.btnUpdateFacture, 6, 7, 1, 1)

        self.dateEchFactureInsert = QDateEdit(self.frame_24)
        self.dateEchFactureInsert.setObjectName(u"dateEchFactureInsert")
        self.dateEchFactureInsert.setEnabled(True)
        self.dateEchFactureInsert.setMinimumSize(QSize(0, 35))
        self.dateEchFactureInsert.setMaximumSize(QSize(16777215, 35))
        self.dateEchFactureInsert.setStyleSheet(u"")
        self.dateEchFactureInsert.setDateTime(QDateTime(QDate(2022, 12, 2), QTime(0, 0, 0)))

        self.gridLayout_10.addWidget(self.dateEchFactureInsert, 5, 6, 1, 2)

        self.spinBoxTvaFactureInsert = QDoubleSpinBox(self.frame_24)
        self.spinBoxTvaFactureInsert.setObjectName(u"spinBoxTvaFactureInsert")
        self.spinBoxTvaFactureInsert.setMinimumSize(QSize(90, 35))
        self.spinBoxTvaFactureInsert.setMaximumSize(QSize(16777215, 35))
        self.spinBoxTvaFactureInsert.setTabletTracking(False)
        self.spinBoxTvaFactureInsert.setStyleSheet(u"")
        self.spinBoxTvaFactureInsert.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxTvaFactureInsert.setAccelerated(True)
        self.spinBoxTvaFactureInsert.setDecimals(2)
        self.spinBoxTvaFactureInsert.setMinimum(0.000000000000000)
        self.spinBoxTvaFactureInsert.setMaximum(999.000000000000000)
        self.spinBoxTvaFactureInsert.setStepType(QAbstractSpinBox.DefaultStepType)
        self.spinBoxTvaFactureInsert.setValue(19.000000000000000)

        self.gridLayout_10.addWidget(self.spinBoxTvaFactureInsert, 5, 4, 1, 2)


        self.verticalLayout_37.addWidget(self.frame_24, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageInsertFacture)
        self.pageClient = QWidget()
        self.pageClient.setObjectName(u"pageClient")
        self.verticalLayout_24 = QVBoxLayout(self.pageClient)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.pageClient)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Plain)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 762, 173))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 15, -1, -1)
        self.frame_9 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(15, -1, 15, -1)
        self.editFilterClient = QLineEdit(self.frame_9)
        self.editFilterClient.setObjectName(u"editFilterClient")
        self.editFilterClient.setMinimumSize(QSize(300, 35))
        self.editFilterClient.setMaximumSize(QSize(300, 16777215))
        self.editFilterClient.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.editFilterClient)

        self.cboxFilterClient = QComboBox(self.frame_9)
        self.cboxFilterClient.setObjectName(u"cboxFilterClient")
        self.cboxFilterClient.setMinimumSize(QSize(170, 35))
        self.cboxFilterClient.setMaximumSize(QSize(170, 35))
        self.cboxFilterClient.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.cboxFilterClient)

        self.btnRechClient = QPushButton(self.frame_9)
        self.btnRechClient.setObjectName(u"btnRechClient")
        self.btnRechClient.setMinimumSize(QSize(110, 35))
        self.btnRechClient.setMaximumSize(QSize(110, 35))
        self.btnRechClient.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.btnRechClient)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.btnPageClientInsert = QPushButton(self.frame_9)
        self.btnPageClientInsert.setObjectName(u"btnPageClientInsert")
        self.btnPageClientInsert.setMinimumSize(QSize(110, 35))
        self.btnPageClientInsert.setMaximumSize(QSize(110, 35))
        self.btnPageClientInsert.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.btnPageClientInsert)


        self.verticalLayout_22.addWidget(self.frame_9)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_14)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 9, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(14, 0, 14, 5)
        self.label_28 = QLabel(self.frame_15)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_11.addWidget(self.label_28)

        self.label_103 = QLabel(self.frame_15)
        self.label_103.setObjectName(u"label_103")
        sizePolicy1.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy1)
        self.label_103.setMinimumSize(QSize(100, 0))
        self.label_103.setMaximumSize(QSize(100, 16777215))
        self.label_103.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_103.setWordWrap(False)

        self.horizontalLayout_11.addWidget(self.label_103)

        self.sboxClientFetchRows = QSpinBox(self.frame_15)
        self.sboxClientFetchRows.setObjectName(u"sboxClientFetchRows")
        self.sboxClientFetchRows.setEnabled(True)
        self.sboxClientFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxClientFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxClientFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxClientFetchRows.setMinimum(0)
        self.sboxClientFetchRows.setMaximum(999999999)
        self.sboxClientFetchRows.setValue(100)

        self.horizontalLayout_11.addWidget(self.sboxClientFetchRows)

        self.label_104 = QLabel(self.frame_15)
        self.label_104.setObjectName(u"label_104")
        sizePolicy1.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy1)
        self.label_104.setMinimumSize(QSize(50, 0))
        self.label_104.setMaximumSize(QSize(27, 16777215))
        self.label_104.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_104.setWordWrap(False)

        self.horizontalLayout_11.addWidget(self.label_104)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_18)

        self.refreshClient = QPushButton(self.frame_15)
        self.refreshClient.setObjectName(u"refreshClient")
        self.refreshClient.setMinimumSize(QSize(20, 20))
        self.refreshClient.setMaximumSize(QSize(20, 20))
        self.refreshClient.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshClient.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.refreshClient)


        self.verticalLayout_23.addWidget(self.frame_15)

        self.tableViewClient = QTableView(self.frame_14)
        self.tableViewClient.setObjectName(u"tableViewClient")
        self.tableViewClient.setStyleSheet(u"")
        self.tableViewClient.setFrameShape(QFrame.NoFrame)
        self.tableViewClient.setFrameShadow(QFrame.Plain)
        self.tableViewClient.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewClient.setTabKeyNavigation(True)
        self.tableViewClient.setProperty("showDropIndicator", False)
        self.tableViewClient.setDragDropOverwriteMode(False)
        self.tableViewClient.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewClient.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewClient.setTextElideMode(Qt.ElideNone)
        self.tableViewClient.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewClient.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewClient.setShowGrid(False)
        self.tableViewClient.setSortingEnabled(True)
        self.tableViewClient.setWordWrap(False)
        self.tableViewClient.setCornerButtonEnabled(False)
        self.tableViewClient.horizontalHeader().setHighlightSections(False)
        self.tableViewClient.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewClient.horizontalHeader().setStretchLastSection(True)
        self.tableViewClient.verticalHeader().setVisible(False)
        self.tableViewClient.verticalHeader().setHighlightSections(False)

        self.verticalLayout_23.addWidget(self.tableViewClient)


        self.verticalLayout_22.addWidget(self.frame_14)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_24.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.pageClient)
        self.pageInsertClient = QWidget()
        self.pageInsertClient.setObjectName(u"pageInsertClient")
        self.verticalLayout_25 = QVBoxLayout(self.pageInsertClient)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_16 = QFrame(self.pageInsertClient)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setMinimumSize(QSize(600, 350))
        self.frame_16.setMaximumSize(QSize(500, 350))
        self.frame_16.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.gridLayout_7 = QGridLayout(self.frame_16)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(17)
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 9)
        self.cBoxNomAdvClientInsert = QComboBox(self.frame_16)
        self.cBoxNomAdvClientInsert.setObjectName(u"cBoxNomAdvClientInsert")
        self.cBoxNomAdvClientInsert.setMinimumSize(QSize(200, 35))
        self.cBoxNomAdvClientInsert.setMaximumSize(QSize(200, 35))
        self.cBoxNomAdvClientInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cBoxNomAdvClientInsert.setEditable(True)

        self.gridLayout_7.addWidget(self.cBoxNomAdvClientInsert, 2, 0, 1, 1)

        self.labelInsertClient = QLabel(self.frame_16)
        self.labelInsertClient.setObjectName(u"labelInsertClient")
        self.labelInsertClient.setMaximumSize(QSize(16777215, 70))
        self.labelInsertClient.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelInsertClient.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.labelInsertClient, 0, 0, 1, 4)

        self.editNumTelClientInsert = QLineEdit(self.frame_16)
        self.editNumTelClientInsert.setObjectName(u"editNumTelClientInsert")
        self.editNumTelClientInsert.setMinimumSize(QSize(100, 35))
        self.editNumTelClientInsert.setMaximumSize(QSize(100, 35))
        self.editNumTelClientInsert.setStyleSheet(u"")
        self.editNumTelClientInsert.setClearButtonEnabled(False)

        self.gridLayout_7.addWidget(self.editNumTelClientInsert, 4, 1, 1, 1)

        self.btnInsertClient = QPushButton(self.frame_16)
        self.btnInsertClient.setObjectName(u"btnInsertClient")
        self.btnInsertClient.setMinimumSize(QSize(110, 35))
        self.btnInsertClient.setMaximumSize(QSize(110, 35))
        self.btnInsertClient.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.btnInsertClient, 5, 0, 1, 1)

        self.editEmailClientInsert = QLineEdit(self.frame_16)
        self.editEmailClientInsert.setObjectName(u"editEmailClientInsert")
        self.editEmailClientInsert.setMinimumSize(QSize(0, 35))
        self.editEmailClientInsert.setMaximumSize(QSize(16777215, 35))
        self.editEmailClientInsert.setStyleSheet(u"")
        self.editEmailClientInsert.setClearButtonEnabled(False)

        self.gridLayout_7.addWidget(self.editEmailClientInsert, 4, 0, 1, 1)

        self.label_50 = QLabel(self.frame_16)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 20))
        self.label_50.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_7.addWidget(self.label_50, 1, 0, 1, 1)

        self.label_51 = QLabel(self.frame_16)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 20))
        self.label_51.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_7.addWidget(self.label_51, 3, 0, 1, 1)

        self.label_35 = QLabel(self.frame_16)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 20))
        self.label_35.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_7.addWidget(self.label_35, 3, 1, 1, 1)

        self.btnUpdateClient = QPushButton(self.frame_16)
        self.btnUpdateClient.setObjectName(u"btnUpdateClient")
        self.btnUpdateClient.setMinimumSize(QSize(110, 35))
        self.btnUpdateClient.setMaximumSize(QSize(110, 35))
        self.btnUpdateClient.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.btnUpdateClient, 6, 0, 1, 1)

        self.pTEditDescClientInsert = QPlainTextEdit(self.frame_16)
        self.pTEditDescClientInsert.setObjectName(u"pTEditDescClientInsert")

        self.gridLayout_7.addWidget(self.pTEditDescClientInsert, 2, 2, 3, 2)

        self.label_52 = QLabel(self.frame_16)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 20))
        self.label_52.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_7.addWidget(self.label_52, 1, 2, 1, 1)

        self.label_34 = QLabel(self.frame_16)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_7.addWidget(self.label_34, 1, 1, 1, 1)

        self.spinBoxNumWilayaClientInsert = QSpinBox(self.frame_16)
        self.spinBoxNumWilayaClientInsert.setObjectName(u"spinBoxNumWilayaClientInsert")
        self.spinBoxNumWilayaClientInsert.setMinimumSize(QSize(100, 35))
        self.spinBoxNumWilayaClientInsert.setMaximumSize(QSize(100, 35))
        self.spinBoxNumWilayaClientInsert.setMinimum(1)
        self.spinBoxNumWilayaClientInsert.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBoxNumWilayaClientInsert, 2, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_16, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageInsertClient)
        self.pageInsertProduit = QWidget()
        self.pageInsertProduit.setObjectName(u"pageInsertProduit")
        self.verticalLayout_10 = QVBoxLayout(self.pageInsertProduit)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_5 = QFrame(self.pageInsertProduit)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(500, 350))
        self.frame_5.setMaximumSize(QSize(500, 350))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(17)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.spinBoxCPProduitInsert = QSpinBox(self.frame_5)
        self.spinBoxCPProduitInsert.setObjectName(u"spinBoxCPProduitInsert")
        self.spinBoxCPProduitInsert.setMinimumSize(QSize(150, 35))
        self.spinBoxCPProduitInsert.setMaximumSize(QSize(150, 35))
        self.spinBoxCPProduitInsert.setMinimum(1)
        self.spinBoxCPProduitInsert.setMaximum(99999)

        self.gridLayout_3.addWidget(self.spinBoxCPProduitInsert, 7, 0, 1, 1)

        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 20))
        self.label_30.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_30, 6, 1, 1, 2)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.cBoxTypeProduitInsert = QComboBox(self.frame_5)
        self.cBoxTypeProduitInsert.addItem("")
        self.cBoxTypeProduitInsert.addItem("")
        self.cBoxTypeProduitInsert.setObjectName(u"cBoxTypeProduitInsert")
        self.cBoxTypeProduitInsert.setMinimumSize(QSize(100, 35))
        self.cBoxTypeProduitInsert.setMaximumSize(QSize(100, 35))
        self.cBoxTypeProduitInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.cBoxTypeProduitInsert, 2, 3, 1, 1)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 20))
        self.label_21.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_21, 3, 3, 1, 1)

        self.editNomProduitInsert = QLineEdit(self.frame_5)
        self.editNomProduitInsert.setObjectName(u"editNomProduitInsert")
        self.editNomProduitInsert.setMinimumSize(QSize(150, 35))
        self.editNomProduitInsert.setMaximumSize(QSize(150, 35))
        self.editNomProduitInsert.setStyleSheet(u"")
        self.editNomProduitInsert.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.editNomProduitInsert, 2, 0, 1, 1)

        self.cBoxUPoidsProduitInsert = QComboBox(self.frame_5)
        self.cBoxUPoidsProduitInsert.addItem("")
        self.cBoxUPoidsProduitInsert.addItem("")
        self.cBoxUPoidsProduitInsert.setObjectName(u"cBoxUPoidsProduitInsert")
        self.cBoxUPoidsProduitInsert.setMinimumSize(QSize(57, 35))
        self.cBoxUPoidsProduitInsert.setMaximumSize(QSize(40, 35))
        self.cBoxUPoidsProduitInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.cBoxUPoidsProduitInsert, 5, 3, 1, 1)

        self.spinBoxPrixUProduitInsert = QDoubleSpinBox(self.frame_5)
        self.spinBoxPrixUProduitInsert.setObjectName(u"spinBoxPrixUProduitInsert")
        self.spinBoxPrixUProduitInsert.setMinimumSize(QSize(150, 35))
        self.spinBoxPrixUProduitInsert.setMaximumSize(QSize(150, 35))
        self.spinBoxPrixUProduitInsert.setStyleSheet(u"")
        self.spinBoxPrixUProduitInsert.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxPrixUProduitInsert.setAccelerated(True)
        self.spinBoxPrixUProduitInsert.setDecimals(4)
        self.spinBoxPrixUProduitInsert.setMaximum(10000000.000000000000000)

        self.gridLayout_3.addWidget(self.spinBoxPrixUProduitInsert, 5, 0, 1, 1)

        self.spinBoxCCProduitInsert = QSpinBox(self.frame_5)
        self.spinBoxCCProduitInsert.setObjectName(u"spinBoxCCProduitInsert")
        self.spinBoxCCProduitInsert.setMinimumSize(QSize(150, 35))
        self.spinBoxCCProduitInsert.setMaximumSize(QSize(150, 35))
        self.spinBoxCCProduitInsert.setMinimum(1)
        self.spinBoxCCProduitInsert.setMaximum(99999)

        self.gridLayout_3.addWidget(self.spinBoxCCProduitInsert, 7, 1, 1, 1)

        self.spinBoxPoidsUProduitInsert = QDoubleSpinBox(self.frame_5)
        self.spinBoxPoidsUProduitInsert.setObjectName(u"spinBoxPoidsUProduitInsert")
        self.spinBoxPoidsUProduitInsert.setMinimumSize(QSize(150, 35))
        self.spinBoxPoidsUProduitInsert.setMaximumSize(QSize(150, 35))
        self.spinBoxPoidsUProduitInsert.setTabletTracking(False)
        self.spinBoxPoidsUProduitInsert.setStyleSheet(u"")
        self.spinBoxPoidsUProduitInsert.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxPoidsUProduitInsert.setAccelerated(True)
        self.spinBoxPoidsUProduitInsert.setDecimals(3)
        self.spinBoxPoidsUProduitInsert.setMinimum(0.000000000000000)
        self.spinBoxPoidsUProduitInsert.setMaximum(999.000000000000000)
        self.spinBoxPoidsUProduitInsert.setStepType(QAbstractSpinBox.DefaultStepType)

        self.gridLayout_3.addWidget(self.spinBoxPoidsUProduitInsert, 5, 1, 1, 1)

        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(153, 20))
        self.label_29.setMaximumSize(QSize(153, 20))
        self.label_29.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_29, 6, 0, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_18, 1, 3, 1, 1)

        self.labelInsertProduit = QLabel(self.frame_5)
        self.labelInsertProduit.setObjectName(u"labelInsertProduit")
        self.labelInsertProduit.setMaximumSize(QSize(16777215, 70))
        self.labelInsertProduit.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelInsertProduit.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.labelInsertProduit, 0, 0, 1, 5)

        self.cboxMarqueProduitInsert = QComboBox(self.frame_5)
        self.cboxMarqueProduitInsert.setObjectName(u"cboxMarqueProduitInsert")
        self.cboxMarqueProduitInsert.setMinimumSize(QSize(150, 35))
        self.cboxMarqueProduitInsert.setMaximumSize(QSize(150, 35))
        self.cboxMarqueProduitInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.cboxMarqueProduitInsert, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 20))
        self.label_20.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_3.addWidget(self.label_20, 3, 1, 1, 1)

        self.btnUpdateProduit = QPushButton(self.frame_5)
        self.btnUpdateProduit.setObjectName(u"btnUpdateProduit")
        self.btnUpdateProduit.setMinimumSize(QSize(110, 35))
        self.btnUpdateProduit.setMaximumSize(QSize(110, 35))
        self.btnUpdateProduit.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.btnUpdateProduit, 7, 3, 1, 1)

        self.btnInsertProduit = QPushButton(self.frame_5)
        self.btnInsertProduit.setObjectName(u"btnInsertProduit")
        self.btnInsertProduit.setMinimumSize(QSize(110, 35))
        self.btnInsertProduit.setMaximumSize(QSize(110, 35))
        self.btnInsertProduit.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.btnInsertProduit, 6, 3, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageInsertProduit)
        self.pageStock = QWidget()
        self.pageStock.setObjectName(u"pageStock")
        self.verticalLayout_13 = QVBoxLayout(self.pageStock)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.pageStock)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 873, 458))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 15, -1, -1)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 170))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.editFilterStock = QLineEdit(self.frame_3)
        self.editFilterStock.setObjectName(u"editFilterStock")
        self.editFilterStock.setMinimumSize(QSize(300, 35))
        self.editFilterStock.setMaximumSize(QSize(300, 16777215))
        self.editFilterStock.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.editFilterStock)

        self.cboxFilterStock = QComboBox(self.frame_3)
        self.cboxFilterStock.setObjectName(u"cboxFilterStock")
        self.cboxFilterStock.setMinimumSize(QSize(170, 35))
        self.cboxFilterStock.setMaximumSize(QSize(170, 35))
        self.cboxFilterStock.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cboxFilterStock)

        self.btnRechStock = QPushButton(self.frame_3)
        self.btnRechStock.setObjectName(u"btnRechStock")
        self.btnRechStock.setMinimumSize(QSize(110, 35))
        self.btnRechStock.setMaximumSize(QSize(110, 35))
        self.btnRechStock.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btnRechStock)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnPageStockInsert = QPushButton(self.frame_3)
        self.btnPageStockInsert.setObjectName(u"btnPageStockInsert")
        self.btnPageStockInsert.setMinimumSize(QSize(110, 35))
        self.btnPageStockInsert.setMaximumSize(QSize(110, 35))
        self.btnPageStockInsert.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btnPageStockInsert)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setContentsMargins(-1, 5, -1, -1)
        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(3, 0))
        self.line.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 3, 1)

        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 20))
        self.label_31.setStyleSheet(u"")
        self.label_31.setScaledContents(False)

        self.gridLayout.addWidget(self.label_31, 0, 8, 1, 2)

        self.checkBoxDEfilterStock = QCheckBox(self.frame_3)
        self.checkBoxDEfilterStock.setObjectName(u"checkBoxDEfilterStock")
        self.checkBoxDEfilterStock.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDEfilterStock.setStyleSheet(u"")
        self.checkBoxDEfilterStock.setCheckable(True)
        self.checkBoxDEfilterStock.setChecked(True)
        self.checkBoxDEfilterStock.setTristate(False)

        self.gridLayout.addWidget(self.checkBoxDEfilterStock, 0, 3, 1, 2)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(20, 16777215))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.dateDEStockFilterT2 = QDateEdit(self.frame_3)
        self.dateDEStockFilterT2.setObjectName(u"dateDEStockFilterT2")
        self.dateDEStockFilterT2.setEnabled(True)
        self.dateDEStockFilterT2.setMinimumSize(QSize(0, 35))
        self.dateDEStockFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDEStockFilterT2.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDEStockFilterT2.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.dateDEStockFilterT2, 2, 4, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(20, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(30, 16777215))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 2, 6, 1, 1)

        self.dateDFStockFilterT2 = QDateEdit(self.frame_3)
        self.dateDFStockFilterT2.setObjectName(u"dateDFStockFilterT2")
        self.dateDFStockFilterT2.setEnabled(True)
        self.dateDFStockFilterT2.setMinimumSize(QSize(0, 35))
        self.dateDFStockFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDFStockFilterT2.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDFStockFilterT2.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.dateDFStockFilterT2, 2, 1, 1, 1)

        self.dateDFStockFilterT1 = QDateEdit(self.frame_3)
        self.dateDFStockFilterT1.setObjectName(u"dateDFStockFilterT1")
        self.dateDFStockFilterT1.setEnabled(True)
        self.dateDFStockFilterT1.setMinimumSize(QSize(0, 35))
        self.dateDFStockFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDFStockFilterT1.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDFStockFilterT1.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.dateDFStockFilterT1, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(20, 16777215))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.dateDEStockFilterT1 = QDateEdit(self.frame_3)
        self.dateDEStockFilterT1.setObjectName(u"dateDEStockFilterT1")
        self.dateDEStockFilterT1.setEnabled(True)
        self.dateDEStockFilterT1.setMinimumSize(QSize(0, 35))
        self.dateDEStockFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDEStockFilterT1.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDEStockFilterT1.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.dateDEStockFilterT1, 1, 4, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(20, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(3, 0))
        self.line_2.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 5, 3, 1)

        self.checkBoxDFfilterStock = QCheckBox(self.frame_3)
        self.checkBoxDFfilterStock.setObjectName(u"checkBoxDFfilterStock")
        self.checkBoxDFfilterStock.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDFfilterStock.setStyleSheet(u"")
        self.checkBoxDFfilterStock.setCheckable(True)
        self.checkBoxDFfilterStock.setChecked(True)
        self.checkBoxDFfilterStock.setTristate(False)

        self.gridLayout.addWidget(self.checkBoxDFfilterStock, 0, 0, 1, 2, Qt.AlignLeft|Qt.AlignTop)

        self.checkBoxQfilterStock = QCheckBox(self.frame_3)
        self.checkBoxQfilterStock.setObjectName(u"checkBoxQfilterStock")
        self.checkBoxQfilterStock.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxQfilterStock.setStyleSheet(u"")
        self.checkBoxQfilterStock.setCheckable(True)
        self.checkBoxQfilterStock.setChecked(True)
        self.checkBoxQfilterStock.setTristate(False)

        self.gridLayout.addWidget(self.checkBoxQfilterStock, 0, 6, 1, 2)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(30, 16777215))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 1, 6, 1, 1)

        self.cboxUQStockFilter = QComboBox(self.frame_3)
        self.cboxUQStockFilter.addItem("")
        self.cboxUQStockFilter.addItem("")
        self.cboxUQStockFilter.addItem("")
        self.cboxUQStockFilter.setObjectName(u"cboxUQStockFilter")
        self.cboxUQStockFilter.setEnabled(True)
        self.cboxUQStockFilter.setMinimumSize(QSize(110, 35))
        self.cboxUQStockFilter.setMaximumSize(QSize(110, 35))
        self.cboxUQStockFilter.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.cboxUQStockFilter, 1, 8, 1, 2)

        self.sboxQStockFilterMin = QSpinBox(self.frame_3)
        self.sboxQStockFilterMin.setObjectName(u"sboxQStockFilterMin")
        self.sboxQStockFilterMin.setEnabled(True)
        self.sboxQStockFilterMin.setMinimumSize(QSize(0, 35))
        self.sboxQStockFilterMin.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQStockFilterMin.setMinimum(0)
        self.sboxQStockFilterMin.setMaximum(999999999)

        self.gridLayout.addWidget(self.sboxQStockFilterMin, 1, 7, 1, 1)

        self.sboxQStockFilterMax = QSpinBox(self.frame_3)
        self.sboxQStockFilterMax.setObjectName(u"sboxQStockFilterMax")
        self.sboxQStockFilterMax.setEnabled(True)
        self.sboxQStockFilterMax.setMinimumSize(QSize(0, 35))
        self.sboxQStockFilterMax.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQStockFilterMax.setMinimum(0)
        self.sboxQStockFilterMax.setMaximum(999999999)

        self.gridLayout.addWidget(self.sboxQStockFilterMax, 2, 7, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 9, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(14, 0, 14, 5)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_6.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.label_87 = QLabel(self.frame_7)
        self.label_87.setObjectName(u"label_87")
        sizePolicy1.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy1)
        self.label_87.setMinimumSize(QSize(100, 0))
        self.label_87.setMaximumSize(QSize(100, 16777215))
        self.label_87.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_87.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_87)

        self.sboxStockFetchRows = QSpinBox(self.frame_7)
        self.sboxStockFetchRows.setObjectName(u"sboxStockFetchRows")
        self.sboxStockFetchRows.setEnabled(True)
        self.sboxStockFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxStockFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxStockFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxStockFetchRows.setMinimum(0)
        self.sboxStockFetchRows.setMaximum(999999999)
        self.sboxStockFetchRows.setValue(200)

        self.horizontalLayout_6.addWidget(self.sboxStockFetchRows)

        self.label_88 = QLabel(self.frame_7)
        self.label_88.setObjectName(u"label_88")
        sizePolicy1.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy1)
        self.label_88.setMinimumSize(QSize(50, 0))
        self.label_88.setMaximumSize(QSize(27, 16777215))
        self.label_88.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_88.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_88)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_17)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(68, 0))
        self.label_14.setMaximumSize(QSize(20, 16777215))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.vBoxShowColsStock = QVBoxLayout()
        self.vBoxShowColsStock.setObjectName(u"vBoxShowColsStock")

        self.horizontalLayout_6.addLayout(self.vBoxShowColsStock)

        self.refreshStock = QPushButton(self.frame_7)
        self.refreshStock.setObjectName(u"refreshStock")
        self.refreshStock.setMinimumSize(QSize(20, 20))
        self.refreshStock.setMaximumSize(QSize(20, 20))
        self.refreshStock.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshStock.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.refreshStock)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.tableViewStock = QTableView(self.frame_6)
        self.tableViewStock.setObjectName(u"tableViewStock")
        self.tableViewStock.setStyleSheet(u"")
        self.tableViewStock.setFrameShape(QFrame.NoFrame)
        self.tableViewStock.setFrameShadow(QFrame.Plain)
        self.tableViewStock.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewStock.setTabKeyNavigation(True)
        self.tableViewStock.setProperty("showDropIndicator", False)
        self.tableViewStock.setDragDropOverwriteMode(False)
        self.tableViewStock.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewStock.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewStock.setTextElideMode(Qt.ElideNone)
        self.tableViewStock.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewStock.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewStock.setShowGrid(False)
        self.tableViewStock.setSortingEnabled(True)
        self.tableViewStock.setWordWrap(False)
        self.tableViewStock.setCornerButtonEnabled(False)
        self.tableViewStock.horizontalHeader().setHighlightSections(False)
        self.tableViewStock.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewStock.horizontalHeader().setStretchLastSection(True)
        self.tableViewStock.verticalHeader().setVisible(False)
        self.tableViewStock.verticalHeader().setHighlightSections(False)

        self.verticalLayout_12.addWidget(self.tableViewStock)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_13.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.pageStock)
        self.pageInv = QWidget()
        self.pageInv.setObjectName(u"pageInv")
        self.verticalLayout_19 = QVBoxLayout(self.pageInv)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.pageInv)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 782, 290))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 15, -1, -1)
        self.frame_13 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 170))
        self.frame_13.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.verticalLayout_21 = QVBoxLayout(self.frame_13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.editFilterInv = QLineEdit(self.frame_13)
        self.editFilterInv.setObjectName(u"editFilterInv")
        self.editFilterInv.setMinimumSize(QSize(300, 35))
        self.editFilterInv.setMaximumSize(QSize(300, 16777215))
        self.editFilterInv.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(248, 250, 255);\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: None;\n"
"background-image: url(:/icons/bin/ui/icons/icon_search.svg);\n"
"padding-left: 30px;\n"
"padding-right: 10px;\n"
"background-repeat: none;\n"
"background-position: left center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.editFilterInv)

        self.cboxFilterInv = QComboBox(self.frame_13)
        self.cboxFilterInv.setObjectName(u"cboxFilterInv")
        self.cboxFilterInv.setMinimumSize(QSize(170, 35))
        self.cboxFilterInv.setMaximumSize(QSize(170, 35))
        self.cboxFilterInv.setStyleSheet(u"QComboBox {\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.cboxFilterInv)

        self.btnRechInv = QPushButton(self.frame_13)
        self.btnRechInv.setObjectName(u"btnRechInv")
        self.btnRechInv.setMinimumSize(QSize(110, 35))
        self.btnRechInv.setMaximumSize(QSize(110, 35))
        self.btnRechInv.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.btnRechInv)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.btnPageInvInsert = QPushButton(self.frame_13)
        self.btnPageInvInsert.setObjectName(u"btnPageInvInsert")
        self.btnPageInvInsert.setMinimumSize(QSize(110, 35))
        self.btnPageInvInsert.setMaximumSize(QSize(110, 35))
        self.btnPageInvInsert.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.btnPageInvInsert)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(15)
        self.gridLayout_6.setContentsMargins(-1, 5, -1, -1)
        self.line_5 = QFrame(self.frame_13)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(3, 0))
        self.line_5.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_5, 0, 2, 3, 1)

        self.label_33 = QLabel(self.frame_13)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        self.label_33.setStyleSheet(u"")
        self.label_33.setScaledContents(False)

        self.gridLayout_6.addWidget(self.label_33, 0, 8, 1, 2)

        self.checkBoxDEfilterInv = QCheckBox(self.frame_13)
        self.checkBoxDEfilterInv.setObjectName(u"checkBoxDEfilterInv")
        self.checkBoxDEfilterInv.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDEfilterInv.setStyleSheet(u"")
        self.checkBoxDEfilterInv.setCheckable(True)
        self.checkBoxDEfilterInv.setChecked(True)
        self.checkBoxDEfilterInv.setTristate(False)

        self.gridLayout_6.addWidget(self.checkBoxDEfilterInv, 0, 3, 1, 2)

        self.label_40 = QLabel(self.frame_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(20, 16777215))
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_40, 2, 3, 1, 1)

        self.dateDEInvFilterT2 = QDateEdit(self.frame_13)
        self.dateDEInvFilterT2.setObjectName(u"dateDEInvFilterT2")
        self.dateDEInvFilterT2.setEnabled(True)
        self.dateDEInvFilterT2.setMinimumSize(QSize(0, 35))
        self.dateDEInvFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDEInvFilterT2.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDEInvFilterT2.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_6.addWidget(self.dateDEInvFilterT2, 2, 4, 1, 1)

        self.label_45 = QLabel(self.frame_13)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(20, 16777215))
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_45, 1, 0, 1, 1)

        self.label_46 = QLabel(self.frame_13)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(30, 16777215))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_46, 2, 6, 1, 1)

        self.dateDFInvFilterT2 = QDateEdit(self.frame_13)
        self.dateDFInvFilterT2.setObjectName(u"dateDFInvFilterT2")
        self.dateDFInvFilterT2.setEnabled(True)
        self.dateDFInvFilterT2.setMinimumSize(QSize(0, 35))
        self.dateDFInvFilterT2.setMaximumSize(QSize(16777215, 35))
        self.dateDFInvFilterT2.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDFInvFilterT2.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_6.addWidget(self.dateDFInvFilterT2, 2, 1, 1, 1)

        self.dateDFInvFilterT1 = QDateEdit(self.frame_13)
        self.dateDFInvFilterT1.setObjectName(u"dateDFInvFilterT1")
        self.dateDFInvFilterT1.setEnabled(True)
        self.dateDFInvFilterT1.setMinimumSize(QSize(0, 35))
        self.dateDFInvFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDFInvFilterT1.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDFInvFilterT1.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_6.addWidget(self.dateDFInvFilterT1, 1, 1, 1, 1)

        self.label_47 = QLabel(self.frame_13)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(20, 16777215))
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_47, 1, 3, 1, 1)

        self.dateDEInvFilterT1 = QDateEdit(self.frame_13)
        self.dateDEInvFilterT1.setObjectName(u"dateDEInvFilterT1")
        self.dateDEInvFilterT1.setEnabled(True)
        self.dateDEInvFilterT1.setMinimumSize(QSize(0, 35))
        self.dateDEInvFilterT1.setMaximumSize(QSize(16777215, 35))
        self.dateDEInvFilterT1.setStyleSheet(u"QWidget {background: transparent;}")
        self.dateDEInvFilterT1.setDateTime(QDateTime(QDate(2022, 12, 3), QTime(0, 0, 0)))

        self.gridLayout_6.addWidget(self.dateDEInvFilterT1, 1, 4, 1, 1)

        self.label_48 = QLabel(self.frame_13)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(20, 16777215))
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_48, 2, 0, 1, 1)

        self.line_6 = QFrame(self.frame_13)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(3, 0))
        self.line_6.setStyleSheet(u"background-color: rgb(6, 35, 100);\n"
"")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_6, 0, 5, 3, 1)

        self.checkBoxDFfilterInv = QCheckBox(self.frame_13)
        self.checkBoxDFfilterInv.setObjectName(u"checkBoxDFfilterInv")
        self.checkBoxDFfilterInv.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxDFfilterInv.setStyleSheet(u"")
        self.checkBoxDFfilterInv.setCheckable(True)
        self.checkBoxDFfilterInv.setChecked(True)
        self.checkBoxDFfilterInv.setTristate(False)

        self.gridLayout_6.addWidget(self.checkBoxDFfilterInv, 0, 0, 1, 2, Qt.AlignLeft|Qt.AlignTop)

        self.checkBoxQfilterInv = QCheckBox(self.frame_13)
        self.checkBoxQfilterInv.setObjectName(u"checkBoxQfilterInv")
        self.checkBoxQfilterInv.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBoxQfilterInv.setStyleSheet(u"")
        self.checkBoxQfilterInv.setCheckable(True)
        self.checkBoxQfilterInv.setChecked(True)
        self.checkBoxQfilterInv.setTristate(False)

        self.gridLayout_6.addWidget(self.checkBoxQfilterInv, 0, 6, 1, 2)

        self.label_49 = QLabel(self.frame_13)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(30, 16777215))
        self.label_49.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_49, 1, 6, 1, 1)

        self.cboxUQInvFilter = QComboBox(self.frame_13)
        self.cboxUQInvFilter.addItem("")
        self.cboxUQInvFilter.addItem("")
        self.cboxUQInvFilter.addItem("")
        self.cboxUQInvFilter.setObjectName(u"cboxUQInvFilter")
        self.cboxUQInvFilter.setEnabled(True)
        self.cboxUQInvFilter.setMinimumSize(QSize(110, 35))
        self.cboxUQInvFilter.setMaximumSize(QSize(110, 35))
        self.cboxUQInvFilter.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.cboxUQInvFilter, 1, 8, 1, 2)

        self.sboxQInvFilterMin = QSpinBox(self.frame_13)
        self.sboxQInvFilterMin.setObjectName(u"sboxQInvFilterMin")
        self.sboxQInvFilterMin.setEnabled(True)
        self.sboxQInvFilterMin.setMinimumSize(QSize(0, 35))
        self.sboxQInvFilterMin.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQInvFilterMin.setMinimum(0)
        self.sboxQInvFilterMin.setMaximum(999999999)

        self.gridLayout_6.addWidget(self.sboxQInvFilterMin, 1, 7, 1, 1)

        self.sboxQInvFilterMax = QSpinBox(self.frame_13)
        self.sboxQInvFilterMax.setObjectName(u"sboxQInvFilterMax")
        self.sboxQInvFilterMax.setEnabled(True)
        self.sboxQInvFilterMax.setMinimumSize(QSize(0, 35))
        self.sboxQInvFilterMax.setMaximumSize(QSize(16777215, 16777215))
        self.sboxQInvFilterMax.setMinimum(0)
        self.sboxQInvFilterMax.setMaximum(999999999)

        self.gridLayout_6.addWidget(self.sboxQInvFilterMax, 2, 7, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)


        self.verticalLayout_16.addWidget(self.frame_13)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_10)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 9, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(14, 0, 14, 5)
        self.label_36 = QLabel(self.frame_11)
        self.label_36.setObjectName(u"label_36")
        sizePolicy2.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy2)
        self.label_36.setStyleSheet(u"font: 700 18pt \"Arial\";")

        self.horizontalLayout_9.addWidget(self.label_36, 0, Qt.AlignLeft)

        self.label_89 = QLabel(self.frame_11)
        self.label_89.setObjectName(u"label_89")
        sizePolicy1.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy1)
        self.label_89.setMinimumSize(QSize(100, 0))
        self.label_89.setMaximumSize(QSize(100, 16777215))
        self.label_89.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_89.setWordWrap(False)

        self.horizontalLayout_9.addWidget(self.label_89, 0, Qt.AlignLeft)

        self.sboxInvFetchRows = QSpinBox(self.frame_11)
        self.sboxInvFetchRows.setObjectName(u"sboxInvFetchRows")
        self.sboxInvFetchRows.setEnabled(True)
        self.sboxInvFetchRows.setMinimumSize(QSize(50, 25))
        self.sboxInvFetchRows.setMaximumSize(QSize(70, 16777215))
        self.sboxInvFetchRows.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sboxInvFetchRows.setMinimum(0)
        self.sboxInvFetchRows.setMaximum(999999999)
        self.sboxInvFetchRows.setValue(10)

        self.horizontalLayout_9.addWidget(self.sboxInvFetchRows)

        self.label_90 = QLabel(self.frame_11)
        self.label_90.setObjectName(u"label_90")
        sizePolicy1.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy1)
        self.label_90.setMinimumSize(QSize(50, 0))
        self.label_90.setMaximumSize(QSize(27, 16777215))
        self.label_90.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_90.setWordWrap(False)

        self.horizontalLayout_9.addWidget(self.label_90, 0, Qt.AlignLeft)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.label_37 = QLabel(self.frame_11)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)
        self.label_37.setMinimumSize(QSize(68, 0))
        self.label_37.setMaximumSize(QSize(20, 16777215))
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_37)

        self.vBoxShowColsInv = QVBoxLayout()
        self.vBoxShowColsInv.setObjectName(u"vBoxShowColsInv")

        self.horizontalLayout_9.addLayout(self.vBoxShowColsInv)

        self.refreshInv = QPushButton(self.frame_11)
        self.refreshInv.setObjectName(u"refreshInv")
        self.refreshInv.setMinimumSize(QSize(20, 20))
        self.refreshInv.setMaximumSize(QSize(20, 20))
        self.refreshInv.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshInv.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	\n"
"	image: url(:/icons/bin/ui/icons/icons8-update-left-rotation-30.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid transparent;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.refreshInv)


        self.verticalLayout_18.addWidget(self.frame_11)

        self.tableViewInv = QTableView(self.frame_10)
        self.tableViewInv.setObjectName(u"tableViewInv")
        self.tableViewInv.setStyleSheet(u"")
        self.tableViewInv.setFrameShape(QFrame.NoFrame)
        self.tableViewInv.setFrameShadow(QFrame.Plain)
        self.tableViewInv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewInv.setTabKeyNavigation(True)
        self.tableViewInv.setProperty("showDropIndicator", False)
        self.tableViewInv.setDragDropOverwriteMode(False)
        self.tableViewInv.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewInv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewInv.setTextElideMode(Qt.ElideNone)
        self.tableViewInv.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewInv.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableViewInv.setShowGrid(False)
        self.tableViewInv.setSortingEnabled(True)
        self.tableViewInv.setWordWrap(False)
        self.tableViewInv.setCornerButtonEnabled(False)
        self.tableViewInv.horizontalHeader().setHighlightSections(False)
        self.tableViewInv.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableViewInv.horizontalHeader().setStretchLastSection(True)
        self.tableViewInv.verticalHeader().setVisible(False)
        self.tableViewInv.verticalHeader().setHighlightSections(False)

        self.verticalLayout_18.addWidget(self.tableViewInv)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_19.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.pageInv)
        self.pageInsertStock = QWidget()
        self.pageInsertStock.setObjectName(u"pageInsertStock")
        self.verticalLayout_14 = QVBoxLayout(self.pageInsertStock)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_8 = QFrame(self.pageInsertStock)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(600, 350))
        self.frame_8.setMaximumSize(QSize(600, 350))
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.spinBoxQuantitePStockInsert = QSpinBox(self.frame_8)
        self.spinBoxQuantitePStockInsert.setObjectName(u"spinBoxQuantitePStockInsert")
        self.spinBoxQuantitePStockInsert.setMinimumSize(QSize(0, 35))
        self.spinBoxQuantitePStockInsert.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxQuantitePStockInsert.setMinimum(0)
        self.spinBoxQuantitePStockInsert.setMaximum(999999999)

        self.gridLayout_4.addWidget(self.spinBoxQuantitePStockInsert, 7, 3, 1, 1)

        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 20))
        self.label_25.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_25, 1, 2, 1, 1)

        self.edtiLotStockInsert = QLineEdit(self.frame_8)
        self.edtiLotStockInsert.setObjectName(u"edtiLotStockInsert")
        self.edtiLotStockInsert.setMinimumSize(QSize(70, 35))
        self.edtiLotStockInsert.setMaximumSize(QSize(70, 35))
        self.edtiLotStockInsert.setStyleSheet(u"")
        self.edtiLotStockInsert.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.edtiLotStockInsert, 5, 3, 1, 1)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)

        self.dateDEStockInsert = QDateEdit(self.frame_8)
        self.dateDEStockInsert.setObjectName(u"dateDEStockInsert")
        self.dateDEStockInsert.setMinimumSize(QSize(0, 35))
        self.dateDEStockInsert.setMaximumSize(QSize(16777215, 35))
        self.dateDEStockInsert.setStyleSheet(u"QWidget {background: transparent;}")

        self.gridLayout_4.addWidget(self.dateDEStockInsert, 5, 2, 1, 1)

        self.spinBoxQuantiteUStockInsert = QSpinBox(self.frame_8)
        self.spinBoxQuantiteUStockInsert.setObjectName(u"spinBoxQuantiteUStockInsert")
        self.spinBoxQuantiteUStockInsert.setMinimumSize(QSize(0, 35))
        self.spinBoxQuantiteUStockInsert.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxQuantiteUStockInsert.setMinimum(0)
        self.spinBoxQuantiteUStockInsert.setMaximum(999999999)

        self.gridLayout_4.addWidget(self.spinBoxQuantiteUStockInsert, 7, 1, 1, 1)

        self.label_27 = QLabel(self.frame_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(130, 0))
        self.label_27.setMaximumSize(QSize(130, 20))
        self.label_27.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_27, 6, 1, 1, 1)

        self.btnUpdateStock = QPushButton(self.frame_8)
        self.btnUpdateStock.setObjectName(u"btnUpdateStock")
        self.btnUpdateStock.setMinimumSize(QSize(110, 35))
        self.btnUpdateStock.setMaximumSize(QSize(110, 35))
        self.btnUpdateStock.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.btnUpdateStock, 11, 3, 1, 1)

        self.labelInsertStock = QLabel(self.frame_8)
        self.labelInsertStock.setObjectName(u"labelInsertStock")
        self.labelInsertStock.setMaximumSize(QSize(16777215, 70))
        self.labelInsertStock.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelInsertStock.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.labelInsertStock, 0, 0, 1, 7)

        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 20))
        self.label_26.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_26, 1, 3, 1, 1)

        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(143, 0))
        self.label_23.setMaximumSize(QSize(143, 20))
        self.label_23.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_23, 6, 3, 1, 1)

        self.spinBoxQuantiteCStockInsert = QSpinBox(self.frame_8)
        self.spinBoxQuantiteCStockInsert.setObjectName(u"spinBoxQuantiteCStockInsert")
        self.spinBoxQuantiteCStockInsert.setMinimumSize(QSize(0, 35))
        self.spinBoxQuantiteCStockInsert.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxQuantiteCStockInsert.setMinimum(0)
        self.spinBoxQuantiteCStockInsert.setMaximum(999999999)

        self.gridLayout_4.addWidget(self.spinBoxQuantiteCStockInsert, 7, 2, 1, 1)

        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 20))
        self.label_24.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_24, 1, 1, 1, 1)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(140, 0))
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_12, 6, 0, 1, 1)

        self.dateDFStockInsert = QDateEdit(self.frame_8)
        self.dateDFStockInsert.setObjectName(u"dateDFStockInsert")
        self.dateDFStockInsert.setMinimumSize(QSize(0, 35))
        self.dateDFStockInsert.setMaximumSize(QSize(16777215, 35))
        self.dateDFStockInsert.setStyleSheet(u"QWidget {background: transparent;}")

        self.gridLayout_4.addWidget(self.dateDFStockInsert, 5, 1, 1, 1)

        self.cBoxCodeProduitStockInsert = QComboBox(self.frame_8)
        self.cBoxCodeProduitStockInsert.setObjectName(u"cBoxCodeProduitStockInsert")
        self.cBoxCodeProduitStockInsert.setMinimumSize(QSize(0, 35))
        self.cBoxCodeProduitStockInsert.setMaximumSize(QSize(16777215, 35))
        self.cBoxCodeProduitStockInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cBoxCodeProduitStockInsert.setEditable(True)

        self.gridLayout_4.addWidget(self.cBoxCodeProduitStockInsert, 5, 0, 1, 1)

        self.cboxCodeEmpStockInsert = QComboBox(self.frame_8)
        self.cboxCodeEmpStockInsert.setObjectName(u"cboxCodeEmpStockInsert")
        self.cboxCodeEmpStockInsert.setMinimumSize(QSize(120, 35))
        self.cboxCodeEmpStockInsert.setMaximumSize(QSize(150, 35))
        self.cboxCodeEmpStockInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.cboxCodeEmpStockInsert, 7, 0, 1, 1)

        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(144, 0))
        self.label_22.setMaximumSize(QSize(130, 20))
        self.label_22.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_4.addWidget(self.label_22, 6, 2, 1, 1)

        self.btnInsertStock = QPushButton(self.frame_8)
        self.btnInsertStock.setObjectName(u"btnInsertStock")
        self.btnInsertStock.setMinimumSize(QSize(110, 35))
        self.btnInsertStock.setMaximumSize(QSize(110, 35))
        self.btnInsertStock.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.btnInsertStock, 10, 3, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageInsertStock)
        self.pageInsertInv = QWidget()
        self.pageInsertInv.setObjectName(u"pageInsertInv")
        self.verticalLayout_20 = QVBoxLayout(self.pageInsertInv)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_12 = QFrame(self.pageInsertInv)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setMinimumSize(QSize(630, 350))
        self.frame_12.setMaximumSize(QSize(630, 350))
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_12.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_42 = QLabel(self.frame_12)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 20))
        self.label_42.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_42, 1, 3, 1, 1)

        self.cboxTypeInvInsert = QComboBox(self.frame_12)
        self.cboxTypeInvInsert.addItem("")
        self.cboxTypeInvInsert.addItem("")
        self.cboxTypeInvInsert.setObjectName(u"cboxTypeInvInsert")
        self.cboxTypeInvInsert.setMinimumSize(QSize(0, 0))
        self.cboxTypeInvInsert.setMaximumSize(QSize(16777215, 35))
        self.cboxTypeInvInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.cboxTypeInvInsert, 7, 4, 1, 3)

        self.label_44 = QLabel(self.frame_12)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(16777215, 20))
        self.label_44.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_44, 1, 4, 1, 1)

        self.label_41 = QLabel(self.frame_12)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(143, 0))
        self.label_41.setMaximumSize(QSize(143, 20))
        self.label_41.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_41, 6, 3, 1, 1)

        self.spinBoxQuantitePInvInsert = QSpinBox(self.frame_12)
        self.spinBoxQuantitePInvInsert.setObjectName(u"spinBoxQuantitePInvInsert")
        self.spinBoxQuantitePInvInsert.setMinimumSize(QSize(0, 35))
        self.spinBoxQuantitePInvInsert.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxQuantitePInvInsert.setMinimum(0)
        self.spinBoxQuantitePInvInsert.setMaximum(999999999)

        self.gridLayout_5.addWidget(self.spinBoxQuantitePInvInsert, 7, 3, 1, 1)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(140, 0))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_15, 1, 2, 1, 1)

        self.label_39 = QLabel(self.frame_12)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(130, 0))
        self.label_39.setMaximumSize(QSize(130, 20))
        self.label_39.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_39, 6, 0, 1, 1)

        self.dateDEInvInsert = QDateEdit(self.frame_12)
        self.dateDEInvInsert.setObjectName(u"dateDEInvInsert")
        self.dateDEInvInsert.setMinimumSize(QSize(0, 35))
        self.dateDEInvInsert.setMaximumSize(QSize(16777215, 35))
        self.dateDEInvInsert.setStyleSheet(u"QWidget {background: transparent;}")

        self.gridLayout_5.addWidget(self.dateDEInvInsert, 5, 4, 1, 3)

        self.label_97 = QLabel(self.frame_12)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(130, 0))
        self.label_97.setMaximumSize(QSize(130, 20))
        self.label_97.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_97, 8, 0, 1, 1)

        self.cboxCodeEmpInvInsert = QComboBox(self.frame_12)
        self.cboxCodeEmpInvInsert.setObjectName(u"cboxCodeEmpInvInsert")
        self.cboxCodeEmpInvInsert.setMinimumSize(QSize(120, 35))
        self.cboxCodeEmpInvInsert.setMaximumSize(QSize(150, 35))
        self.cboxCodeEmpInvInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.cboxCodeEmpInvInsert, 5, 2, 1, 1)

        self.spinBoxQuantiteUInvInsert = QSpinBox(self.frame_12)
        self.spinBoxQuantiteUInvInsert.setObjectName(u"spinBoxQuantiteUInvInsert")
        self.spinBoxQuantiteUInvInsert.setMinimumSize(QSize(0, 35))
        self.spinBoxQuantiteUInvInsert.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxQuantiteUInvInsert.setMinimum(0)
        self.spinBoxQuantiteUInvInsert.setMaximum(999999999)

        self.gridLayout_5.addWidget(self.spinBoxQuantiteUInvInsert, 7, 0, 1, 1)

        self.cBoxCodeProduitInvInsert = QComboBox(self.frame_12)
        self.cBoxCodeProduitInvInsert.setObjectName(u"cBoxCodeProduitInvInsert")
        self.cBoxCodeProduitInvInsert.setMinimumSize(QSize(0, 35))
        self.cBoxCodeProduitInvInsert.setMaximumSize(QSize(16777215, 35))
        self.cBoxCodeProduitInvInsert.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"")
        self.cBoxCodeProduitInvInsert.setEditable(True)

        self.gridLayout_5.addWidget(self.cBoxCodeProduitInvInsert, 5, 0, 1, 1)

        self.dateDFInvInsert = QDateEdit(self.frame_12)
        self.dateDFInvInsert.setObjectName(u"dateDFInvInsert")
        self.dateDFInvInsert.setMinimumSize(QSize(0, 35))
        self.dateDFInvInsert.setMaximumSize(QSize(16777215, 35))
        self.dateDFInvInsert.setStyleSheet(u"QWidget {background: transparent;}")

        self.gridLayout_5.addWidget(self.dateDFInvInsert, 5, 3, 1, 1)

        self.btnInsertInv = QPushButton(self.frame_12)
        self.btnInsertInv.setObjectName(u"btnInsertInv")
        self.btnInsertInv.setMinimumSize(QSize(110, 35))
        self.btnInsertInv.setMaximumSize(QSize(110, 35))
        self.btnInsertInv.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.btnInsertInv, 9, 3, 1, 1)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(140, 0))
        self.label_17.setMaximumSize(QSize(16777215, 20))
        self.label_17.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_17, 6, 4, 1, 1)

        self.label_38 = QLabel(self.frame_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 20))
        self.label_38.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_38, 1, 0, 1, 1)

        self.spinBoxQuantiteCInvInsert = QSpinBox(self.frame_12)
        self.spinBoxQuantiteCInvInsert.setObjectName(u"spinBoxQuantiteCInvInsert")
        self.spinBoxQuantiteCInvInsert.setMinimumSize(QSize(0, 35))
        self.spinBoxQuantiteCInvInsert.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxQuantiteCInvInsert.setMinimum(0)
        self.spinBoxQuantiteCInvInsert.setMaximum(999999999)

        self.gridLayout_5.addWidget(self.spinBoxQuantiteCInvInsert, 7, 2, 1, 1)

        self.labelInsertInv = QLabel(self.frame_12)
        self.labelInsertInv.setObjectName(u"labelInsertInv")
        self.labelInsertInv.setMaximumSize(QSize(16777215, 70))
        self.labelInsertInv.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.labelInsertInv.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelInsertInv, 0, 0, 1, 7)

        self.label_43 = QLabel(self.frame_12)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(144, 0))
        self.label_43.setMaximumSize(QSize(130, 20))
        self.label_43.setStyleSheet(u"font: 12pt \"Arial\";")

        self.gridLayout_5.addWidget(self.label_43, 6, 2, 1, 1)

        self.edtiLotInvInsert = QLineEdit(self.frame_12)
        self.edtiLotInvInsert.setObjectName(u"edtiLotInvInsert")
        self.edtiLotInvInsert.setMinimumSize(QSize(70, 35))
        self.edtiLotInvInsert.setMaximumSize(QSize(70, 35))
        self.edtiLotInvInsert.setStyleSheet(u"")
        self.edtiLotInvInsert.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.edtiLotInvInsert, 9, 0, 1, 1)

        self.btnUpdateInv = QPushButton(self.frame_12)
        self.btnUpdateInv.setObjectName(u"btnUpdateInv")
        self.btnUpdateInv.setMinimumSize(QSize(110, 35))
        self.btnUpdateInv.setMaximumSize(QSize(110, 35))
        self.btnUpdateInv.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.btnUpdateInv, 9, 4, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageInsertInv)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.midFrame)

        self.midFrame.raise_()
        self.topFrame.raise_()

        self.horizontalLayout.addWidget(self.mainFrame)


        self.verticalLayout.addWidget(self.styles)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.checkBoxQfilterStock.toggled.connect(self.label_13.setVisible)
        self.checkBoxDFfilterStock.toggled.connect(self.label_3.setVisible)
        self.checkBoxDEfilterInv.toggled.connect(self.dateDEInvFilterT1.setVisible)
        self.checkBoxDEfilterInv.toggled.connect(self.label_40.setVisible)
        self.checkBoxDFfilterInv.toggled.connect(self.label_45.setVisible)
        self.checkBoxDEfilterStock.toggled.connect(self.label_9.setVisible)
        self.checkBoxQfilterStock.toggled.connect(self.label_10.setVisible)
        self.checkBoxQfilterInv.toggled.connect(self.sboxQInvFilterMax.setVisible)
        self.checkBoxDFfilterStock.toggled.connect(self.label_2.setVisible)
        self.checkBoxDEfilterInv.toggled.connect(self.label_47.setVisible)
        self.checkBoxDEfilterInv.toggled.connect(self.dateDEInvFilterT2.setVisible)
        self.checkBoxQfilterStock.toggled.connect(self.sboxQStockFilterMin.setVisible)
        self.checkBoxQfilterStock.toggled.connect(self.sboxQStockFilterMax.setVisible)
        self.checkBoxDFfilterInv.toggled.connect(self.label_48.setVisible)
        self.checkBoxQfilterInv.toggled.connect(self.cboxUQInvFilter.setVisible)
        self.checkBoxQfilterInv.toggled.connect(self.label_46.setVisible)
        self.checkBoxQfilterInv.toggled.connect(self.label_49.setVisible)
        self.checkBoxDEfilterStock.toggled.connect(self.dateDEStockFilterT2.setVisible)
        self.checkBoxDEfilterStock.toggled.connect(self.dateDEStockFilterT1.setVisible)
        self.checkBoxDFfilterInv.toggled.connect(self.dateDFInvFilterT2.setVisible)
        self.checkBoxQfilterInv.toggled.connect(self.label_33.setVisible)
        self.checkBoxDFfilterInv.toggled.connect(self.dateDFInvFilterT1.setVisible)
        self.checkBoxQfilterStock.toggled.connect(self.cboxUQStockFilter.setVisible)
        self.checkBoxQfilterStock.toggled.connect(self.label_31.setVisible)
        self.checkBoxDFfilterStock.toggled.connect(self.dateDFStockFilterT2.setVisible)
        self.checkBoxDEfilterStock.toggled.connect(self.label_8.setVisible)
        self.checkBoxDFfilterStock.toggled.connect(self.dateDFStockFilterT1.setVisible)
        self.checkBoxQfilterInv.toggled.connect(self.sboxQInvFilterMin.setVisible)
        self.checkBoxQfilterCmd.toggled.connect(self.label_32.setVisible)
        self.checkBoxQfilterCmd.toggled.connect(self.cboxUQCmdFilter.setVisible)
        self.checkBoxQfilterCmd.toggled.connect(self.sboxQCmdFilterMin.setVisible)
        self.checkBoxQfilterCmd.toggled.connect(self.label_58.setVisible)
        self.checkBoxQfilterCmd.toggled.connect(self.label_55.setVisible)
        self.checkBoxQfilterCmd.toggled.connect(self.sboxQCmdFilterMax.setVisible)
        self.checkBoxDCfilterCmd.toggled.connect(self.dateDCCmdFilterT1.setVisible)
        self.checkBoxDCfilterCmd.toggled.connect(self.label_54.setVisible)
        self.checkBoxDCfilterCmd.toggled.connect(self.dateDCCmdFilterT2.setVisible)
        self.checkBoxDCfilterCmd.toggled.connect(self.label_57.setVisible)
        self.checkBoxDFfilterFacture.toggled.connect(self.dateDFFactureFilterT1.setVisible)
        self.checkBoxDFfilterFacture.toggled.connect(self.label_56.setVisible)
        self.checkBoxDFfilterFacture.toggled.connect(self.dateDFFactureFilterT2.setVisible)
        self.checkBoxDFfilterFacture.toggled.connect(self.label_64.setVisible)
        self.checkBoxQfilterFacture.toggled.connect(self.sboxQFactureFilterMin.setVisible)
        self.checkBoxQfilterFacture.toggled.connect(self.label_65.setVisible)
        self.checkBoxQfilterFacture.toggled.connect(self.label_61.setVisible)
        self.checkBoxQfilterFacture.toggled.connect(self.sboxQFactureFilterMax.setVisible)
        self.checkBoxQfilterFacture.toggled.connect(self.cboxUQFactureFilter.setVisible)
        self.checkBoxQfilterFacture.toggled.connect(self.label_63.setVisible)
        self.checkBoxDLfilterLiv.toggled.connect(self.dateDLLivFilterT1.setVisible)
        self.checkBoxDLfilterLiv.toggled.connect(self.dateDLLivFilterT2.setVisible)
        self.checkBoxDLfilterLiv.toggled.connect(self.label_74.setVisible)
        self.checkBoxDLfilterLiv.toggled.connect(self.label_77.setVisible)
        self.checkBoxQfilterLiv.toggled.connect(self.label_78.setVisible)
        self.checkBoxQfilterLiv.toggled.connect(self.label_75.setVisible)
        self.checkBoxQfilterLiv.toggled.connect(self.sboxQLivFilterMin.setVisible)
        self.checkBoxQfilterLiv.toggled.connect(self.sboxQLivFilterMax.setVisible)
        self.checkBoxQfilterLiv.toggled.connect(self.label_76.setVisible)
        self.checkBoxQfilterLiv.toggled.connect(self.cboxUQLivFilter.setVisible)
        self.checkBoxQRfilterLiv.toggled.connect(self.sboxQRLivFilterMin.setVisible)
        self.checkBoxQRfilterLiv.toggled.connect(self.label_84.setVisible)
        self.checkBoxQRfilterLiv.toggled.connect(self.label_85.setVisible)
        self.checkBoxQRfilterLiv.toggled.connect(self.sboxQRLivFilterMax.setVisible)
        self.checkBoxQRfilterLiv.toggled.connect(self.cboxUQRLivFilter.setVisible)
        self.checkBoxQRfilterLiv.toggled.connect(self.label_82.setVisible)
        self.checkBoxDfilterMs.toggled.connect(self.label_112.setVisible)
        self.checkBoxDfilterMs.toggled.connect(self.label_113.setVisible)
        self.checkBoxDfilterMs.toggled.connect(self.dateDMsFilterT1.setVisible)
        self.checkBoxDfilterMs.toggled.connect(self.dateDMsFilterT2.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.cboxAnaCount.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.cboxAnaCountPerDate.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.labelInsertFacture_4.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.cboxAnaCountChartType.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.labelInsertFacture_6.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.btnAnaCountDisplay.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.editAnaCountValue.setVisible)
        self.checkBoxAnaGroupe.toggled.connect(self.cboxAnaCountFunc.setVisible)
        self.checkBoxAnaTS.toggled.connect(self.cboxAnaTS.setVisible)
        self.checkBoxAnaTS.toggled.connect(self.btnAnaTSDisplay.setVisible)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(15)
        self.stackedWidget.setCurrentIndex(13)
        self.cboxUQCmdFilter.setCurrentIndex(0)
        self.cboxCalcCmd.setCurrentIndex(0)
        self.cBoxModePaiementCmdInsert.setCurrentIndex(0)
        self.cBoxCodeClientCmdInsert.setCurrentIndex(-1)
        self.cboxUQFactureFilter.setCurrentIndex(0)
        self.cboxCalcFacture.setCurrentIndex(0)
        self.cboxUQRLivFilter.setCurrentIndex(0)
        self.cboxUQLivFilter.setCurrentIndex(0)
        self.cboxCalcLiv.setCurrentIndex(0)
        self.cboxCodeCmdLivAdd.setCurrentIndex(0)
        self.cboxAnaTS.setCurrentIndex(0)
        self.cboxAnaCountPerDate.setCurrentIndex(0)
        self.cboxAnaCountChartType.setCurrentIndex(0)
        self.cboxAnaCount.setCurrentIndex(0)
        self.cboxAnaCountFunc.setCurrentIndex(0)
        self.cboxCodeLivFactureAdd.setCurrentIndex(0)
        self.cBoxModePaiementFactureInsert.setCurrentIndex(0)
        self.cBoxNomAdvClientInsert.setCurrentIndex(-1)
        self.cBoxUPoidsProduitInsert.setCurrentIndex(0)
        self.cboxMarqueProduitInsert.setCurrentIndex(-1)
        self.cboxUQStockFilter.setCurrentIndex(0)
        self.cboxUQInvFilter.setCurrentIndex(0)
        self.cBoxCodeProduitStockInsert.setCurrentIndex(-1)
        self.cboxCodeEmpStockInsert.setCurrentIndex(-1)
        self.cboxTypeInvInsert.setCurrentIndex(0)
        self.cboxCodeEmpInvInsert.setCurrentIndex(-1)
        self.cBoxCodeProduitInvInsert.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Compact Inventory Monitor", None))
        self.btnPageProduit.setText(QCoreApplication.translate("MainWindow", u"Produit", None))
        self.btnPageStock.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.btnPageInv.setText(QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.btnPageMS.setText(QCoreApplication.translate("MainWindow", u"Mouvement de stock", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tabDepot), QCoreApplication.translate("MainWindow", u"D\u00e9p\u00f4t ", None))
        self.btnPageClient.setText(QCoreApplication.translate("MainWindow", u"Tableau des clients", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tabClient), QCoreApplication.translate("MainWindow", u"Client", None))
        self.btnPageCmd.setText(QCoreApplication.translate("MainWindow", u"Tableau des commandes", None))
        self.btnPageInsertCmd.setText(QCoreApplication.translate("MainWindow", u"Page d'insertion", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tabCmd), QCoreApplication.translate("MainWindow", u"Commande", None))
        self.btnPageFacture.setText(QCoreApplication.translate("MainWindow", u"Tableau des Factures", None))
        self.btnPageInsertFacture.setText(QCoreApplication.translate("MainWindow", u"Page d'insertion", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tabFac), QCoreApplication.translate("MainWindow", u"Facture", None))
        self.btnPageLiv.setText(QCoreApplication.translate("MainWindow", u"Tableau des livraisons", None))
        self.btnPageInsertLiv.setText(QCoreApplication.translate("MainWindow", u"Page d'insertion", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tabLiv), QCoreApplication.translate("MainWindow", u"Livraison", None))
        self.btnPageCharts.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.btnPageReport.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tabTools), QCoreApplication.translate("MainWindow", u"Tools", None))
#if QT_CONFIG(tooltip)
        self.btnRollback.setToolTip(QCoreApplication.translate("MainWindow", u"Annuler la derni\u00e8re query", None))
#endif // QT_CONFIG(tooltip)
        self.btnRollback.setText("")
#if QT_CONFIG(tooltip)
        self.btnLoad.setToolTip(QCoreApplication.translate("MainWindow", u"Recharger toutes les donn\u00e9es", None))
#endif // QT_CONFIG(tooltip)
        self.btnLoad.setText("")
#if QT_CONFIG(tooltip)
        self.btnConnect.setToolTip(QCoreApplication.translate("MainWindow", u"Tester la connexion aux server", None))
#endif // QT_CONFIG(tooltip)
        self.btnConnect.setText("")
        self.editFilterProduit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterProduit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechProduit.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
#if QT_CONFIG(tooltip)
        self.btnPageProduitInsert.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
#endif // QT_CONFIG(tooltip)
        self.btnPageProduitInsert.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Produit", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
#if QT_CONFIG(tooltip)
        self.refreshProduit.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshProduit.setText("")
        self.editFilterCmd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterCmd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechCmd.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
#if QT_CONFIG(tooltip)
        self.btnPageCmdInsert.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
#endif // QT_CONFIG(tooltip)
        self.btnPageCmdInsert.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.dateDCCmdFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.checkBoxDCfilterCmd.setText(QCoreApplication.translate("MainWindow", u"Plage de date commande", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.checkBoxQfilterCmd.setText(QCoreApplication.translate("MainWindow", u"Plage de quantite", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.dateDCCmdFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.cboxUQCmdFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Unite", None))
        self.cboxUQCmdFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Palette", None))
        self.cboxUQCmdFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Carton", None))

        self.cboxUQCmdFilter.setPlaceholderText("")
        self.cboxCalcCmd.setItemText(0, QCoreApplication.translate("MainWindow", u"TotalMontantHT", None))
        self.cboxCalcCmd.setItemText(1, QCoreApplication.translate("MainWindow", u"TotalQuantite", None))

        self.cboxCalcCmd.setPlaceholderText("")
        self.btnCalcCmd.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Commande", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
        self.checkBoxViewTypeCmd.setText(QCoreApplication.translate("MainWindow", u"Masquer les produit", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Afficher", None))
#if QT_CONFIG(tooltip)
        self.refreshCmd.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshCmd.setText("")
        self.btnInsertCmd.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.cBoxModePaiementCmdInsert.setItemText(0, QCoreApplication.translate("MainWindow", u"Virement bancaire", None))
        self.cBoxModePaiementCmdInsert.setItemText(1, QCoreApplication.translate("MainWindow", u"ACH", None))
        self.cBoxModePaiementCmdInsert.setItemText(2, QCoreApplication.translate("MainWindow", u"Credit/Debit", None))
        self.cBoxModePaiementCmdInsert.setItemText(3, QCoreApplication.translate("MainWindow", u"Cheque", None))
        self.cBoxModePaiementCmdInsert.setItemText(4, QCoreApplication.translate("MainWindow", u"PayPal", None))

        self.cBoxModePaiementCmdInsert.setPlaceholderText("")
        self.labelInsertCmd.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer une commande", None))
        ___qtablewidgetitem = self.tableWidgetCmd.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CodeProduit", None));
        ___qtablewidgetitem1 = self.tableWidgetCmd.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"QuantiteUnite", None));
        ___qtablewidgetitem2 = self.tableWidgetCmd.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"QuantiteCarton", None));
        ___qtablewidgetitem3 = self.tableWidgetCmd.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"QuantitePalette", None));
        self.btnUpdateCmd.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
#if QT_CONFIG(tooltip)
        self.btnSubRowCmd.setToolTip(QCoreApplication.translate("MainWindow", u"Supprimer la ligne s\u00e9lectionn\u00e9e", None))
#endif // QT_CONFIG(tooltip)
        self.btnSubRowCmd.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cBoxCodeClientCmdInsert.setPlaceholderText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"ModePaiement", None))
#if QT_CONFIG(tooltip)
        self.btnAddRowCmd.setToolTip(QCoreApplication.translate("MainWindow", u"Ajouter une ligne vide", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddRowCmd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Code Client", None))
        self.editFilterFacture.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterFacture.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechFacture.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
#if QT_CONFIG(tooltip)
        self.btnPageFactureInsert.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
#endif // QT_CONFIG(tooltip)
        self.btnPageFactureInsert.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.dateDFFactureFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.checkBoxDFfilterFacture.setText(QCoreApplication.translate("MainWindow", u"Plage de date facture", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.checkBoxQfilterFacture.setText(QCoreApplication.translate("MainWindow", u"Plage de quantite", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.dateDFFactureFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.cboxUQFactureFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Unite", None))
        self.cboxUQFactureFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Palette", None))
        self.cboxUQFactureFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Carton", None))

        self.cboxUQFactureFilter.setPlaceholderText("")
        self.cboxCalcFacture.setItemText(0, QCoreApplication.translate("MainWindow", u"TotalQuantite_TotalHT_TVA_TTC", None))

        self.cboxCalcFacture.setPlaceholderText("")
        self.btnCalcFacture.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Facture", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
        self.checkBoxViewTypeFacture.setText(QCoreApplication.translate("MainWindow", u"Masquer les produit", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Afficher", None))
#if QT_CONFIG(tooltip)
        self.refreshFacture.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshFacture.setText("")
        self.editFilterMS.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterMS.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechMs.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
        self.dateDMsFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.checkBoxDfilterMs.setText(QCoreApplication.translate("MainWindow", u"Plage de date", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.dateDMsFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Mouvement de stock", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
#if QT_CONFIG(tooltip)
        self.refreshMs.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshMs.setText("")
        self.editFilterLiv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterLiv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechLiv.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
#if QT_CONFIG(tooltip)
        self.btnPageLivInsert.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
#endif // QT_CONFIG(tooltip)
        self.btnPageLivInsert.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.cboxUQRLivFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Unite", None))
        self.cboxUQRLivFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Palette", None))
        self.cboxUQRLivFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Carton", None))

        self.cboxUQRLivFilter.setPlaceholderText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par", None))
        self.btnCalcLiv.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.cboxUQLivFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Unite", None))
        self.cboxUQLivFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Palette", None))
        self.cboxUQLivFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Carton", None))

        self.cboxUQLivFilter.setPlaceholderText("")
        self.dateDLLivFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.checkBoxDLfilterLiv.setText(QCoreApplication.translate("MainWindow", u"Plage de date livraison", None))
        self.dateDLLivFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.cboxCalcLiv.setItemText(0, QCoreApplication.translate("MainWindow", u"TotalQuantite", None))

        self.cboxCalcLiv.setPlaceholderText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.checkBoxQfilterLiv.setText(QCoreApplication.translate("MainWindow", u"Plage de quantite Livr\u00e9e", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.checkBoxQRfilterLiv.setText(QCoreApplication.translate("MainWindow", u"Plage de quantite recue", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Livraison", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
        self.checkBoxViewTypeLiv.setText(QCoreApplication.translate("MainWindow", u"Masquer les produit", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Afficher", None))
#if QT_CONFIG(tooltip)
        self.refreshLiv.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshLiv.setText("")
        ___qtablewidgetitem4 = self.tableWidgetLiv.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CodeCommande", None));
        ___qtablewidgetitem5 = self.tableWidgetLiv.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CodeProduit", None));
        ___qtablewidgetitem6 = self.tableWidgetLiv.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"CodeEmplacement", None));
        ___qtablewidgetitem7 = self.tableWidgetLiv.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Lot", None));
        ___qtablewidgetitem8 = self.tableWidgetLiv.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DateFabrication", None));
        ___qtablewidgetitem9 = self.tableWidgetLiv.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"DateExpiration", None));
        ___qtablewidgetitem10 = self.tableWidgetLiv.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"QuantiteLivreeUnite", None));
        ___qtablewidgetitem11 = self.tableWidgetLiv.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"QuantiteLivreeCarton", None));
        ___qtablewidgetitem12 = self.tableWidgetLiv.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"QuantiteLivreePalette", None));
        ___qtablewidgetitem13 = self.tableWidgetLiv.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"QuantiteRecueUnite", None));
        ___qtablewidgetitem14 = self.tableWidgetLiv.horizontalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"QuantiteRecueCarton", None));
        ___qtablewidgetitem15 = self.tableWidgetLiv.horizontalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"QuantiteRecuePalette", None));
        ___qtablewidgetitem16 = self.tableWidgetLiv.horizontalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"TotalQuantiteRejetee par Unite", None));
        ___qtablewidgetitem17 = self.tableWidgetLiv.horizontalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"DescriptionProduitsRejetee", None));
        self.btnInsertLiv.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
#if QT_CONFIG(tooltip)
        self.btnAddRowLiv.setToolTip(QCoreApplication.translate("MainWindow", u"Ajouter une ligne", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddRowLiv.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnUpdateLiv.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
#if QT_CONFIG(tooltip)
        self.btnSubRowLiv.setToolTip(QCoreApplication.translate("MainWindow", u"Supprimer la ligne s\u00e9lectionn\u00e9e", None))
#endif // QT_CONFIG(tooltip)
        self.btnSubRowLiv.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Address de livraison", None))
        self.labelInsertLiv.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer une livraison", None))
        self.cboxCodeCmdLivAdd.setItemText(0, QCoreApplication.translate("MainWindow", u"Ligne vide", None))

#if QT_CONFIG(tooltip)
        self.cboxCodeCmdLivAdd.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer une ligne vide ou un codeCommande", None))
#endif // QT_CONFIG(tooltip)
        self.cboxCodeCmdLivAdd.setPlaceholderText("")
        self.btnAnaCountDisplay.setText(QCoreApplication.translate("MainWindow", u"Afficher", None))
        self.labelInsertFacture_8.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.dateAnaLoadD1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.labelInsertFacture_9.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.dateAnaLoadD2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
#if QT_CONFIG(tooltip)
        self.btnAnaLoadDf.setToolTip(QCoreApplication.translate("MainWindow", u"Charger les donnes", None))
#endif // QT_CONFIG(tooltip)
        self.btnAnaLoadDf.setText("")
        self.labelInsertFacture_7.setText(QCoreApplication.translate("MainWindow", u"Charger des donn\u00e9es", None))
        self.labelInsertFacture_6.setText(QCoreApplication.translate("MainWindow", u"Type de chart", None))
        self.cboxAnaTS.setItemText(0, QCoreApplication.translate("MainWindow", u"Tendance des ventes", None))
        self.cboxAnaTS.setItemText(1, QCoreApplication.translate("MainWindow", u"Saisonnalit\u00e9 des ventes", None))

        self.cboxAnaTS.setPlaceholderText("")
        self.editAnaCountValue.setPlaceholderText("")
        self.btnAnaTSDisplay.setText(QCoreApplication.translate("MainWindow", u"Afficher", None))
        self.cboxAnaCountPerDate.setItemText(0, QCoreApplication.translate("MainWindow", u"Ann\u00e9e", None))
        self.cboxAnaCountPerDate.setItemText(1, QCoreApplication.translate("MainWindow", u"Mois", None))
        self.cboxAnaCountPerDate.setItemText(2, QCoreApplication.translate("MainWindow", u"Jour", None))
        self.cboxAnaCountPerDate.setItemText(3, QCoreApplication.translate("MainWindow", u"Jour de la semaine", None))

        self.cboxAnaCountPerDate.setPlaceholderText("")
        self.checkBoxAnaGroupe.setText(QCoreApplication.translate("MainWindow", u" Groupe", None))
        self.labelInsertFacture_5.setText(QCoreApplication.translate("MainWindow", u"Options d'analyse", None))
        self.cboxAnaCountChartType.setItemText(0, QCoreApplication.translate("MainWindow", u"bar", None))
        self.cboxAnaCountChartType.setItemText(1, QCoreApplication.translate("MainWindow", u"barh", None))

        self.cboxAnaCountChartType.setPlaceholderText("")
        self.checkBoxAnaTS.setText(QCoreApplication.translate("MainWindow", u"Time series", None))
        self.labelInsertFacture_4.setText(QCoreApplication.translate("MainWindow", u"Par", None))
        self.cboxAnaCount.setItemText(0, QCoreApplication.translate("MainWindow", u"Total commandes", None))
        self.cboxAnaCount.setItemText(1, QCoreApplication.translate("MainWindow", u"Total commandes par client", None))
        self.cboxAnaCount.setItemText(2, QCoreApplication.translate("MainWindow", u"Montant total d\u00e9pens\u00e9 par client", None))
        self.cboxAnaCount.setItemText(3, QCoreApplication.translate("MainWindow", u"Quantit\u00e9 totale vendue par produit", None))
        self.cboxAnaCount.setItemText(4, QCoreApplication.translate("MainWindow", u"Revenu total g\u00e9n\u00e9r\u00e9 par chaque produit", None))
        self.cboxAnaCount.setItemText(5, QCoreApplication.translate("MainWindow", u"Revenu total g\u00e9n\u00e9r\u00e9 par chaque mode de paiement", None))

        self.cboxAnaCount.setPlaceholderText("")
        self.cboxAnaCountFunc.setItemText(0, QCoreApplication.translate("MainWindow", u"mean", None))
        self.cboxAnaCountFunc.setItemText(1, QCoreApplication.translate("MainWindow", u"sum", None))

        self.cboxAnaCountFunc.setPlaceholderText("")
        self.labelchart.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer un rapport pour", None))
        self.cboxRep.setItemText(0, QCoreApplication.translate("MainWindow", u"Facture", None))

        self.cboxRep.setPlaceholderText("")
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Code", None))
        self.editRep.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.btnPageRepPrev.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnPageRepPrev.setText(QCoreApplication.translate("MainWindow", u"Aper\u00e7u", None))
#if QT_CONFIG(tooltip)
        self.btnPageRepNav.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnPageRepNav.setText(QCoreApplication.translate("MainWindow", u"Ouvrir dans le navigateur", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Taux TVA", None))
#if QT_CONFIG(tooltip)
        self.btnSubRowFacture.setToolTip(QCoreApplication.translate("MainWindow", u"Supprimer la ligne s\u00e9lectionn\u00e9e", None))
#endif // QT_CONFIG(tooltip)
        self.btnSubRowFacture.setText(QCoreApplication.translate("MainWindow", u"-", None))
        ___qtablewidgetitem18 = self.tableWidgetFacture.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"CodeCommande", None));
        ___qtablewidgetitem19 = self.tableWidgetFacture.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"CodeProduit", None));
        ___qtablewidgetitem20 = self.tableWidgetFacture.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"QuantiteUnite", None));
        ___qtablewidgetitem21 = self.tableWidgetFacture.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"QuantiteCarton", None));
        ___qtablewidgetitem22 = self.tableWidgetFacture.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"QuantitePalette", None));
        ___qtablewidgetitem23 = self.tableWidgetFacture.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Remise", None));
        ___qtablewidgetitem24 = self.tableWidgetFacture.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Etat", None));
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"ModePaiement", None))
        self.labelInsertFacture.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer une facture", None))
#if QT_CONFIG(tooltip)
        self.btnAddRowFacture.setToolTip(QCoreApplication.translate("MainWindow", u"Ajouter une ligne vide", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddRowFacture.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.cboxCodeLivFactureAdd.setItemText(0, QCoreApplication.translate("MainWindow", u"Ligne vide", None))

#if QT_CONFIG(tooltip)
        self.cboxCodeLivFactureAdd.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer une ligne vide ou un codeLivraison", None))
#endif // QT_CONFIG(tooltip)
        self.cboxCodeLivFactureAdd.setPlaceholderText("")
        self.cBoxModePaiementFactureInsert.setItemText(0, QCoreApplication.translate("MainWindow", u"Virement bancaire", None))
        self.cBoxModePaiementFactureInsert.setItemText(1, QCoreApplication.translate("MainWindow", u"ACH", None))
        self.cBoxModePaiementFactureInsert.setItemText(2, QCoreApplication.translate("MainWindow", u"Cr\u00e9dit/D\u00e9bit", None))
        self.cBoxModePaiementFactureInsert.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e8que", None))
        self.cBoxModePaiementFactureInsert.setItemText(4, QCoreApplication.translate("MainWindow", u"PayPal", None))

        self.cBoxModePaiementFactureInsert.setPlaceholderText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u" Date d'\u00e9ch\u00e9ance", None))
        self.btnInsertFacture.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.btnUpdateFacture.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.dateEchFactureInsert.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.spinBoxTvaFactureInsert.setPrefix("")
        self.editFilterClient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterClient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechClient.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
#if QT_CONFIG(tooltip)
        self.btnPageClientInsert.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
#endif // QT_CONFIG(tooltip)
        self.btnPageClientInsert.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
#if QT_CONFIG(tooltip)
        self.refreshClient.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshClient.setText("")
        self.cBoxNomAdvClientInsert.setPlaceholderText("")
        self.labelInsertClient.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un client", None))
        self.btnInsertClient.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"ADV", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Telephone", None))
        self.btnUpdateClient.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Wilaya", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Capacit\u00e9 Carton (U)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nom de produit", None))
        self.cBoxTypeProduitInsert.setItemText(0, QCoreApplication.translate("MainWindow", u"Pack", None))
        self.cBoxTypeProduitInsert.setItemText(1, QCoreApplication.translate("MainWindow", u"CS", None))

        self.cBoxTypeProduitInsert.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Unite de poids", None))
        self.cBoxUPoidsProduitInsert.setItemText(0, QCoreApplication.translate("MainWindow", u"G", None))
        self.cBoxUPoidsProduitInsert.setItemText(1, QCoreApplication.translate("MainWindow", u"L", None))

        self.cBoxUPoidsProduitInsert.setPlaceholderText("")
        self.spinBoxPrixUProduitInsert.setPrefix(QCoreApplication.translate("MainWindow", u"$ ", None))
        self.spinBoxPoidsUProduitInsert.setPrefix("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Capacit\u00e9 Palette (C)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.labelInsertProduit.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
        self.cboxMarqueProduitInsert.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Prix Unitaire", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Poids Unitaire (G/L)", None))
        self.btnUpdateProduit.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.btnInsertProduit.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.editFilterStock.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterStock.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechStock.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
#if QT_CONFIG(tooltip)
        self.btnPageStockInsert.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
#endif // QT_CONFIG(tooltip)
        self.btnPageStockInsert.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par", None))
        self.checkBoxDEfilterStock.setText(QCoreApplication.translate("MainWindow", u"Plage de date expiration", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.dateDEStockFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.dateDFStockFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.dateDFStockFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.dateDEStockFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.checkBoxDFfilterStock.setText(QCoreApplication.translate("MainWindow", u"Plage de date fabrication", None))
        self.checkBoxQfilterStock.setText(QCoreApplication.translate("MainWindow", u"Plage de quantite", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.cboxUQStockFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Unite", None))
        self.cboxUQStockFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Palette", None))
        self.cboxUQStockFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Carton", None))

        self.cboxUQStockFilter.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Afficher", None))
#if QT_CONFIG(tooltip)
        self.refreshStock.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshStock.setText("")
        self.editFilterInv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.cboxFilterInv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherch\u00e9 par", None))
        self.btnRechInv.setText(QCoreApplication.translate("MainWindow", u"Recherche", None))
#if QT_CONFIG(tooltip)
        self.btnPageInvInsert.setToolTip(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit", None))
#endif // QT_CONFIG(tooltip)
        self.btnPageInvInsert.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Filtr\u00e9 par", None))
        self.checkBoxDEfilterInv.setText(QCoreApplication.translate("MainWindow", u"Plage de date expiration", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.dateDEInvFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.dateDFInvFilterT2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.dateDFInvFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.dateDEInvFilterT1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.checkBoxDFfilterInv.setText(QCoreApplication.translate("MainWindow", u"Plage de date fabrication", None))
        self.checkBoxQfilterInv.setText(QCoreApplication.translate("MainWindow", u"Plage de quantite", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.cboxUQInvFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Unite", None))
        self.cboxUQInvFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Palette", None))
        self.cboxUQInvFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Carton", None))

        self.cboxUQInvFilter.setPlaceholderText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Obtenir", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"lignes", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Afficher", None))
#if QT_CONFIG(tooltip)
        self.refreshInv.setToolTip(QCoreApplication.translate("MainWindow", u"Rafra\u00eecher la table", None))
#endif // QT_CONFIG(tooltip)
        self.refreshInv.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"DateExpiration", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CodeProduit", None))
        self.dateDEStockInsert.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Quantite par unite", None))
        self.btnUpdateStock.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.labelInsertStock.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un produit dans le stock", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Lot", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Quantite par palette", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"DateFabrication", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CodeEmplacement", None))
        self.dateDFStockInsert.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.cBoxCodeProduitStockInsert.setPlaceholderText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Quantite par carton", None))
        self.btnInsertStock.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"DateFabrication", None))
        self.cboxTypeInvInsert.setItemText(0, QCoreApplication.translate("MainWindow", u"Verification", None))
        self.cboxTypeInvInsert.setItemText(1, QCoreApplication.translate("MainWindow", u"Production", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"DateExpiration", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Quantite par palette", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CodeEmplacement", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Quantite par unite", None))
        self.dateDEInvInsert.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Lot", None))
        self.cBoxCodeProduitInvInsert.setPlaceholderText("")
        self.dateDFInvInsert.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.btnInsertInv.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Type d'inventaire", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"CodeProduit", None))
        self.labelInsertInv.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer un inventaire", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Quantite par carton", None))
        self.btnUpdateInv.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
    # retranslateUi

