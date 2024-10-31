from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

""" КонструкторыЖ
- QFont('Arial', 18) - задать имя шрифта и размер;
- QFont('Arial', 18, 81, True) - помимо имени и размера можно задать вес (жирный шрифт) и курсив (True или False)
    Все необходимые значения есть в документации https://doc.qt.io/qt-6/qfont.html
    по ссылке https://doc.qt.io/qt-6/qfont.html#Weight-enum;
- QFont() - создать пустой объект и установить свойства сеттерами setFamily(), setWeight(), setPointSize() и т.д.

Есть метод QFontDialog.getFont(), который возвращает tuple (объект класса QFont, True или False, что нажал пользователь)
Если необходимо установить шрифт для виджта без участия пользователя, то:
    - создаётся объект и помещается в переменную;
    - указывается имя семейства шрифта, размер, "жирность" или вес и курсив ли
    
"""


class DlgMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton("Choose font: ", self)
        self.btn.move(35, 50)
        font = QFont('Arial', 8, 75, True)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        font, b_ok = QFontDialog.getFont()
        print(font, b_ok)
        if bOK:
            print(font.family())  # получаем семейство шрифта из объекта класса QFont
            print(font.italic())  # узнает, курсив ли (True или False)
            print(font.bold())  # узнает, жирный ли
            print(font.weight())
            print(font.pointSize())
            # устанавливаем выбранный шрифт на кнопку
            self.btn.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DlgMain()
    main_window.show()
    sys.exit(app.exec_())
