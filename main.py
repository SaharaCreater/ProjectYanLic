import os
import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from design1 import Ui_MainWindow
from shifr import *


class Shifrovshik(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_button.clicked.connect(self.run)

        self.qdb = QSqlDatabase.addDatabase('QSQLITE')
        self.qdb.setDatabaseName('my_db.db')
        self.qdb.open()

        self.model = QSqlTableModel(self, self.qdb)
        self.model.setTable('Shifr')

        self.show_db.clicked.connect(self.db)
        self.delete_db.clicked.connect(self.delete)
        self.hide_button.clicked.connect(self.hide)

    def db(self):
        current = self.task_db.currentText()
        if current == 'Все записи':
            self.model.setFilter('')
        elif current in ('Расшифровано', 'Зашифровано'):
            self.model.setFilter(f"task = '{current}'")
        else:
            self.model.setFilter(f"name_shifr = '{current}'")
        self.model.select()
        self.tableView.setModel(self.model)

    def _refresh_if_visible(self):
        if self.tableView.model() is not None:
            self.model.select()

    def delete(self):
        current = self.task_db.currentText()
        with sqlite3.connect('my_db.db') as con:
            cur = con.cursor()
            if current == 'Все записи':
                cur.execute('DELETE FROM Shifr')
            elif current in ('Расшифровано', 'Зашифровано'):
                cur.execute('DELETE FROM Shifr WHERE task = ?', (current,))
            else:
                cur.execute('DELETE FROM Shifr WHERE name_shifr = ?', (current,))
            con.commit()
        self._refresh_if_visible()

    def insert_db(self, key):
        task = ('Зашифровано' if self.choose_task.currentText() == 'Зашифровать'
                else 'Расшифровано')
        with sqlite3.connect('my_db.db') as con:
            cur = con.cursor()
            cur.execute(
                'INSERT INTO Shifr (name_shifr, task, key, start_file) VALUES (?, ?, ?, ?)',
                (self.choose_shifr.currentText(), task, key or '0',
                 self.name_file.text())
            )
            con.commit()
        self._refresh_if_visible()

    def hide(self):
        self.tableView.setModel(None)

    def run(self):
        self.statusbar.showMessage('')

        shifr = self.choose_shifr.currentText()
        task = self.choose_task.currentText()
        key = self.key.text().strip()
        text = self.input_text.toPlainText()
        name_file = self.name_file.text().strip() or None

        if name_file and not os.path.isfile(name_file):
            self.statusbar.showMessage('Файл не найден')
            return

        try:
            if shifr == 'Шифр Атбаш':
                result = func_ashbat(text, name_file)
                db_key = '-'
                err = 'Ошибка обработки файла'
            elif shifr == 'Шифр Цезаря':
                result = func_zesar(text, key, task, name_file)
                db_key = key
                err = 'Некорректные входные данные: ключом должно быть целое число'
            elif shifr == 'Азбука Морзе':
                result = func_morse(text, task, key, name_file)
                db_key = key
                err = 'Некорректные входные данные: ключом может быть только "RU" или "EN"'
            elif shifr == 'Шифр Виженера':
                result = func_vizenera(text, task, key, name_file)
                db_key = key
                err = 'Ключ не должен быть пустым или не совпадать с алфавитом'
            elif shifr == 'Шифр Вернама':
                result = func_vernama(text, task, key, name_file)
                db_key = key
                err = 'Некорректные входные данные: ключом должно быть слово'
            else:
                return
        except Exception as e:
            self.statusbar.showMessage(f'Ошибка: {e}')
            return

        if result == 'OK':
            self.statusbar.showMessage('Файл обработан корректно')
            self.insert_db(db_key)
        elif result == 'Error':
            self.statusbar.showMessage(err)
        else:
            self.output_text.setPlainText(result)
            self.statusbar.showMessage('OK')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Shifrovshik()
    ex.show()
    sys.exit(app.exec())