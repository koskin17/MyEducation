from PyQt5.QtWidgets import *
import sys

""" Methods
# Получение текста
QInputDialog.getText(parent_window, 'Title(Заголовок окна)', 'Prompt (Строка)', text = 'Default')

# Получение целых чисел
QInputDialog.getInt(parent_window, 'Title(Заголовок окна)', 'Prompt (Строка)', iDef, iMin, iMax, iStep)

# Получение вещественных чисел. dDigits - количество цифр после десятичной точки
QInputDialog.getDouble(parent_window, 'Title(Заголовок окна)', 'Prompt (Строка)', dDef, dMin, dMax, dDigits)

# Также можно получать значения из списка.
# editable(редактируемый) - означает возможность изменять именно список, не его значения.
# Т.е. в список можно добавить новые значения.
# QInputDialog возвращает tuple - (val, status).
# val - это введенное числа
# status - bool-значение в зависимости от того, что кликнул пользователь:
# True - "OK" = True;
# False - "Cancel" = False
# Результат можно присвоить переменной и потом по индексу обращаться к значениям: res = QInputDialog.getItem()
# res1 = res[0], res2 = res[1]
# Или же сразу разнести полученный результат по переменным: res1, res2 = QInputDialog.getItem()
sList = ["item1", "item2", "item3"]
editable по умолчанию = True, т.е. для неизменяемого списка нужно писать editable=False
QInputDialog.getItem(parent_window, 'Title(Заголовок окна)', 'Prompt (Строка)', sList, editable=False)
"""


class DlgMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton("Show input", self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # name, ok = QInputDialog.getText(self, "Test Title", "Enter Your name: ")
        # print(name, ok)
        # # получаем ('Костя', True) или ('', False)
        # if ok:
        #     QMessageBox.information(self, "Name", "Your name is " + name)
        # else:
        #     QMessageBox.critical(self, "Canceled", "User has clicked \"Cancel\"")

        # Получение числа от пользователя
        # age, ok = QInputDialog.getInt(self, "Test Title", "Enter Your age: ", 18, 18, 65, 1)
        # if ok:
        #     QMessageBox.information(self, "Age", "Your age is " + str(age))
        # else:
        #     QMessageBox.critical(self, "Canceled", "User has clicked \"Cancel\"")

        # Получение значения из списка
        colors = ["red", "orange", "yellow", "green", "blue"]
        res1, res2 = QInputDialog.getItem(self, "Color", "Enter Your favorite color: ", colors)
        print(res1, res2)
        if res1:
            QMessageBox.information(self, "Color", "Your favorite color is: " + res1)
        else:
            QMessageBox.critical(self, "Canceled", "User has clicked \"Cancel\"")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DlgMain()
    main_window.show()
    sys.exit(app.exec_())
