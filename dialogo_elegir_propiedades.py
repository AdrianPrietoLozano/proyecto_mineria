from dialogo_elegir_propiedades_ui import *
from ventana_base_datos import VentanaBaseDatos
from main_window import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt, QDir
import json

class DialogoElegirPropiedades(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.botonAceptar.clicked.connect(self.cargar_datos)
        self.botonCancelar.clicked.connect(self.cerrar_programa)
        self.elegir_archivo.clicked.connect(self.pedir_archivo)

        self.lineEditRuta.setText("adult_propiedades.json")

    def pedir_archivo(self):
        file, _ = QFileDialog.getOpenFileName(self, "Selecciona un archivo", QDir.homePath(), "All Files (*)");
        self.lineEditRuta.setText(file)

    def cargar_datos(self):
        if self.lineEditRuta.text() == "":
            pass
        else:

            datos_conexion = self.get_datos_conexion_bd()
            if datos_conexion != None and datos_conexion != "": # si se definieron datos de conexion
                self.close()
                self.ventana = VentanaBaseDatos(datos_conexion, self.lineEditRuta.text())
                self.ventana.show()
                
            else: # inicia normalmente con archivo csv
                self.close()
                self.main = MainWindow(self.lineEditRuta.text())
                self.main.show()

    def get_datos_conexion_bd(self):
        with open(self.lineEditRuta.text()) as contenido:
            data = json.load(contenido)

            datos_conexion = data.get("datos_conexion", None)

            contenido.close()

        return datos_conexion

    def cerrar_programa(self):
        pass



        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dialogo = DialgoElegirPropiedades()
    dialogo.show()
    app.exec_()