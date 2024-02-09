import PyQt5, sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    main = Window()
    main.show()
    app.exec()
    sys.exit()