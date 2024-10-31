'''
Создание окон процедурными методами
'''

##import sys
##from PyQt5.QtWidgets import *
##
##app = QApplication(sys.argv)    # creat application
##dlgMain = QWidget()             # creat main GUI window 
##dlgMain.setWindowTitle("Fistr GUI")
##dlgMain.show()                  # show the GUI
##
##dlgMain2 = QDialog()
##dlgMain2.show()
##
##dlgMain3 = QMainWindow()
##dlgMain3.show()
##
##sys.exit(app.exec_())           # execute the app

'''
Создание окон методами ООП
'''
import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):             # создание класса,
                                    # наследованного от QDialog
    def __init__(self):
        super().__init__()          # при помощи метода супер вызывается метод-конструктор родительского класса
        self.setWindowTitle("Second GUI")   # add widgets and set propetries
        self.resize(300, 200)               # установка размера окна
        '''
        Для создания виджета создаётся переменная,
        которая будет хранить этот виджет
        '''
        self.ledText = QLineEdit("Default Text", self)  # led означает line edit или редактирумая строка
        self.ledText.move(90, 50)          # передвижение виджета в окне от левого верхнего угла

        self.btnUpdate = QPushButton("Update Window Title", self)
        self.btnUpdate.move(90, 80)

        self.btnUpdate.clicked.connect(self.evt_btnupdate_clicked)

    def evt_btnupdate_clicked(self):
        self.setWindowTitle(self.ledText.text())    # методом text получаем текст, который находится в этом виджете

if __name__ == '__main__':
    app = QApplication(sys.argv)    # create application
    dlgMain = DlgMain()             # create main GUI window
    dlgMain.show()                  # show GUI
    sys.exit(app.exec_())           # execute the application
