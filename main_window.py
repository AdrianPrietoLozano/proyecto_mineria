from main_window_ui import *
from dialogo_elegir_propiedades import *
from agregar_instancia import *
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QAction, QAbstractItemView
from PyQt5.QtCore import Qt, QDir, QItemSelectionModel, QSize, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
import pandas as pd
from conjunto_datos import ConjuntoDatos
from table_model_pandas import TableModelPandas

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    NUMERICO = 1
    CATEGORICO = 2

    signal_agregar_instancia = pyqtSignal()

    def __init__(self, ruta, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.ruta = ruta
        self.conjunto = ConjuntoDatos(self.ruta)

        # utilizando un modelo los datos en la tabla se cargan muchisimo más rápido
        self.model = TableModelPandas(self.conjunto.panda)
        self.tabla.setModel(self.model)        

        self.llenar_combo_boxes()
        self.mostrar_atributo() # muestra los datos del atributo seleccionado por defecto en el combo box

        #evento cuando se cambia de elemento en el combo box
        self.comboBoxAtributos.currentIndexChanged.connect(lambda x: self.mostrar_atributo())

        #evento boton actualizar atributo
        self.btnActualizar.clicked.connect(self.actualizar_atributo)

        self.comboBoxAtributos.setIconSize(QSize(12, 12))
        self.comboBoxTarget.setIconSize(QSize(12, 12))

        # muestrar la información general del conjunto de datos
        self.labelNumInstancias.setText(str(self.conjunto.getNumInstancias()))
        self.labelNumAtributos.setText(str(self.conjunto.getNumAtributos()))
        
        self.iniciar_target()
        self.lineEditValorFaltante.setText(str(self.conjunto.getSimboloFaltante()))
        self.lineEditRuta.setText(str(self.conjunto.getRuta()))

        # toolbar
        self.agregar_actions_toolbar()

        # evento boton eliminar atributo
        self.btnEliminarAtributo.clicked.connect(self.eliminar_atributo)

        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.selectionModel().selectionChanged.connect(self.selecciono)

        # conectar evento
        self.signal_agregar_instancia.connect(self.actualizar_etiquetas)

    def eliminar_atributo(self):
        nombre_atributo = self.comboBoxAtributos.currentText()
        index_combo_box = self.comboBoxAtributos.currentIndex()

        # obtiene el index de una columna por nombre
        actual_index = self.conjunto.getIndiceAtributo(nombre_atributo)
        if self.model.removeColumns(actual_index, actual_index): # si se eliminó la columan correctamente
            self.conjunto.eliminarAtributoDeDiccionario(nombre_atributo)
            self.comboBoxAtributos.removeItem(index_combo_box)

            # del combo box que tiene las opciones para el target se quita el atributo eliminado
            index_target = self.comboBoxTarget.findText(nombre_atributo)
            if index_target != -1:
                self.comboBoxTarget.removeItem(index_target)
                if nombre_atributo == self.conjunto.getTarget(): # si se eliminó el atributo target
                    self.conjunto.setTarget("")
                    self.comboBoxTarget.setCurrentIndex(0)

            # actualiza la etiqueta de numero de atributos
            self.labelNumAtributos.setText(str(self.conjunto.getNumAtributos()))
        else:
            print("Ocurrio un error")


    def selecciono(self, a, b):
        print("entro a selecciono")

    def iniciar_target(self):
        """Inicializa el combo box del target con el atributo correcto"""
        target = self.conjunto.getTarget()
        if target != None and target != "" and target in self.conjunto.getNombresAtributos():
            if self.conjunto.getAtributo(target).getTipo() == "categorico":
                self.comboBoxTarget.setCurrentText(target)
            else:
                print("el target debe ser categorico")
        else:
            print("target no valido")
        

    def agregar_actions_toolbar(self):
        """Agrega las acciones (nueva instancia, nuevo atributo, etc) al toolbar"""
        self.eliminar_instancia_action = QAction(QtGui.QIcon('iconos/remove.ico'), "Eliminar instancias")
        self.toolBar.addAction(self.eliminar_instancia_action)

        self.agregar_instancia_action = QAction(QtGui.QIcon('iconos/add.ico'), "Agregar instancias")
        self.agregar_instancia_action.triggered.connect(self.mostrar_agregar_instancia)
        self.toolBar.addAction(self.agregar_instancia_action)

    def mostrar_agregar_instancia(self):
        """Muestra la ventana para agregar un nueva instancia"""
        self.ventana = AgregarInstancia(self.conjunto, self.model, self.signal_agregar_instancia)
        self.ventana.show()

    def actualizar_etiquetas(self):
        """Actualiza las etiquetas despues de insertar una instancia"""
        nombre_atributo = self.comboBoxAtributos.currentText()
        tipo_atributo = self.comboBoxAtributos.currentData()
        atributo = self.conjunto.getAtributo(nombre_atributo)

        if tipo_atributo == self.NUMERICO:
            self.actualizarMetricas(atributo)

        self.actualizar_label_fuera_dominio(atributo)
        self.actualizar_label_valores_faltantes(atributo)
        self.labelNumInstancias.setText(str(self.conjunto.getNumInstancias()))

    def llenar_combo_boxes(self):
        """Llena los combo box con los nombres de los atributos separados por tipo.
        También llena las opciones para elegir el target"""
        for atributo in self.conjunto.getAtributos():
            if atributo.getTipo() == "numerico":
                self.comboBoxAtributos.addItem(QIcon("iconos/numerico.ico"), atributo.getNombre(), userData=self.NUMERICO)
            elif atributo.getTipo() == "categorico":
                self.comboBoxAtributos.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre(), userData=self.CATEGORICO)
                self.comboBoxTarget.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre())

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

    def actualizar_label_moda(self, atributo):
        """Acutualiza el valor de la moda"""
        moda = str(atributo.getModa())
        self.labelModa.setText(moda)

    def actualizar_label_media(self, atributo):
        """Acutualiza el valor de la media"""
        media = str(atributo.getMedia())
        self.labelMedia.setText(media)

    def actualizar_label_mediana(self, atributo):
        """Acutualiza el valor de la mediana"""
        mediana = str(atributo.getMediana())
        self.labelMediana.setText(mediana)

    def mostrar_atributo(self):
        """"Muestra los datos del atributo actual que esta en el combo box"""
        if self.comboBoxAtributos.count() == 0: # si no hay elementos en el combo box se desactiva
            self.editNombreAtributo.setText("")
            self.editTipoAtributo.setText("")
            self.editDominioAtributo.setText("")
            self.groupBoxAtributos.setEnabled(False)
            #falta limpiar mas etiquetas
        
        else:
            if not self.groupBoxAtributos.isEnabled():
                self.groupBoxAtributos.setEnabled(True)

            nombre_atributo = self.comboBoxAtributos.currentText()
            atributo = self.conjunto.getAtributo(nombre_atributo)
            self.editNombreAtributo.setText(atributo.getNombre())
            self.editTipoAtributo.setText(atributo.getTipo())
            self.editDominioAtributo.setText(atributo.getDominio())

            self.actualizar_label_fuera_dominio(atributo)
            self.actualizar_label_valores_faltantes(atributo)

            # si el atributo es numerico muestra su moda, media, mediana, etc..
            if self.comboBoxAtributos.currentData() == self.NUMERICO:
                self.actualizarMetricas(atributo)
                self.btnHistograma.setVisible(False)
                self.btnBoxPlot.setVisible(True)
            else: # si es categorico esconde la moda, media, mediana, etc.
                self.contenedorMetricas.setVisible(False)
                self.btnHistograma.setVisible(True)
                self.btnBoxPlot.setVisible(False)


    def actualizarMetricas(self, atributo):
        """Muestra el contenedor donde esta la moda, media, mediana, etc.
        y actualiza los valores"""
        self.contenedorMetricas.setVisible(True)
        self.actualizar_label_moda(atributo)
        self.actualizar_label_mediana(atributo)
        self.actualizar_label_media(atributo)

    
    def actualizar_atributo(self):
        """Evento clic del boton para acualizar un atributo"""
        nombre_atributo = self.comboBoxAtributos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)

        # falta comprobar que los datos no esten vacios
        nom = self.editNombreAtributo.text()
        tipo = self.editTipoAtributo.text()
        dominio = self.editDominioAtributo.text()
        index = self.comboBoxAtributos.currentIndex()

        if nom != atributo.getNombre(): # solo cambia el nombre si es diferente al anterior
            atributo.setNombre(nom)
            self.comboBoxAtributos.setItemText(index, nom)
            #self.tabla.selectColumn(QItemSelectionModel.Deselect) # deselecciona las columnas seleccionadas
            #indexColumna = self.encontrar_index_columna(nom)
            #self.tabla.selectColumn(indexColumna)

        if tipo != atributo.getTipo(): # solo cambia el tipo si es diferente al anterior
            atributo.setTipo(tipo) # al cambiar el tipo es necesario actualizar la instancia atributo
            atributo = self.conjunto.getAtributo(atributo.getNombre()) # actualiza el atributo ya que al cambiar de tipo se cambia el tipo de instancias
            if tipo == "categorico":
                nuevo_tipo = self.CATEGORICO
                icono = QIcon("iconos/categorico.ico")
                self.contenedorMetricas.setVisible(False) # oculta la moda, media, mediana, ...
            else:
                nuevo_tipo = self.NUMERICO
                icono = QIcon("iconos/numerico.ico")
                self.actualizarMetricas(atributo) # muestra la moda, media, mediana, ...

            self.comboBoxAtributos.setItemData(index, nuevo_tipo)
            self.comboBoxAtributos.setItemIcon(index, icono)
                

        if dominio != atributo.getDominio(): # solo cambia el dominio si es diferente
            atributo.setDominio(dominio)
            self.actualizar_label_fuera_dominio(atributo)



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