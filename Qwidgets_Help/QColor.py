from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

""" Конструкторы для цветовой схемы RGB:
- QColor(#3af5d1):
    - 3a - числа интенсивности красного цвета
    - f5 - числа интенсивности зелёного цвета
    - d1 - числа интенсивности синего цвета.
- QColor(120, 214, 37) - аналогично, только в десятеричной системе исчисления
- QColor(120, 214, 37, 125) - последнее число - альфа значение или прозрачность цвета
- QColor("khaki") - можно передать название цвета
- создать объект QColor() без параметров. Его значение будет Nan и потом назначить цвета через сеттеры:
    setRed(97), setGreen(225) и т.д.
    Также можно получить значения у созданного объекта через методы геттеры:
    - red() - получаем значение красного;
    - green() - получаем значение зелёного;
    - blue() - получаем значение синего;
    - alpha() - получает значение прозрачности;
    - name() - получаем название цвета.
    
Если нужно, чтобы пользователь выбрал цвет, то есть метод QColorDialog.getColor(QColor, parent, 'Title'):
    - QColor - default цвет, который будет отображаться при открытии диалога выбора цвета;
"""


class DlgMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton("Choose color: ", self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        color = QColorDialog.getColor(QColor('red'), self, 'Choose color')
        print(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DlgMain()
    main_window.show()
    sys.exit(app.exec_())
