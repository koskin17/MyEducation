"""Method QMessageBox for use in future.
May to use warning, information, critical, question
May set buttons: button1 | button 2 | button 3 and buttonDefault
May use buttons: QMessageBox.Cancel, QMessageBox.Ok, QMessageBox.Yes and QMessageBox.No

1 Method for make QMessageBox:
    result = QMessageBox.warning(parent, 'Title', 'Message')

2 Method for make QMessageBox:
    - создать объект класса QMessageBox()
    msgDiskFull = QMessageBox()

    вызывать методы класса:
    msgDiskFull.setText("Диск полный")
    msgDiskFull.setDetailedText("Освободите место")
    msgDiskFull.setIcon(QMessageBox.information)
    msgDiskFull.setWindowTitle("Заголовок окна")
    msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgDiskFull.exec_()"""