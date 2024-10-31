from typing import List

from PyQt5.QtWidgets import *
import sys

"""Methods
# directory передаётся в формате "строка" - директория по умолчанию, которая будет отображаться в диалоговом окне
# types - указываются типы файлов, которые хотим "видеть" в диалогово окне. При этом:
# при указании типов файлов обязательно должна быть структура: "Название файлов (*.расширение)"
QFileDialog.getOpenFileName(parent_windows, 'Title', directory, types)
# Если нужно отображать несколько типов файлов, то строки с типом файлов разделяются при помощи ";;":
# "Excel files (*.xlsx);;Word files (*.doc)"

# Метод добавления нового файла, которого не существует.
QFileDialog.getSaveFileName(paren_window, 'Title', directory, types)

# Открытие нескольких файлов - возвращается массив из имён файлов
Возвращается список из путей и имён открытых файлов
QFileDialog.getOpenFileNames(parent_window, 'Title', directory, types)
"""


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton("Open file", self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # Открытие одного файла
        # Возвращается tuple с:
        # - элемент [0] - путь к файлу, который выбрали для открытия;
        # - элемент [1] - описание файла с расширением, то в таком виде, в каком мы указали "*.xlsx"
        res = QFileDialog.getOpenFileName(self, 'Open file', 'C:/', '*.xlsx;;*.xls')
        print(res[0])
        # Метод сохранения файла.
        # res = QFileDialog.getSaveFileName(self, 'Open file', 'C:/', '*.xlsx;;*.xls')
        # print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DlgMain()
    main_window.show()
    sys.exit(app.exec_())
