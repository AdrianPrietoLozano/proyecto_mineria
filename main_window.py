from main_window_ui import *
from dialogo_elegir_propiedades import *
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, QDir, QItemSelectionModel, QSize
from PyQt5.QtGui import QIcon
import pandas as pd
from conjunto_datos import ConjuntoDatos
from table_model_pandas import TableModelPandas

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    NUMERICO = 1
    CATEGORICO = 2

    def __init__(self, ruta, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.ruta = ruta
        self.conjunto = ConjuntoDatos(self.ruta)

        # utilizando un modelo los datos en la tabla se cargan muchisimo más rápido
        self.model = TableModelPandas(self.conjunto.panda)
        self.tabla.setModel(self.model)        

        self.llenar_combo_box()
        self.mostrar_atributo() # muestra los datos del atributo seleccionado por defecto

        #eventos cuando se cambia de elemento en el combo box
        self.comboBoxAtributos.currentIndexChanged.connect(lambda x: self.mostrar_atributo())

        #eventos botones actualizar atributo
        self.btnActualizar.clicked.connect(self.actualizar_atributo)

        self.comboBoxAtributos.setIconSize(QSize(12, 12))

        # muestrar la información general del conjunto de datos
        self.labelNumInstancias.setText(str(self.conjunto.getNumInstancias()))
        self.labelNumAtributos.setText(str(self.conjunto.getNumAtributos()))


    def llenar_tabla(self):
        """Muestra los datos del csv en una tabla"""
        self.tabla.setColumnCount(self.conjunto.getNumAtributos())
        self.tabla.setHorizontalHeaderLabels(self.conjunto.getNombresAtributos())

        self.tabla.setRowCount(0)
        for index, row in self.conjunto.panda.iterrows():
            self.tabla.insertRow(index)
            for i in range(len(row)):
                self.tabla.setItem(index, i, QTableWidgetItem(str(row[i])))

    def llenar_combo_box(self):
        """Llena los combo box con los nombres de los atributos separados por tipo"""
        for atributo in self.conjunto.getAtributos():
            if atributo.getTipo() == "numerico":
                self.comboBoxAtributos.addItem(QIcon("iconos/numerico.ico"), atributo.getNombre(), userData=self.NUMERICO)
            elif atributo.getTipo() == "categorico":
                self.comboBoxAtributos.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre(), userData=self.CATEGORICO)

    def actualizar_label_fuera_dominio(self, atributo):
        fuera_dominio = len(atributo.getValoresFueraDominio())
        total = self.conjunto.getNumInstancias()
        porcentaje = (fuera_dominio * 100) / total
        texto = str(fuera_dominio) + " (" + str(round(porcentaje, 2)) +"%)"
        self.labelFueraDominio.setText(texto)

    def actualizar_label_valores_faltantes(self, atributo):
        faltantes = len(atributo.getValoresFaltantes())
        total = self.conjunto.getNumInstancias()
        porcentaje = (faltantes * 100) / total
        texto = str(faltantes) + " (" + str(round(porcentaje, 2)) +"%)"
        self.labelValoresFaltantes.setText(texto)

    def mostrar_atributo(self):
        """"Muestra los datos del atributo actual que esta en el combo box"""
        if self.comboBoxAtributos.count() == 0: # si no hay elementos en el combo box se desactiva
            self.nombreAtributo.setText("")
            self.tipoAtributo.setText("")
            self.dominioAtributo.setText("")
            self.groupBoxAtributos.setEnabled(False)
            #falta limpiar mas etiquetas
        
        else:
            if not self.groupBoxAtributos.isEnabled():
                self.groupBoxAtributos.setEnabled(True)

            nombre_atributo = self.comboBoxAtributos.currentText()
            atributo = self.conjunto.getAtributo(nombre_atributo)
            self.nombreAtributo.setText(atributo.getNombre())
            self.tipoAtributo.setText(atributo.getTipo())
            self.dominioAtributo.setText(atributo.getDominio())

            self.actualizar_label_fuera_dominio(atributo)
            self.actualizar_label_valores_faltantes(atributo)

    
    def actualizar_atributo(self):
        """Evento clic del boton para acualizar un atributo"""
        nombre_atributo = self.comboBoxAtributos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)

        # falta comprobar que los datos no esten vacios
        nom = self.nombreAtributo.text()
        tipo = self.tipoAtributo.text()
        dominio = self.dominioAtributo.text()
        index = self.comboBoxAtributos.currentIndex()

        if nom != atributo.getNombre():
            atributo.setNombre(nom)
            self.comboBoxAtributos.setItemText(index, nom)
            #self.tabla.selectColumn(QItemSelectionModel.Deselect) # deselecciona las columnas seleccionadas
            #indexColumna = self.encontrar_index_columna(nom)
            #self.tabla.selectColumn(indexColumna)

        if tipo != atributo.getTipo():
            atributo.setTipo(tipo)
            if tipo == "categorico":
                nuevo_tipo = self.CATEGORICO
                icono = QIcon("iconos/categorico.ico")
            else:
                nuevo_tipo = self.NUMERICO
                icono = QIcon("iconos/numerico.ico")

            self.comboBoxAtributos.setItemData(index, nuevo_tipo)
            self.comboBoxAtributos.setItemIcon(index, icono)
                

        if dominio != atributo.getDominio():
            atributo.setDominio(dominio)
            self.actualizar_label_fuera_dominio(self.labelFueraDominio, atributo)



    def encontrar_index_columna(self, columna):
        for index, nom_columna in enumerate(self.conjunto.panda.columns):
            if nom_columna == columna:
                print("\n index=", index)
                return index
        return 0
            






        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()