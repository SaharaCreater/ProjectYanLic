# Дизайн моего проекта
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 698)
        MainWindow.setStyleSheet("background-color: qlineargradient(\n"
"    x1: 0, y1: 0, \n"
"    x2: 1, y2: 1,\n"
"    stop: 0 #00BFFF, \n"
"    stop: 1 #87CEEB\n"
");")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(765, 680))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_list = QtWidgets.QFrame(self.centralwidget)
        self.label_list.setStyleSheet("background-color: rgba(255, 0, 100, 80);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.label_list.setObjectName("label_list")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.label_list)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.label_list)
        self.label.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.label_list)
        self.label_2.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.label_list)
        self.label_3.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.label_list)
        self.label_4.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3.addWidget(self.label_list)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_file = QtWidgets.QLineEdit(self.centralwidget)
        self.name_file.setStyleSheet("background-color: rgba(255, 0, 100, 80);\n"
"border: 5px solid rgba(255, 0, 100, 40);\n"
"border-radius: 7px;\n"
"height: 25 px;\n"
"width: 295;\n"
"font-weight: bold;\n"
"color: white;\n"
"font-size: 15 pt")
        self.name_file.setObjectName("name_file")
        self.verticalLayout_2.addWidget(self.name_file)
        self.key = QtWidgets.QLineEdit(self.centralwidget)
        self.key.setStyleSheet("background-color: rgba(255, 0, 100, 80);\n"
"border: 5px solid rgba(255, 0, 100, 40);\n"
"border-radius: 7px;\n"
"height: 25 px;\n"
"width: 295;\n"
"font-weight: bold;\n"
"color: white;\n"
"font-size: 15 pt")
        self.key.setObjectName("key")
        self.verticalLayout_2.addWidget(self.key)
        self.choose_shifr = QtWidgets.QComboBox(self.centralwidget)
        self.choose_shifr.setStyleSheet("background-color: rgba(255, 0, 100, 80);\n"
"border: 5px solid rgba(255, 0, 100, 40);\n"
"border-radius: 7px;\n"
"height: 25 px;\n"
"width: 295;\n"
"font-weight: bold;\n"
"color: white;\n"
"font-size: 15 pt")
        self.choose_shifr.setObjectName("choose_shifr")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.verticalLayout_2.addWidget(self.choose_shifr)
        self.choose_task = QtWidgets.QComboBox(self.centralwidget)
        self.choose_task.setStyleSheet("background-color: rgba(255, 0, 100, 80);\n"
"border: 5px solid rgba(255, 0, 100, 40);\n"
"border-radius: 7px;\n"
"height: 25 px;\n"
"width: 295;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 25 pt;")
        self.choose_task.setObjectName("choose_task")
        self.choose_task.addItem("")
        self.choose_task.addItem("")
        self.verticalLayout_2.addWidget(self.choose_task)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.main_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_button.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 0, 100, 80);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"height: 161;\n"
