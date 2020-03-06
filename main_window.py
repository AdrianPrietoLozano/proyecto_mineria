from main_window_ui import *
from dialogo_elegir_propiedades import *
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtCore import Qt, QDir
import pandas as pd
from conjunto_datos import ConjuntoDatos

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ruta, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.ruta = ruta
        self.conjunto = ConjuntoDatos(self.ruta)
        self.llenar_tabla()

        self.llenar_combo_boxes()
        self.mostrar_atributo_numerico()
        self.mostrar_atributo_categorico()


    def llenar_tabla(self):
        """Muestra los datos del csv en una tabla"""
        self.tabla.setColumnCount(self.conjunto.getNumAtributos())
        self.tabla.setHorizontalHeaderLabels(self.conjunto.getNombresAtributos())

        self.tabla.setRowCount(0)
        for index, row in self.conjunto.panda.iterrows():
            self.tabla.insertRow(index)
            for i in range(len(row)):
                self.tabla.setItem(index, i, QTableWidgetItem(str(row[i])))

    def llenar_combo_boxes(self):
        """Llena los combo box con los nombres de los atributos separados por tipo"""
        for atributo in self.conjunto.getAtributos():
            if atributo.getTipo() == "numerico":
                self.comboBoxNumericos.addItem(atributo.getNombre())
            elif atributo.getTipo() == "categorico":
                self.comboBoxCategoricos.addItem(atributo.getNombre())

    def mostrar_atributo_numerico(self):
        """"Muestra los datos del atributo numerico actual que esta en el combo box"""
        nombre_atributo = self.comboBoxNumericos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)
        self.nombreAtributoNumerico.setText(atributo.getNombre())
        self.tipoAtributoNumerico.setText(atributo.getTipo())
        self.dominioAtributoNumerico.setText(atributo.getDominio())

    def mostrar_atributo_categorico(self):
        """Muestra los datos del atributo categorico actual que esta en el combo box"""
        nombre_atributo = self.comboBoxNumericos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)
        self.nombreAtributoCate.setText(atributo.getNombre())
        self.tipoAtributoCate.setText(atributo.getTipo())
        self.dominioAtributoCate.setText(atributo.getDominio())

        #Categóricos


        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()