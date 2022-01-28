import sys
from PyQt5.QtWidgets import QMainWindow
from change import Ui_MainWindow
from functools import partial
from PyQt5 import QtWidgets

def convert(ui):
    input = ui.lineEdit_2.text()
    result = float(input)*6.7
    ui.lineEdit_2.setText(str(result))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(partial(convert,ui))
    sys.exit(app.exec_())