"width: 200;\n"
"font-size: 16px;\n"
"widht: 202\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 0, 100, 90);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 0, 100, 100);\n"
"}\n"
"")
        self.main_button.setObjectName("main_button")
        self.horizontalLayout_3.addWidget(self.main_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.print = QtWidgets.QFrame(self.centralwidget)
        self.print.setStyleSheet("background-color: rgba(255, 0, 100, 80);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.print.setObjectName("print")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.print)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_text = QtWidgets.QPlainTextEdit(self.print)
        self.input_text.setStyleSheet("background-color: rgba(255, 0, 100, 3);\n"
"height: 81;\n"
"width: 359;\n"
"font-weight: bold;\n"
"font-size: 15 pt;\n"
"color: white")
        self.input_text.setObjectName("input_text")
        self.horizontalLayout.addWidget(self.input_text)
        self.output_text = QtWidgets.QPlainTextEdit(self.print)
        self.output_text.setStyleSheet("background-color: rgba(255, 0, 100, 3);\n"
"height: 81;\n"
"width: 359;\n"
"font-weight: bold;\n"
"font-size: 15 pt;\n"
"color: white")
        self.output_text.setObjectName("output_text")
        self.horizontalLayout.addWidget(self.output_text)
        self.verticalLayout_3.addWidget(self.print)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.task_db = QtWidgets.QComboBox(self.centralwidget)
        self.task_db.setStyleSheet("background-color: rgba(255, 0, 100, 80);\n"
"border: 5px solid rgba(255, 0, 100, 40);\n"
"border-radius: 7px;\n"
"height: 25 px;\n"
"width: 205;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 25 pt;")
        self.task_db.setObjectName("task_db")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.horizontalLayout_4.addWidget(self.task_db)
        self.show_db = QtWidgets.QPushButton(self.centralwidget)
        self.show_db.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 0, 100, 80);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"height: 31;\n"
"width: 200;\n"
"font-size: 16px;\n"
"widht: 202\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 0, 100, 90);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 0, 100, 100);\n"
"}\n"
"")
        self.show_db.setObjectName("show_db")
        self.horizontalLayout_4.addWidget(self.show_db)
        self.hide_button = QtWidgets.QPushButton(self.centralwidget)
        self.hide_button.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 0, 100, 80);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"height: 31;\n"
"width: 200;\n"
"font-size: 16px;\n"
"widht: 202\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 0, 100, 90);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 0, 100, 100);\n"
"}")
        self.hide_button.setObjectName("hide_button")
        self.horizontalLayout_4.addWidget(self.hide_button)
        self.delete_db = QtWidgets.QPushButton(self.centralwidget)
        self.delete_db.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 0, 100, 80);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"height: 31;\n"
"width: 200;\n"
"font-size: 16px;\n"
"widht: 202\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 0, 100, 90);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 0, 100, 100);\n"
"}\n"
"")
        self.delete_db.setObjectName("delete_db")
        self.horizontalLayout_4.addWidget(self.delete_db)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setStyleSheet("background-color: white;")
        self.verticalLayout_4.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "шифровщик"))
        self.label.setText(_translate("MainWindow", "Введите название файла"))
        self.label_2.setText(_translate("MainWindow", "Введите ключ"))
        self.label_3.setText(_translate("MainWindow", "Выбирете шифр"))
        self.label_4.setText(_translate("MainWindow", "Выбирете действие"))
        self.choose_shifr.setItemText(0, _translate("MainWindow", "Шифр Цезаря"))
        self.choose_shifr.setItemText(1, _translate("MainWindow", "Шифр Виженера"))
        self.choose_shifr.setItemText(2, _translate("MainWindow", "Шифр Атбаш"))
        self.choose_shifr.setItemText(3, _translate("MainWindow", "Шифр Вернама"))
        self.choose_shifr.setItemText(4, _translate("MainWindow", "Азбука Морзе"))
        self.choose_task.setItemText(0, _translate("MainWindow", "Расшифровать"))
        self.choose_task.setItemText(1, _translate("MainWindow", "Зашифровать"))
        self.main_button.setText(_translate("MainWindow", "PushButton"))
        self.task_db.setItemText(0, _translate("MainWindow", "Все записи"))
        self.task_db.setItemText(1, _translate("MainWindow", "Расшифровано"))
        self.task_db.setItemText(2, _translate("MainWindow", "Зашифровано"))
        self.task_db.setItemText(3, _translate("MainWindow", "Шифр Атбаш"))
        self.task_db.setItemText(4, _translate("MainWindow", "Шифр Цезаря"))
        self.task_db.setItemText(5, _translate("MainWindow", "Шифр Вернама"))
        self.task_db.setItemText(6, _translate("MainWindow", "Шифр Виженера"))
        self.task_db.setItemText(7, _translate("MainWindow", "Азбука Морзе"))
        self.show_db.setText(_translate("MainWindow", "Показать записи из БД"))
        self.hide_button.setText(_translate("MainWindow", "Скрыть записи из БД"))
        self.delete_db.setText(_translate("MainWindow", "Удалить записи из БД"))
