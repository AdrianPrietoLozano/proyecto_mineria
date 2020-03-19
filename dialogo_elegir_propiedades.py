from dialogo_elegir_propiedades_ui import *
from main_window import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt, QDir

class DialogoElegirPropiedades(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.botonAceptar.clicked.connect(self.cargar_datos)
        self.botonCancelar.clicked.connect(self.cerrar_programa)
        self.elegir_archivo.clicked.connect(self.pedir_archivo)

        self.lineEditRuta.setText("adult_propiedades.json")

    def pedir_archivo(self):
        file, _ = QFileDialog.getOpenFileName(self, "Selecciona un archivo", QDir.homePath(), "All Files (*)")
        self.lineEditRuta.setText(file)

    def cargar_datos(self):
        if not self.lineEditRuta.text:
            pass
        else:
            self.close()
            self.main = MainWindow(self.lineEditRuta.text())
            self.main.show()

    def cerrar_programa(self):
        pass


"""
# ---        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dialogo = DialgoElegirPropiedades()
    dialogo.show()
    app.exec_()
"""