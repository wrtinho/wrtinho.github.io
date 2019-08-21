from Cadastro_ui import *
from Inicial_ui import *
import sys

class CadastroWindow(QtWidgets.QMainWindow, Ui_CadastroWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

class InicialWindow(QtWidgets.QMainWindow, Ui_InicialWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = loginWindow()
    window.show()
    app.exec_()

