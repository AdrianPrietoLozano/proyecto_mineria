from dialogo_elegir_propiedades_ui import *
from ventana_base_datos import VentanaBaseDatos
from main_window import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QDir
import mysql.connector
import json
import os

class DialogoElegirPropiedades(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.botonAceptar.clicked.connect(self.cargar_datos)
        self.botonCancelar.clicked.connect(self.cerrar_programa)
        self.elegir_archivo.clicked.connect(self.pedir_archivo)

        self.lineEditRuta.setText("adult_propiedades.json") # se carga por defecto

    def pedir_archivo(self):
        file, _ = QFileDialog.getOpenFileName(self, "Selecciona un archivo", QDir.homePath(), "All Files (*)");
        self.lineEditRuta.setText(file)

    def cargar_datos(self):
        if self.lineEditRuta.text() == "":
            pass
        else:
            ruta_propiedades = self.lineEditRuta.text()

            if not os.path.isfile(ruta_propiedades): # si no existe el archivo json muestra un error
                QMessageBox.critical(self, "Error", "No existe el archivo")
                return

            with open(ruta_propiedades) as contenido: # cargar archivo de propiedades
                data = json.load(contenido)
                contenido.close()

            path_csv = data.get("path_csv", None)
            if path_csv != None: # si esta definido el csv
                if os.path.isfile(path_csv): # comprueba que el csv exista
                    self.mostrar_main_window()

                else: # si no existe el csv
                    QMessageBox.critical(self, "Error", "No existe el archivo csv")

            elif data.get("datos_conexion", False): # comprueba que este definido una conexion a base de datos
                conexion = self.intentar_conectarse_bd(data["datos_conexion"])
                if conexion != None: # si se pudo conectar
                    self.mostrar_ventana_base_datos(conexion)
                else:
                    QMessageBox.critical(self, "Error", "No fue posible conectarse a la base de datos")
            else:
                QMessageBox.critical(self, "Error", "No esta definido el csv ni una conexion a base de datos")

    def mostrar_main_window(self):
        """Cierra esta ventana y muestra la principal"""
        self.close()
        self.main = MainWindow(self.lineEditRuta.text())
        self.main.show()

    def mostrar_ventana_base_datos(self, conexion):
        """Cierra esta ventana y muestra la ventana de base de datos para ejecutar query"""
        self.close()
        self.ventana = VentanaBaseDatos(conexion, self.lineEditRuta.text())
        self.ventana.show()

    def intentar_conectarse_bd(self, datos_conexion):
        """Intenta conectarse a la base de datos"""
        usuario = datos_conexion.get("usuario", None)
        contrasenia = datos_conexion.get("contrasenia", None)
        base_datos = datos_conexion.get("base_datos", None)
        host = datos_conexion.get("host", None)

        try:
            return mysql.connector.connect(user=usuario,
                password=contrasenia,
                database=base_datos,
                host=host)
        except:
            return None

    def cerrar_programa(self):
        self.close()



        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dialogo = DialgoElegirPropiedades()
    dialogo.show()
    app.exec_()