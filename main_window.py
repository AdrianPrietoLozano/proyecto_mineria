from main_window_ui import *
from dialogo_elegir_propiedades import *
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, QDir, QItemSelectionModel
import pandas as pd
from conjunto_datos import ConjuntoDatos
from table_model_pandas import TableModelPandas

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ruta, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.ruta = ruta
        self.conjunto = ConjuntoDatos(self.ruta)

        # utilizando un modelo los datos en la tabla se cargan muchisimo más rápido
        self.model = TableModelPandas(self.conjunto.panda)
        self.tabla.setModel(self.model)        

        self.llenar_combo_boxes()
        self.mostrar_atributo_numerico() # muestra los datos del atributo numerico seleccionado por defecto
        self.mostrar_atributo_categorico() # muestra los datos del atributo categorico seleccionado por defecto

        #eventos cuando se cambia de elemento en el combo box
        self.comboBoxNumericos.currentIndexChanged.connect(lambda x: self.mostrar_atributo_numerico())
        self.comboBoxCategoricos.currentIndexChanged.connect(lambda x: self.mostrar_atributo_categorico())

        #eventos botones actualizar atributo
        self.btnActualizarNumericos.clicked.connect(self.actualizar_atributo_numerico)
        self.btnActualizarCategoricos.clicked.connect(self.actualizar_atributo_categorico)

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

    def llenar_combo_boxes(self):
        """Llena los combo box con los nombres de los atributos separados por tipo"""
        for atributo in self.conjunto.getAtributos():
            if atributo.getTipo() == "numerico":
                self.comboBoxNumericos.addItem(atributo.getNombre())
            elif atributo.getTipo() == "categorico":
                self.comboBoxCategoricos.addItem(atributo.getNombre())

    def actualizar_label_fuera_dominio(self, label, atributo):
        fuera_dominio = (len(atributo.getValoresFueraDominio()))
        total = self.conjunto.getNumInstancias()
        procentaje = (fuera_dominio * 100) / total
        texto = str(fuera_dominio) + " (" + str(round(procentaje, 2)) +"%)"

        label.setText(texto)

    def mostrar_atributo_numerico(self):
        """"Muestra los datos del atributo numerico actual que esta en el combo box"""
        if self.comboBoxNumericos.count() == 0: # si no hay elementos en el combo box se desactiva
            self.nombreAtributoNumerico.setText("")
            self.tipoAtributoNumerico.setText("")
            self.dominioAtributoNumerico.setText("")
            self.groupBoxNumericos.setEnabled(False)
        
        else:
            if not self.groupBoxNumericos.isEnabled():
                self.groupBoxNumericos.setEnabled(True)

            nombre_atributo = self.comboBoxNumericos.currentText()
            atributo = self.conjunto.getAtributo(nombre_atributo)
            self.nombreAtributoNumerico.setText(atributo.getNombre())
            self.tipoAtributoNumerico.setText(atributo.getTipo())
            self.dominioAtributoNumerico.setText(atributo.getDominio())

            self.actualizar_label_fuera_dominio(self.labelFueraDominioNumerico, atributo)

    

    def mostrar_atributo_categorico(self):
        """Muestra los datos del atributo categorico actual que esta en el combo box"""
        if self.comboBoxCategoricos.count() == 0: # si no hay elementos en el combo box se desactiva
            self.nombreAtributoCate.setText("")
            self.tipoAtributoCate.setText("")
            self.dominioAtributoCate.setText("")
            self.groupBoxCategoricos.setEnabled(False)

        else:
            if not self.groupBoxCategoricos.isEnabled():
                self.groupBoxCategoricos.setEnabled(True)

            nombre_atributo = self.comboBoxCategoricos.currentText()
            atributo = self.conjunto.getAtributo(nombre_atributo)
            self.nombreAtributoCate.setText(atributo.getNombre())
            self.tipoAtributoCate.setText(atributo.getTipo())
            self.dominioAtributoCate.setText(atributo.getDominio())

            self.actualizar_label_fuera_dominio(self.labelFueraDominioCategorico, atributo)

    def actualizar_atributo_numerico(self):
        """Evento clic del boton para acualizar un atributo numéricos"""
        nombre_atributo = self.comboBoxNumericos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)

        # falta comprobar que los datos no esten vacios
        nom = self.nombreAtributoNumerico.text()
        tipo = self.tipoAtributoNumerico.text()
        dominio = self.dominioAtributoNumerico.text()
        index = self.comboBoxNumericos.currentIndex()

        if nom != atributo.getNombre():
            atributo.setNombre(nom)
            self.comboBoxNumericos.setItemText(index, nom)
            #self.tabla.selectColumn(QItemSelectionModel.Deselect) # deselecciona las columnas seleccionadas
            #indexColumna = self.encontrar_index_columna(nom)
            #self.tabla.selectColumn(indexColumna)

        if tipo != atributo.getTipo():
            if tipo == "categorico":
                atributo.setTipo(tipo)
                self.comboBoxCategoricos.addItem(atributo.getNombre())
                self.comboBoxNumericos.removeItem(index)

        if dominio != atributo.getDominio():
            atributo.setDominio(dominio)
            self.actualizar_label_fuera_dominio(self.labelFueraDominioNumerico, atributo)



    def actualizar_atributo_categorico(self):
        """Evento clic del boton para acualizar un atributo categorico"""
        nombre_atributo = self.comboBoxCategoricos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)

        # falta comprobar que los datos no esten vacios
        nom = self.nombreAtributoCate.text()
        tipo = self.tipoAtributoCate.text()
        dominio = self.dominioAtributoCate.text()
        index = self.comboBoxCategoricos.currentIndex()

        if nom != atributo.getNombre():
            atributo.setNombre(nom)
            self.comboBoxCategoricos.setItemText(index, nom)
            #self.tabla.selectColumn(QItemSelectionModel.Deselect) # deselecciona las columnas seleccionadas
            #indexColumna = self.encontrar_index_columna(nom)
            #self.tabla.selectColumn(indexColumna)


        if tipo != atributo.getTipo():
            if tipo == "numerico":
                atributo.setTipo(tipo)
                self.comboBoxNumericos.addItem(atributo.getNombre())
                self.comboBoxCategoricos.removeItem(index)

        if dominio != atributo.getDominio():
            atributo.setDominio(dominio)
            self.actualizar_label_fuera_dominio(self.labelFueraDominioCategorico, atributo)



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