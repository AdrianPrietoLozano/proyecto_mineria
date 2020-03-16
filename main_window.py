from main_window_ui import *
from dialogo_elegir_propiedades import *
from ventana_descripcion import *
from ventana_valores_faltantes import *
from ventana_fuera_dominio import *
from ventana_agregar_instancia import *
from ventana_eliminar_instancias import *
from ventana_correlacion_pearson import *
from ventana_coeficiente_tschuprow import *
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QAction, QAbstractItemView
from PyQt5.QtCore import Qt, QDir, QItemSelectionModel, QSize, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
import pandas as pd
import re
from conjunto_datos import ConjuntoDatos
from table_model_pandas import TableModelPandas

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    NUMERICO = 1
    CATEGORICO = 2

    # posiciones de las opciones del combo box donde se elige el tipo de atributo
    POS_NUMERICO_COMBO = 0
    POS_CATEGORICO_COMBO = 1

    signal_agregar_instancia = pyqtSignal()
    signal_eliminar_instancias = pyqtSignal()

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

        # evento boton descripcion
        self.btnDescripcion.clicked.connect(self.mostrar_descripcion)

        # evento boton valores fuera de dominio
        self.btnFueraDominio.clicked.connect(self.mostrar_fuera_dominio)
        # evento boton valores faltantes
        self.btnFaltantes.clicked.connect(self.mostrar_val_faltantes)

        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.selectionModel().selectionChanged.connect(self.selecciono)

        # conectar evento agregar instancia
        self.signal_agregar_instancia.connect(self.actualizar_etiquetas)
        self.signal_eliminar_instancias.connect(self.actualizar_etiquetas)

    def mostrar_fuera_dominio(self):
        nombre_atributo = self.comboBoxAtributos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)
        val_fuera_dominio = atributo.getValoresFueraDominio()
        self.ventana_fuera_dominio = VentanaFueraDominio(val_fuera_dominio, nombre_atributo)
        self.ventana_fuera_dominio.show()

    def mostrar_descripcion(self):
        self.ventana_descripcion = VentanaDescripcion(self.conjunto)
        self.ventana_descripcion.show()

    def mostrar_val_faltantes(self):
        nombre_atributo = self.comboBoxAtributos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)
        valores_faltantes = atributo.getValoresFaltantes()
        self.ventana_faltantes = VentanaFaltantes(valores_faltantes, nombre_atributo)
        self.ventana_faltantes.show()

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
        self.eliminar_instancia_action.triggered.connect(self.mostrar_eliminar_instancias)
        self.toolBar.addAction(self.eliminar_instancia_action)

        self.agregar_instancia_action = QAction(QtGui.QIcon('iconos/add.ico'), "Agregar instancias")
        self.agregar_instancia_action.triggered.connect(self.mostrar_agregar_instancia)
        self.toolBar.addAction(self.agregar_instancia_action)

        self.toolBar.addSeparator()
        self.btnCorrelacion = QtWidgets.QPushButton(self.toolBar)
        self.btnCorrelacion.setText("Correlación de Pearson")
        self.btnCorrelacion.clicked.connect(self.mostrar_ventana_correlacion)
        self.toolBar.addWidget(self.btnCorrelacion)

        self.btnTschuprow = QtWidgets.QPushButton(self.toolBar)
        self.btnTschuprow.setText("Coeficiente de contingencia de Tschuprow")
        self.btnTschuprow.clicked.connect(self.mostrar_ventana_tschuprow)
        self.toolBar.addWidget(self.btnTschuprow)

    def mostrar_ventana_correlacion(self):
        self.ventana = VentanaCorrelacionPearson(self.conjunto)
        self.ventana.show()

    def mostrar_ventana_tschuprow(self):
        self.ventana = VentanaCoeficienteTschuprow(self.conjunto)
        self.ventana.show()

    def mostrar_eliminar_instancias(self):
        """Muestra la ventana para eliminar instancias"""
        self.ventana = VentanaEliminarInstancias(self.model, self.signal_eliminar_instancias)
        self.ventana.show()

    def mostrar_agregar_instancia(self):
        """Muestra la ventana para agregar un nueva instancia"""
        self.ventana = VentanaAgregarInstancia(self.conjunto, self.model, self.signal_agregar_instancia)
        self.ventana.show()

    def actualizar_etiquetas(self):
        """Actualiza las etiquetas despues de insertar una instancia"""
        if self.comboBoxAtributos.count() == 0: # si no hay atributos termina
            return

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
        try:
            fuera_dominio = len(atributo.getValoresFueraDominio())
            total = self.conjunto.getNumInstancias()
            porcentaje = (fuera_dominio * 100) / total
            texto = str(fuera_dominio) + " (" + str(round(porcentaje, 2)) +"%)"
            self.labelFueraDominio.setText(texto)
            self.btnFueraDominio.setEnabled(True)
        except re.error: # si la expresión regular es inválida
            QMessageBox.warning(self, "Dominio incorrecto",
                "El dominio no es una expresión regular válida")
            self.labelFueraDominio.clear()
            self.btnFueraDominio.setEnabled(False)


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

    def actualizar_label_desviacion(self, atributo):
        desviacion = str(atributo.getDesviacionEstandar())
        self.labelDesviacionEstandar.setText(desviacion)

    def mostrar_atributo(self):
        """"Muestra los datos del atributo actual que esta en el combo box"""
        if self.comboBoxAtributos.count() == 0: # si no hay elementos en el combo box se desactiva
            self.editNombreAtributo.setText("")
            self.comboBoxTipoAtributo.setEnabled(False)
            self.editDominioAtributo.setText("")
            self.groupBoxAtributos.setEnabled(False)
            #falta limpiar mas etiquetas
        
        else:
            if not self.groupBoxAtributos.isEnabled():
                self.groupBoxAtributos.setEnabled(True)

            nombre_atributo = self.comboBoxAtributos.currentText()
            atributo = self.conjunto.getAtributo(nombre_atributo)
            self.editNombreAtributo.setText(atributo.getNombre())
            self.editDominioAtributo.setText(atributo.getDominio())

            self.actualizar_label_fuera_dominio(atributo)
            self.actualizar_label_valores_faltantes(atributo)

            # si el atributo es numerico muestra su moda, media, mediana, etc..
            if self.comboBoxAtributos.currentData() == self.NUMERICO:
                self.actualizarMetricas(atributo)
                self.btnHistograma.setVisible(False)
                self.btnBoxPlot.setVisible(True)
                self.comboBoxTipoAtributo.setCurrentIndex(self.POS_NUMERICO_COMBO)
            else: # si es categorico esconde la moda, media, mediana, etc.
                self.contenedorMetricas.setVisible(False)
                self.btnHistograma.setVisible(True)
                self.btnBoxPlot.setVisible(False)
                self.comboBoxTipoAtributo.setCurrentIndex(self.POS_CATEGORICO_COMBO)


    def actualizarMetricas(self, atributo):
        """Muestra el contenedor donde esta la moda, media, mediana, etc.
        y actualiza los valores"""
        self.contenedorMetricas.setVisible(True)
        self.actualizar_label_moda(atributo)
        self.actualizar_label_mediana(atributo)
        self.actualizar_label_media(atributo)
        self.actualizar_label_desviacion(atributo)

    
    def actualizar_atributo(self):
        """Evento clic del boton para actualizar un atributo"""
        dominio = self.editDominioAtributo.text()
        nom = self.editNombreAtributo.text()

        if dominio == "" or nom == "":
            print("vacios")
            return

        nombre_atributo = self.comboBoxAtributos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)

        if self.comboBoxTipoAtributo.currentIndex() == self.POS_NUMERICO_COMBO:
            tipo = "numerico"
        else:
            tipo = "categorico"
        
        index = self.comboBoxAtributos.currentIndex()

        # actualizar nombre
        if nom != atributo.getNombre(): # solo cambia el nombre si es diferente al anterior
            atributo.setNombre(nom)
            self.comboBoxAtributos.setItemText(index, nom)

        # actualizar tipo
        if tipo != atributo.getTipo(): # solo cambia el tipo si es diferente al anterior
            atributo.setTipo(tipo) # al cambiar el tipo es necesario actualizar la instancia atributo
            atributo = self.conjunto.getAtributo(atributo.getNombre()) # actualiza el atributo ya que al cambiar de tipo se cambia el tipo de instancias
            if tipo == "categorico": # si el nuevo tipo es categorico entonces debe agregarlo a las opciones del combo box target
                nuevo_tipo = self.CATEGORICO
                icono = QIcon("iconos/categorico.ico")
                self.contenedorMetricas.setVisible(False) # oculta la moda, media, mediana, ...
                self.comboBoxTarget.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre())
            else:
                nuevo_tipo = self.NUMERICO
                icono = QIcon("iconos/numerico.ico")
                self.actualizarMetricas(atributo) # muestra la moda, media, mediana, ...
                index_target = self.comboBoxTarget.findText(atributo.getNombre())
                self.comboBoxTarget.removeItem(index_target)
                if atributo.getNombre() == self.conjunto.getTarget(): # si se cambio el tipo del atributo target
                    self.conjunto.setTarget("")
                    self.comboBoxTarget.setCurrentIndex(0)

            self.comboBoxAtributos.setItemData(index, nuevo_tipo)
            self.comboBoxAtributos.setItemIcon(index, icono)
                
        # actualizar dominio
        if dominio != atributo.getDominio(): # solo cambia el dominio si es diferente
            atributo.setDominio(dominio)
            self.actualizar_label_fuera_dominio(atributo)


        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()