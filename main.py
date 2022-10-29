# -*- coding: utf-8 -*-
import sqlite3
import sys
import src

from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


# Класс на отслеживание кликов на QLabel
class ClickedLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """Базовая настройка интерфейса"""

        # Настройка отображения главного экрана
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 698)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1246, 698))
        MainWindow.setMaximumSize(QtCore.QSize(1246, 698))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: #191919;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # end Настройка отображения главного экрана

        # Настройка главного меню
        # - Header
        self.header = QtWidgets.QGroupBox(self.centralwidget)
        self.header.setEnabled(True)
        self.header.setGeometry(QtCore.QRect(0, 0, 269, 698))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(269, 0))
        self.header.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.header.setStyleSheet("border: 0;\n"
                                  "background: #151515;")
        self.header.setObjectName("header")
        # - Logo
        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setGeometry(QtCore.QRect(20, 20, 142, 52))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(142, 52))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/src/img/logo.svg"))
        self.logo.setObjectName("logo")
        # - Add folder btn
        self.btn_add_folder = ClickedLabel(self.header)
        self.btn_add_folder.setGeometry(QtCore.QRect(218, 30, 24, 31))
        self.btn_add_folder.setPixmap(QtGui.QPixmap(":/src/img/add_folder.svg"))
        self.btn_add_folder.setObjectName("btn_add_folder")
        self.btn_add_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # - Buttons
        self.buttons = QtWidgets.QGroupBox(self.header)
        self.buttons.setGeometry(QtCore.QRect(23, 93, 219, 583))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setMaximumSize(QtCore.QSize(219, 583))
        self.buttons.setTitle("")
        self.buttons.setObjectName("buttons")
        # end Настройка главного меню

        # Настройка main
        self.main = QtWidgets.QStackedWidget(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(269, -20, 977, 719))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMinimumSize(QtCore.QSize(977, 719))
        self.main.setMaximumSize(QtCore.QSize(977, 719))
        self.main.setObjectName("main")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setMaximumSize(QtCore.QSize(977, 719))
        self.page_3.setObjectName("page_3")
        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 708, 698))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(708, 698))
        self.scrollArea.setMaximumSize(QtCore.QSize(708, 698))
        self.scrollArea.setStyleSheet("border: 0;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 708, 698))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setContentsMargins(25, 25, 25, 25)
        self.gridLayout.setObjectName("gridLayout")
        self.tasks_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.tasks_7.setTitle("")
        self.tasks_7.setObjectName("tasks_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tasks_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tasks_7)
        self.label_5.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 16px;\n"
                                   "/* identical to box height, or 100% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #A3A3A3;")
        self.label_5.setObjectName("label_5")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.verticalLayout_8.addLayout(self.formLayout_6)
        self.gridLayout.addWidget(self.tasks_7, 8, 0, 1, 1)
        self.tasks_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.tasks_1.setTitle("")
        self.tasks_1.setObjectName("tasks_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tasks_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.task_1_1 = QtWidgets.QFormLayout()
        self.task_1_1.setContentsMargins(-1, 10, -1, -1)
        self.task_1_1.setObjectName("task_1_1")
        self.task_btn_1_1 = QtWidgets.QToolButton(self.tasks_1)
        self.task_btn_1_1.setMaximumSize(QtCore.QSize(18, 18))
        self.task_btn_1_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.task_btn_1_1.setStyleSheet("border: 1px solid #FFFFFF;\n"
                                        "border-radius: 5px;")
        self.task_btn_1_1.setText("")
        self.task_btn_1_1.setObjectName("task_btn_1_1")
        self.task_1_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.task_btn_1_1)
        self.task_description_1_1 = QtWidgets.QLabel(self.tasks_1)
        self.task_description_1_1.setStyleSheet("font-family: \'Inter\';\n"
                                                "font-style: normal;\n"
                                                "font-weight: 400;\n"
                                                "font-size: 16px;\n"
                                                "line-height: 16px;\n"
                                                "/* identical to box height, or 100% */\n"
                                                "\n"
                                                "letter-spacing: -0.055em;\n"
                                                "\n"
                                                "color: #FFFFFF;")
        self.task_description_1_1.setWordWrap(False)
        self.task_description_1_1.setObjectName("task_description_1_1")
        self.task_1_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.task_description_1_1)
        self.verticalLayout.addLayout(self.task_1_1)
        self.gridLayout.addWidget(self.tasks_1, 1, 0, 1, 1)
        self.tasks_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.tasks_5.setTitle("")
        self.tasks_5.setObjectName("tasks_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tasks_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tasks_5)
        self.label_3.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 16px;\n"
                                   "/* identical to box height, or 100% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #A3A3A3;")
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout_6.addLayout(self.formLayout_4)
        self.gridLayout.addWidget(self.tasks_5, 6, 0, 1, 1)
        self.tasks_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.tasks_3.setTitle("")
        self.tasks_3.setObjectName("tasks_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tasks_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.tasks_3)
        self.label.setStyleSheet("font-family: \'Inter\';\n"
                                 "font-style: normal;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px;\n"
                                 "line-height: 16px;\n"
                                 "/* identical to box height, or 100% */\n"
                                 "\n"
                                 "letter-spacing: -0.055em;\n"
                                 "\n"
                                 "color: #A3A3A3;")
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.gridLayout.addWidget(self.tasks_3, 4, 0, 1, 1)
        self.tasks_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.tasks_4.setTitle("")
        self.tasks_4.setObjectName("tasks_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tasks_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tasks_4)
        self.label_2.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 16px;\n"
                                   "/* identical to box height, or 100% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #A3A3A3;")
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_5.addLayout(self.formLayout_3)
        self.gridLayout.addWidget(self.tasks_4, 4, 1, 1, 1)
        self.tasks_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.tasks_6.setTitle("")
        self.tasks_6.setObjectName("tasks_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tasks_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tasks_6)
        self.label_4.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 16px;\n"
                                   "/* identical to box height, or 100% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #A3A3A3;")
        self.label_4.setObjectName("label_4")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout_7.addLayout(self.formLayout_5)
        self.gridLayout.addWidget(self.tasks_6, 6, 1, 1, 1)
        self.title_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_6.sizePolicy().hasHeightForWidth())
        self.title_6.setSizePolicy(sizePolicy)
        self.title_6.setMaximumSize(QtCore.QSize(16777215, 29))
        self.title_6.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.title_6.setObjectName("title_6")
        self.gridLayout.addWidget(self.title_6, 5, 1, 1, 1)
        self.title_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_1.sizePolicy().hasHeightForWidth())
        self.title_1.setSizePolicy(sizePolicy)
        self.title_1.setMaximumSize(QtCore.QSize(16777215, 29))
        self.title_1.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.title_1.setObjectName("title_1")
        self.gridLayout.addWidget(self.title_1, 0, 0, 1, 1)
        self.title_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy)
        self.title_2.setMaximumSize(QtCore.QSize(16777215, 29))
        self.title_2.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.title_2.setObjectName("title_2")
        self.gridLayout.addWidget(self.title_2, 0, 1, 1, 1)
        self.title_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_3.sizePolicy().hasHeightForWidth())
        self.title_3.setSizePolicy(sizePolicy)
        self.title_3.setMaximumSize(QtCore.QSize(16777215, 29))
        self.title_3.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.title_3.setObjectName("title_3")
        self.gridLayout.addWidget(self.title_3, 3, 0, 1, 1)
        self.title_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_4.sizePolicy().hasHeightForWidth())
        self.title_4.setSizePolicy(sizePolicy)
        self.title_4.setMaximumSize(QtCore.QSize(16777215, 29))
        self.title_4.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.title_4.setObjectName("title_4")
        self.gridLayout.addWidget(self.title_4, 3, 1, 1, 1)
        self.title_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_5.sizePolicy().hasHeightForWidth())
        self.title_5.setSizePolicy(sizePolicy)
        self.title_5.setMaximumSize(QtCore.QSize(16777215, 29))
        self.title_5.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.title_5.setObjectName("title_5")
        self.gridLayout.addWidget(self.title_5, 5, 0, 1, 1)
        self.title_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_7.sizePolicy().hasHeightForWidth())
        self.title_7.setSizePolicy(sizePolicy)
        self.title_7.setMaximumSize(QtCore.QSize(16777215, 29))
        self.title_7.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.title_7.setObjectName("title_7")
        self.gridLayout.addWidget(self.title_7, 7, 0, 1, 1)
        self.tasks_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.tasks_2.setTitle("")
        self.tasks_2.setObjectName("tasks_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tasks_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.task_2_1 = QtWidgets.QFormLayout()
        self.task_2_1.setContentsMargins(-1, 10, -1, -1)
        self.task_2_1.setObjectName("task_2_1")
        self.checkBox = QtWidgets.QCheckBox(self.tasks_2)
        self.checkBox.setObjectName("checkBox")
        self.task_2_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.verticalLayout_2.addLayout(self.task_2_1)
        self.gridLayout.addWidget(self.tasks_2, 1, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(708, 20, 271, 691))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 691))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 691))
        self.scrollArea_2.setStyleSheet("border: 0;\n"
                                        "background: #151515;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 271, 691))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 29))
        self.label_9.setStyleSheet("font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 700;\n"
                                   "font-size: 24px;\n"
                                   "line-height: 29px;\n"
                                   "/* identical to box height, or 121% */\n"
                                   "\n"
                                   "letter-spacing: -0.055em;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_2.addWidget(self.groupBox_9, 3, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("position: top;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        self.task_2_2 = QtWidgets.QFormLayout()
        self.task_2_2.setContentsMargins(-1, 10, -1, -1)
        self.task_2_2.setObjectName("task_2_2")
        self.task_btn_2_2 = QtWidgets.QToolButton(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_btn_2_2.sizePolicy().hasHeightForWidth())
        self.task_btn_2_2.setSizePolicy(sizePolicy)
        self.task_btn_2_2.setMaximumSize(QtCore.QSize(18, 18))
        self.task_btn_2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.task_btn_2_2.setStyleSheet("background: #1490AA;\n"
                                        "border-radius: 5px;")
        self.task_btn_2_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/img/task_done.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.task_btn_2_2.setIcon(icon1)
        self.task_btn_2_2.setObjectName("task_btn_2_2")
        self.task_2_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.task_btn_2_2)
        self.task_description_2_2 = QtWidgets.QLabel(self.groupBox_8)
        self.task_description_2_2.setStyleSheet("font-family: \'Inter\';\n"
                                                "font-style: normal;\n"
                                                "font-weight: 400;\n"
                                                "font-size: 16px;\n"
                                                "line-height: 16px;\n"
                                                "/* identical to box height, or 100% */\n"
                                                "\n"
                                                "letter-spacing: -0.055em;\n"
                                                "\n"
                                                "color: #FFFFFF;")
        self.task_description_2_2.setTextFormat(QtCore.Qt.AutoText)
        self.task_description_2_2.setScaledContents(False)
        self.task_description_2_2.setWordWrap(True)
        self.task_description_2_2.setObjectName("task_description_2_2")
        self.task_2_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.task_description_2_2)
        self.gridLayout_4.addLayout(self.task_2_2, 0, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 29))
        self.label_10.setStyleSheet("font-family: \'Inter\';\n"
                                    "font-style: normal;\n"
                                    "font-weight: 700;\n"
                                    "font-size: 24px;\n"
                                    "line-height: 29px;\n"
                                    "/* identical to box height, or 121% */\n"
                                    "\n"
                                    "letter-spacing: -0.055em;\n"
                                    "\n"
                                    "color: #FFFFFF;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.main.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.main.addWidget(self.page_4)
        # end Настройка main

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tasker"))
        self.label_5.setText(_translate("MainWindow", "Задач нет"))
        self.task_description_1_1.setText(_translate("MainWindow", "Простое задание"))
        self.label_3.setText(_translate("MainWindow", "Задач нет"))
        self.label.setText(_translate("MainWindow", "Задач нет"))
        self.label_2.setText(_translate("MainWindow", "Задач нет"))
        self.label_4.setText(_translate("MainWindow", "Задач нет"))
        self.title_6.setText(_translate("MainWindow", "Среда, 28 октября"))
        self.title_1.setText(_translate("MainWindow", "Сегодня"))
        self.title_2.setText(_translate("MainWindow", "Завтра"))
        self.title_3.setText(_translate("MainWindow", "Послезавтра"))
        self.title_4.setText(_translate("MainWindow", "Понедельник, 31 октября"))
        self.title_5.setText(_translate("MainWindow", "Вторник, 27 октября"))
        self.title_7.setText(_translate("MainWindow", "Четверг, 29 октября"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_9.setText(_translate("MainWindow", "Просроченные"))
        self.label_6.setText(_translate("MainWindow", "27.01"))
        self.task_description_2_2.setText(_translate("MainWindow", "Простое задание"))
        self.label_10.setText(_translate("MainWindow", "Предстоящие"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect('data/tasker_data.db')
        self.cur = self.db.cursor()

        self.setupUi(self)
        self.headers_btn_setup()
        self.btn_add_folder.clicked.connect(self.add_folder)

    def headers_btn_setup(self):
        self.btn_menu1 = QtWidgets.QPushButton(self.buttons)
        self.btn_menu1.setGeometry(QtCore.QRect(0, 0, 219, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu1.sizePolicy().hasHeightForWidth())
        self.btn_menu1.setSizePolicy(sizePolicy)
        self.btn_menu1.setMaximumSize(QtCore.QSize(219, 37))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu1.setFont(font)
        self.btn_menu1.setStyleSheet("background: #1490AA;\n"
                                     "border-radius: 11px;\n"
                                     "font-family: \'Inter\';\n"
                                     "font-style: normal;\n"
                                     "font-weight: 400;\n"
                                     "font-size: 16px;\n"
                                     "line-height: 19px;\n"
                                     "text-align: left;\n"
                                     "color: #FFFFFF;\n"
                                     "padding: 8px 0 8px 15px;")
        self.btn_menu1.setObjectName("btn_menu1")

        folders = self.cur.execute('''SELECT * FROM folders''').fetchall()
        for button in folders:
            pass
        self.btn_menu2 = QtWidgets.QPushButton(self.buttons)
        self.btn_menu2.setGeometry(QtCore.QRect(0, 47, 219, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu2.sizePolicy().hasHeightForWidth())
        self.btn_menu2.setSizePolicy(sizePolicy)
        self.btn_menu2.setMaximumSize(QtCore.QSize(219, 37))
        self.btn_menu2.setStyleSheet("background: #282828;\n"
                                     "border-radius: 11px;\n"
                                     "font-family: \'Inter\';\n"
                                     "font-style: normal;\n"
                                     "font-weight: 400;\n"
                                     "font-size: 16px;\n"
                                     "line-height: 19px;\n"
                                     "text-align: left;\n"
                                     "color: #FFFFFF;\n"
                                     "padding: 8px 0 8px 15px;")
        self.btn_menu2.setObjectName("btn_menu2")
        self.btn_menu3 = QtWidgets.QPushButton(self.buttons)
        self.btn_menu3.setGeometry(QtCore.QRect(0, 94, 219, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu3.sizePolicy().hasHeightForWidth())
        self.btn_menu3.setSizePolicy(sizePolicy)
        self.btn_menu3.setMaximumSize(QtCore.QSize(219, 37))
        self.btn_menu3.setStyleSheet("background: #282828;\n"
                                     "border-radius: 11px;\n"
                                     "font-family: \'Inter\';\n"
                                     "font-style: normal;\n"
                                     "font-weight: 400;\n"
                                     "font-size: 16px;\n"
                                     "line-height: 19px;\n"
                                     "text-align: left;\n"
                                     "color: #FFFFFF;\n"
                                     "padding: 8px 0 8px 15px;")
        self.btn_menu3.setObjectName("btn_menu3")

        _translate = QtCore.QCoreApplication.translate
        self.btn_menu1.setText(_translate("MainWindow", "Все задачи"))
        self.btn_menu2.setText(_translate("MainWindow", "Папка 1"))
        self.btn_menu3.setText(_translate("MainWindow", "Папка 2"))

    def add_folder(self):
        print('yes')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())