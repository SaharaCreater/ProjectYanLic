# Основной файл
import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from design1 import Ui_MainWindow
from shifr import *


class Shifrovshik(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Подключение дизайна, базы данных и подсоединение кнопок к функциям
        self.setupUi(self)
        self.main_button.clicked.connect(self.run)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('my_db.db')
        db.open()

        self.model = QSqlTableModel(self, db)
        self.model.setTable('Shifr')
        self.show_db.clicked.connect(self.db)
        self.delete_db.clicked.connect(self.delete)
        self.hide_button.clicked.connect(self.hide)
    # Функция для отображения данных из базы данных
    def db(self):
        current_task = self.task_db.currentText()
        if current_task in ['Расшифровано', 'Зашифровано']:
            self.model.setFilter(f"task = '{current_task}'")
        elif current_task == 'Все записи':
            self.model.setFilter("")
        else:
            self.model.setFilter(f"name_shifr = '{current_task}'")
        self.model.select()
        self.tableView.setModel(self.model)
    # Функция для удаления данных из базы данных
    def delete(self):
        con = sqlite3.connect("my_db.db")
        cur = con.cursor()
        current_task = self.task_db.currentText()
        if current_task in ['Расшифровано', 'Зашифровано']:
            cur.execute(f"""DELETE FROM Shifr
                            WHERE ? = task""", (current_task, ))
        elif current_task == 'Все записи':
            cur.execute(f"""DELETE FROM Shifr""")
        else:
            cur.execute(f"""DELETE FROM Shifr
                            WHERE ? = name_shifr""", (current_task, ))
        con.commit()
        con.close()
    # Функция для добавления данных в базу данных
    def insert_db(self, key):
        con = sqlite3.connect("my_db.db")
        cur = con.cursor()
        if key:
            cur.execute("""INSERT INTO Shifr (name_shifr, task, key, start_file) VALUES (?, ?, ?, ?)""",
                        (self.choose_shifr.currentText(),
                         self.choose_task.currentText()[:-2] + 'но',
                         key,
                         self.name_file.text()))
        else:
            cur.execute("""INSERT INTO Shifr (name_shifr, task, key, start_file) VALUES (?, ?, ?, ?)""",
                        (self.choose_shifr.currentText(),
                         self.choose_task.currentText()[:-2] + 'но',
                         '0',
                         self.name_file.text()))
        con.commit()
        con.close()
    # Функция для скрытия базы данных
    def hide(self):
        self.tableView.setModel(None)
    # Основная функция. Здесь происходит шифровка и дешифровка сообщений
    def run(self):
        self.statusbar.showMessage('')
        if self.choose_shifr.currentText() == 'Шифр Атбаш':
            if not self.name_file.text():
                self.output_text.insertPlainText(func_ashbat(self.input_text.toPlainText()))
                self.statusbar.showMessage('OK')
            else:
                if func_ashbat('', self.name_file.text()) == 'OK':
                    self.statusbar.showMessage('Файл обработан корректно')
                    self.insert_db('-')
                else:
                    self.statusbar.showMessage('Файл не найден')
        elif self.choose_shifr.currentText() == 'Шифр Цезаря':
            if not self.name_file.text():
                if func_zesar(self.input_text.toPlainText(), self.key.text(),
                              self.choose_task.currentText()) != 'Error':
                    self.output_text.insertPlainText(func_zesar(self.input_text.toPlainText(),
                                                                self.key.text(),
                                                                self.choose_task.currentText()))
                    self.statusbar.showMessage('OK')
                else:
                    self.statusbar.showMessage('Некорректные входные данные: ключом должно быть целое число')
            else:
                per = func_zesar('', self.key.text(), self.choose_task.currentText(), self.name_file.text())
                if per == 'OK':
                    self.statusbar.showMessage('Файл обработан корректно')
                    self.insert_db(self.key.text())
                elif per == 'Error':
                    self.statusbar.showMessage('Некорректные входные данные: ключом должно быть целое число')
                else:
                    self.statusbar.showMessage('Файл не найден')
        elif self.choose_shifr.currentText() == 'Азбука Морзе':
            if not self.name_file.text():
                if func_morse(self.input_text.toPlainText(), self.choose_task.currentText(),
                              self.key.text()) != 'Error':
                    self.output_text.insertPlainText(func_morse(self.input_text.toPlainText(),
                                                     self.choose_task.currentText(),
                                                     self.key.text()))
                    self.statusbar.showMessage('OK')
                else:
                    self.statusbar.showMessage('Некорректные входные данные: ключом может быть только "RU" или "EN"')
            else:
                per = func_morse('', self.choose_task.currentText(), self.key.text(), self.name_file.text())
                if per == 'OK':
                    self.statusbar.showMessage('Файл обработан корректно')
                    self.insert_db(self.key.text())
                elif per == 'Error':
                    self.statusbar.showMessage('Некорректные входные данные: ключом может быть только "RU" или "EN"')
                else:
                    self.statusbar.showMessage('Файл не найден')
        elif self.choose_shifr.currentText() == 'Шифр Вернама':
            if not self.name_file.text():
                if func_vernama(self.input_text.toPlainText(), self.choose_task.currentText(),
                                self.key.text()) != 'Error':
                    self.output_text.insertPlainText(func_vernama(self.input_text.toPlainText(),
                                                                  self.choose_task.currentText(),
                                                                  self.key.text()))
                    self.statusbar.showMessage('OK')
                else:
                    self.statusbar.showMessage('Некорректные входные данные: ключом должно быть слово')
            else:
                per = func_vernama('',  self.choose_task.currentText(), self.key.text(),
                                    self.name_file.text())
                if per == 'OK':
                    self.statusbar.showMessage('Файл обработан корректно')
                    self.insert_db(self.key.text())
                elif per == 'Error':
                    self.statusbar.showMessage('Некорректные входные данные: ключом должно быть слово')
                else:
                    self.statusbar.showMessage('Файл не найден')
        elif self.choose_shifr.currentText() == 'Шифр Виженера':
            if not self.name_file.text():
                if func_vizenera(self.input_text.toPlainText(),
                                 self.choose_task.currentText(), self.key.text()) != 'Error':
                    self.output_text.insertPlainText(func_vizenera(self.input_text.toPlainText(),
                                                               self.choose_task.currentText(), self.key.text()))
                    self.statusbar.showMessage('OK')
                else:
                    self.statusbar.showMessage('Ключ не должен быть пустым')
            else:
                per = func_vizenera('', self.choose_task.currentText(), self.key.text(),
                                    self.name_file.text())
                if per == 'OK':
                    self.statusbar.showMessage('Файл обработан корректно')
                    self.insert_db(self.key.text())
                elif per == 'Error':
                    self.statusbar.showMessage('Ключ не должен быть пустым')
                else:
                    self.statusbar.showMessage('Файл не найден')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Shifrovshik()
    ex.show()
    sys.exit(app.exec())