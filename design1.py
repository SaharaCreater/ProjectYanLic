from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 780)
        ROW_H = 46
        V_SPACING = 10
        V_MARGIN = 14
        H_MARGIN = 16
        PANEL_H = V_MARGIN * 2 + ROW_H * 4 + V_SPACING * 3  # = 242

        MainWindow.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0284C7,
                    stop:0.5 #0EA5E9,
                    stop:1 #22D3EE);
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setSpacing(14)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(14)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # ============ Панель подписей ============
        self.label_list = QtWidgets.QFrame(self.centralwidget)
        self.label_list.setFixedHeight(PANEL_H)
        self.label_list.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 45);
                border: 1px solid rgba(255, 255, 255, 110);
                border-radius: 14px;
            }
        """)
        self.label_list.setObjectName("label_list")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.label_list)
        self.verticalLayout.setContentsMargins(H_MARGIN, V_MARGIN, H_MARGIN, V_MARGIN)
        self.verticalLayout.setSpacing(V_SPACING)
        self.verticalLayout.setObjectName("verticalLayout")

        _label_css = """
            QLabel {
                color: #FFFFFF;
                font-weight: 600;
                font-size: 13px;
                background: transparent;
                border: none;
                padding: 0;
            }
        """

        self.label = QtWidgets.QLabel(self.label_list)
        self.label.setStyleSheet(_label_css)
        self.label.setFixedHeight(ROW_H)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.label_list)
        self.label_2.setStyleSheet(_label_css)
        self.label_2.setFixedHeight(ROW_H)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.label_list)
        self.label_3.setStyleSheet(_label_css)
        self.label_3.setFixedHeight(ROW_H)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.label_list)
        self.label_4.setStyleSheet(_label_css)
        self.label_4.setFixedHeight(ROW_H)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_3.addWidget(self.label_list)

        # ============ Колонка полей ============
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, V_MARGIN, 0, V_MARGIN)
        self.verticalLayout_2.setSpacing(V_SPACING)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        _input_css = """
            QLineEdit {
                background-color: rgba(255, 255, 255, 235);
                border: 1.5px solid rgba(255, 255, 255, 255);
                border-radius: 10px;
                padding: 0 12px;
                color: #0F172A;
                font-weight: 600;
                font-size: 14px;
                selection-background-color: #FCE7F3;
                selection-color: #831843;
            }
            QLineEdit:hover {
                border: 1.5px solid rgba(236, 72, 153, 170);
            }
            QLineEdit:focus {
                border: 1.5px solid #EC4899;
                background-color: #FFFFFF;
            }
        """

        _combo_css = """
            QComboBox {
                background-color: rgba(255, 255, 255, 235);
                border: 1.5px solid rgba(255, 255, 255, 255);
                border-radius: 10px;
                padding: 0 12px;
                color: #0F172A;
                font-weight: 600;
                font-size: 14px;
            }
            QComboBox:hover {
                border: 1.5px solid rgba(236, 72, 153, 170);
            }
            QComboBox:focus, QComboBox:on {
                border: 1.5px solid #EC4899;
                background-color: #FFFFFF;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 26px;
                border: none;
                background: transparent;
            }
            QComboBox QAbstractItemView {
                background-color: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                color: #0F172A;
                padding: 4px;
                outline: none;
                selection-background-color: #FCE7F3;
                selection-color: #831843;
            }
            QComboBox QAbstractItemView::item {
                padding: 6px 10px;
                border-radius: 4px;
                min-height: 22px;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #FCE7F3;
                color: #831843;
            }
        """

        self.name_file = QtWidgets.QLineEdit(self.centralwidget)
        self.name_file.setStyleSheet(_input_css)
        self.name_file.setFixedHeight(ROW_H)
        self.name_file.setObjectName("name_file")
        self.verticalLayout_2.addWidget(self.name_file)

        self.key = QtWidgets.QLineEdit(self.centralwidget)
        self.key.setStyleSheet(_input_css)
        self.key.setFixedHeight(ROW_H)
        self.key.setObjectName("key")
        self.verticalLayout_2.addWidget(self.key)

        self.choose_shifr = QtWidgets.QComboBox(self.centralwidget)
        self.choose_shifr.setStyleSheet(_combo_css)
        self.choose_shifr.setFixedHeight(ROW_H)
        self.choose_shifr.setObjectName("choose_shifr")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.choose_shifr.addItem("")
        self.verticalLayout_2.addWidget(self.choose_shifr)

        self.choose_task = QtWidgets.QComboBox(self.centralwidget)
        self.choose_task.setStyleSheet(_combo_css)
        self.choose_task.setFixedHeight(ROW_H)
        self.choose_task.setObjectName("choose_task")
        self.choose_task.addItem("")
        self.choose_task.addItem("")
        self.verticalLayout_2.addWidget(self.choose_task)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        # ============ Главная кнопка ============
        self.main_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_button.setFixedHeight(PANEL_H)
        self.main_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #EC4899, stop:1 #A855F7);
                border: none;
                border-radius: 14px;
                color: #FFFFFF;
                font-weight: 700;
                font-size: 16px;
                padding: 0 24px;
                min-width: 150px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #F472B6, stop:1 #C084FC);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #DB2777, stop:1 #9333EA);
            }
        """)
        self.main_button.setObjectName("main_button")
        self.horizontalLayout_3.addWidget(self.main_button)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        # ============ Панель текстовых полей ============
        self.print = QtWidgets.QFrame(self.centralwidget)
        self.print.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 45);
                border: 1px solid rgba(255, 255, 255, 110);
                border-radius: 14px;
            }
        """)
        self.print.setObjectName("print")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.print)
        self.horizontalLayout.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")

        _text_css = """
            QPlainTextEdit {
                background-color: rgba(255, 255, 255, 235);
                border: 1.5px solid rgba(255, 255, 255, 255);
                border-radius: 10px;
                padding: 10px;
                color: #0F172A;
                font-weight: 500;
                font-size: 13px;
                selection-background-color: #FCE7F3;
                selection-color: #831843;
            }
            QPlainTextEdit:focus {
                border: 1.5px solid #EC4899;
                background-color: #FFFFFF;
            }
        """

        self.input_text = QtWidgets.QPlainTextEdit(self.print)
        self.input_text.setStyleSheet(_text_css)
        self.input_text.setFixedHeight(120)
        self.input_text.setObjectName("input_text")
        self.horizontalLayout.addWidget(self.input_text)

        self.output_text = QtWidgets.QPlainTextEdit(self.print)
        self.output_text.setStyleSheet(_text_css)
        self.output_text.setFixedHeight(120)
        self.output_text.setObjectName("output_text")
        self.horizontalLayout.addWidget(self.output_text)

        self.verticalLayout_3.addWidget(self.print)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        # ============ Нижняя панель ============
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.task_db = QtWidgets.QComboBox(self.centralwidget)
        self.task_db.setStyleSheet(_combo_css)
        self.task_db.setFixedHeight(ROW_H)
        self.task_db.setObjectName("task_db")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.task_db.addItem("")
        self.horizontalLayout_4.addWidget(self.task_db, 2)

        _small_btn_css = """
            QPushButton {
                background-color: rgba(255, 255, 255, 235);
                border: 1.5px solid rgba(255, 255, 255, 255);
                border-radius: 10px;
                color: #0F172A;
                font-weight: 600;
                font-size: 13px;
                padding: 0 14px;
            }
            QPushButton:hover {
                background-color: #FFFFFF;
                border: 1.5px solid #EC4899;
                color: #BE185D;
            }
            QPushButton:pressed {
                background-color: #FCE7F3;
                border: 1.5px solid #DB2777;
            }
        """

        self.show_db = QtWidgets.QPushButton(self.centralwidget)
        self.show_db.setStyleSheet(_small_btn_css)
        self.show_db.setFixedHeight(ROW_H)
        self.show_db.setObjectName("show_db")
        self.horizontalLayout_4.addWidget(self.show_db, 1)

        self.hide_button = QtWidgets.QPushButton(self.centralwidget)
        self.hide_button.setStyleSheet(_small_btn_css)
        self.hide_button.setFixedHeight(ROW_H)
        self.hide_button.setObjectName("hide_button")
        self.horizontalLayout_4.addWidget(self.hide_button, 1)

        self.delete_db = QtWidgets.QPushButton(self.centralwidget)
        self.delete_db.setStyleSheet(_small_btn_css)
        self.delete_db.setFixedHeight(ROW_H)
        self.delete_db.setObjectName("delete_db")
        self.horizontalLayout_4.addWidget(self.delete_db, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        # ============ Таблица ============
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setStyleSheet("""
            QTableView {
                background-color: #FFFFFF;
                border: 1px solid rgba(255, 255, 255, 255);
                border-radius: 12px;
                gridline-color: #E2E8F0;
                color: #0F172A;
                font-size: 12px;
                selection-background-color: #FCE7F3;
                selection-color: #831843;
                alternate-background-color: #F8FAFC;
            }
            QTableView::item {
                padding: 4px 8px;
                border: none;
            }
            QTableView::item:selected {
                background-color: #FCE7F3;
                color: #831843;
            }
            QHeaderView::section {
                background-color: #0F172A;
                color: #FFFFFF;
                font-weight: 600;
                font-size: 12px;
                padding: 8px;
                border: none;
                border-right: 1px solid rgba(255, 255, 255, 30);
            }
            QHeaderView::section:first {
                border-top-left-radius: 11px;
            }
            QHeaderView::section:last {
                border-top-right-radius: 11px;
                border-right: none;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                margin: 2px;
            }
            QScrollBar::handle:vertical {
                background: #CBD5E1;
                border-radius: 4px;
                min-height: 24px;
            }
            QScrollBar::handle:vertical:hover {
                background: #94A3B8;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar:horizontal {
                background: transparent;
                height: 8px;
                margin: 2px;
            }
            QScrollBar::handle:horizontal {
                background: #CBD5E1;
                border-radius: 4px;
                min-width: 24px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #94A3B8;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0;
            }
        """)
        self.verticalLayout_4.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("""
            QStatusBar {
                background-color: rgba(0, 0, 0, 50);
                color: rgba(255, 255, 255, 230);
                font-size: 11px;
                border-top: 1px solid rgba(255, 255, 255, 60);
                padding: 2px 8px;
            }
            QStatusBar::item {
                border: none;
            }
        """)
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