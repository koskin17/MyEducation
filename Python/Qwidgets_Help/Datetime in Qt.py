from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

"""
Даты находятся в модуле QtCore.
Основной объект или класс - QDate.
Конструктор для работы с датой - QDate(YYYY, MM, DD), а также есть методы:
    - addDays() - добавление дней к объекту Qdate;
    - addMonths() - добавление месяцев к объекту Qdate;
    - toJulianDay() - дата в формате юлианского календаря;
    - dayOfWeek() - возвращает день недели (номер дня);
    - dayOfYear() - какой по счету день в году;
    - toString() - возврат даты в формате строки
    
    Вся информация в документации https://doc.qt.io/qt-6/qdate.html
    
- Конструктор для работы со временем - QTime:
    - конструктор QTime(HH, MM, SS, ms)
    - методы:
        - addSeconds() - добавить секунды ко времени;
        - secsToQTime(QTime) - секунды до объекта QTime;
        - toString() - возврат времени в формате строки

Для выяснения времени в разных поясах - QTimeZone.
Если создаётся объект QTimeZone, то нужно указывать сдвиг по времени в секундах QTimeZone(seconds)

QDateTime(QDate, QTime) - при передачи QTime передаётся тайм-зона компьютера.
Если надо передать другую, то используется параметр QTimeZone - QDateTime(QDate, QTime, QTimeZone)
Методы для QDateTime:
    - addSecs() - если происходит переход через сутки, то в этом методе для QDateTime дата изменится на следующую;
        В объекте QTime при добавлении секунд при переходе через 60 они просто обнуляются и отображается остаток. 
    - secsTo();
    - daysTo();
    - toString();
    - toSecsSinceEpoch()
    
    Остальное в документации    
"""


class DlgMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton("Dates ", self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        dt = QDate.currentDate()
        print(dt)
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfWeek())
        print(dt.dayOfYear())
        print(dt.dayOfYear())
        print(dt.addDays(21).toString())

        tm = QTime(13, 20)
        print(tm.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DlgMain()
    main_window.show()
    sys.exit(app.exec_())
