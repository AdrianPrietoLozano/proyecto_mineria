from main_window_ui import *
from dialogo_elegir_propiedades import *
from ventana_descripcion import *
from ventana_valores_faltantes import *
from ventana_fuera_dominio import *
from ventana_agregar_instancia import *
from ventana_editar_instancia import *
from ventana_eliminar_instancias import *
from ventana_correlacion_pearson import *
from ventana_coeficiente_tschuprow import *
from ventana_agregar_atributo import *
from ventana_moda import *
from ventana_boxplot import *
from ventana_histograma import *

from ventana_knn import *
from ventana_oneR import *

from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QAction, QAbstractItemView, QMenu,QHeaderView, QMessageBox
from PyQt5.QtCore import Qt, QDir, QItemSelectionModel, QSize, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor
import pandas as pd
from glob import glob
import re
import json
import os
from conjunto_datos import ConjuntoDatos
from table_model_pandas import TableModelPandas
from respaldos import Respaldos
from algoritmos import zero_r


#TODO: Revisar los respaldos, en atributo lo guarda despues de eliminar, en instancias, lo guarda antes de eliminar
#TODO: Eliminar valores faltantes en Boxplot y también histograma
#TODO: Investigar como arreglar que el pandas cuando pasa un valor faltante, convierte toda la columna en categorico
#TODO: Si el target no esta definido, el boxplot e histograma deben hacerse sin tomar en cuenta ese atributo

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    NUMERICO = 1
    CATEGORICO = 2

    # posiciones de las opciones del combo box donde se elige el tipo de atributo
    POS_NUMERICO_COMBO = 0
    POS_CATEGORICO_COMBO = 1

    signal_agregar_instancia = pyqtSignal() # se emite cuando se agrega una instancia
    signal_eliminar_instancias = pyqtSignal(int) # se emite cuando se elimina una instancia
    signal_editar_instancia = pyqtSignal() # se emite cuando se edita una instancia
    signal_agregar_columna = pyqtSignal(str) # se emite cuando se agrega una instancia

    def __init__(self, ruta, conexion=None, query=None, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.conexion = conexion
        self.query = query

        self.ruta = ruta
        self.conjunto = ConjuntoDatos(self.ruta, self.conexion, self.query)

        # si hay una conexión y un query entonces mostrar la opción para cambiar el query
        if self.conexion != None and self.query != None:
            self.agregar_opcion_cambiar_query()


        self.respaldos = Respaldos(self.conjunto) # para hacer los respaldos
        self.num_version = 1 # numero de versión para el nombre de los respaldos
        self.num_instancias_agregadas = 0 # cada que se agregan 10 instancias se hace un respaldo
        self.num_instancias_eliminadas = 0 # cada que se eliminar 10 instancias se hacer un respaldo
        self.cargar_respaldos()

        # action nuevo para cargar nuevo dataset
        self.actionNuevo.triggered.connect(self.cargar_nuevo_dataset)

        # conectar eventos para las opciones de los algoritmos
        self.actionZero_R.triggered.connect(self.zeroR)
        self.actionOne_R.triggered.connect(self.mostrar_ventana_oneR)
        self.actionNaive_Bayes.triggered.connect(self.mostrar_ventana_naive_bayes)
        self.actionK_NN.triggered.connect(self.mostrar_ventana_knn)

        # id de la instancia en la que se dio clic en la tabla
        self.currentIdRow = None

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
        self.lineEditRuta.setText(str(self.conjunto.getRutaRespaldos()))

        # toolbar
        self.agregar_actions_toolbar()

        # evento boton eliminar atributo
        self.btnEliminarAtributo.clicked.connect(self.eliminar_atributo)

        # evento boton mostar moda
        self.btnModas.clicked.connect(self.mostrar_ventanas_modas)

        # evento boton descripcion
        self.btnDescripcion.clicked.connect(self.mostrar_descripcion)

        # evento boton valores fuera de dominio
        self.btnFueraDominio.clicked.connect(self.mostrar_fuera_dominio)
        # evento boton valores faltantes
        self.btnFaltantes.clicked.connect(self.mostrar_val_faltantes)

        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        # este menú se muestra al dar clic sobre un id en la tabla
        self.menu_clic_tabla = QMenu("opciones")
        self.action_editar = QAction(QtGui.QIcon('iconos/editar.png'), "Editar")
        self.action_editar.triggered.connect(self.mostrar_editar_instancia)
        self.menu_clic_tabla.addAction(self.action_editar)
        self.tabla.verticalHeader().sectionPressed.connect(self.mostrar_menu_editar)

        #event boton actualizar target, simbolo faltante y ruta
        self.btnActualizarInfo.clicked.connect(self.actualizar_info_general)
        self.btnHistograma.clicked.connect(self.mostrar_histograma)
        self.btnBoxPlot.clicked.connect(self.mostrar_boxplot)

        # conectar evento agregar instancia. Estos eventos se emiten desde otras ventanas
        self.signal_agregar_instancia.connect(self.instancia_agregada)
        self.signal_eliminar_instancias.connect(self.instancias_eliminadas)
        self.signal_editar_instancia.connect(self.actualizar_etiquetas)
        self.signal_agregar_columna.connect(self.atributo_agregado)


    def cargar_nuevo_dataset(self):
        """Cierra la ventana actual y abre dialogo para abrir nuevo archivo de propiedades"""
        from dialogo_elegir_propiedades import DialogoElegirPropiedades
        self.dialogo = DialogoElegirPropiedades()
        self.close()
        self.dialogo.show()

    def agregar_opcion_cambiar_query(self):
        action_nuevo_query = QAction(self)
        action_nuevo_query.setText("Cambiar query")
        action_nuevo_query.triggered.connect(self.mostrar_ventana_query)
        self.menuArchivo.addAction(action_nuevo_query)

    def mostrar_ventana_query(self):
        from ventana_base_datos import VentanaBaseDatos
        self.conexion.reconnect() # reconecta a la base de datos
        self.ventana = VentanaBaseDatos(self.conexion, self.ruta)
        self.close()
        self.ventana.show()

    def instancia_agregada(self):
        """Este método se ejecuta cada que se agrega una instancia"""
        self.actualizar_etiquetas() # actualizar moda, media, media, num de instancias, etc

        self.num_instancias_agregadas += 1
        # hace respaldo cuando se han agregado 10 instancias
        if self.num_instancias_agregadas >= 10:
            self.hacer_respaldo("instancias_agregadas")
            self.num_instancias_agregadas = 0

    def instancias_eliminadas(self, num):
        """Este método se ejecuta cada que se elimina una instancia"""
        self.actualizar_etiquetas() # actualiza moda, media, media, num de instancias, etc

        self.num_instancias_eliminadas += num
        # hace respaldo cuando se eliminan 10 o más instancias
        if self.num_instancias_eliminadas >= 10:
            self.hacer_respaldo("instancias_eliminadas")
            self.num_instancias_eliminadas = 0

    def mostrar_menu_editar(self, index):
        """Menú que se muestra al dar clic sobre el id de una instancia en la tabla"""
        self.currentIdRow = self.conjunto.panda.index[index]
        self.menu_clic_tabla.exec_(QCursor.pos())

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
            self.conjunto.eliminarAtributoDePropiedades(actual_index) # elimina el atributo del archivo de propiedades
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

            self.hacer_respaldo("eliminar_" + nombre_atributo)

        else:
            print("Ocurrio un error")

        
    def atributo_agregado(self, nombre):
        """Esta función se llama inmediatamente después de haber agregado un nuevo atributo"""
        atributo = self.conjunto.getAtributo(nombre)

        if atributo.getTipo() == "numerico":
            icon = QIcon("iconos/numerico.ico")
            tipo = self.NUMERICO
        else:
            icon = QIcon("iconos/categorico.ico")
            tipo = self.CATEGORICO
            self.comboBoxTarget.addItem(icon, nombre)

        self.comboBoxAtributos.addItem(icon, nombre, userData=tipo)
        self.actualizar_etiquetas()
        self.labelNumAtributos.setText(str(self.conjunto.getNumAtributos()))

        self.hacer_respaldo("agregar_" + nombre)


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
        self.toolBar.addSeparator()
        self.agregar_columna_action = QAction(QtGui.QIcon('iconos/add_column.png'), "Agregar columna")
        self.agregar_columna_action.triggered.connect(self.mostrar_agregar_columna)
        self.toolBar.addAction(self.agregar_columna_action)

        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.btnCorrelacion = QtWidgets.QPushButton(self.toolBar)
        self.btnCorrelacion.setText("Correlación de Pearson")
        self.btnCorrelacion.clicked.connect(self.mostrar_ventana_correlacion)
        self.toolBar.addWidget(self.btnCorrelacion)

        self.btnTschuprow = QtWidgets.QPushButton(self.toolBar)
        self.btnTschuprow.setText("Coeficiente de contingencia de Tschuprow")
        self.btnTschuprow.clicked.connect(self.mostrar_ventana_tschuprow)
        self.toolBar.addWidget(self.btnTschuprow)

    def mostrar_ventanas_modas(self):
        """Muestra una ventana con las modas"""
        nombre_atributo = self.comboBoxAtributos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)
        modas = atributo.getModa()
        self.ventana = VentanaModa(modas)
        self.ventana.show()

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

    def mostrar_agregar_columna(self):
        """Muestra la ventana para agregar un nueva instancia"""
        self.ventana = VentanaAgregarAtributo(self.conjunto, self.model, self.signal_agregar_columna)
        self.ventana.show()

    def mostrar_editar_instancia(self):
        """Muestra la ventana para agregar un nueva instancia"""
        self.ventana = VentanaEditarInstancia(self.currentIdRow, self.conjunto, self.model, self.signal_agregar_instancia)
        self.ventana.show()

    def actualizar_etiquetas(self):
        """Actualiza las etiquetas despues de insertar, editar o eliminar una instancia"""
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
            else:
                self.comboBoxAtributos.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre(), userData=self.CATEGORICO)
                self.comboBoxTarget.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre())

    def actualizar_info_general(self):
        """Actualizar el target, simbolo faltante y ruta"""
        target_actual = self.conjunto.getTarget()
        sim_faltante_actual = self.conjunto.getSimboloFaltante()
        ruta_actual = self.conjunto.getSimboloFaltante()
        debe_actualizar = False

        nuevo_target = self.comboBoxTarget.currentText()
        if nuevo_target != target_actual: # si el nuevo target es diferente al actual
            if self.comboBoxTarget.currentIndex() == 0: # si se va a quitar el target (la opcion 0 corresponde a la opcion "Ninguno")
                self.conjunto.setTarget("")
            else:
                self.conjunto.setTarget(nuevo_target)

        nuevo_simbolo_faltante = self.lineEditValorFaltante.text()
        if nuevo_simbolo_faltante != sim_faltante_actual: # si el nuevo simbolo es diferente al actual
                self.conjunto.setSimboloFaltante(nuevo_simbolo_faltante)
                debe_actualizar = True # debe actualizar etiquetas de moda, media, median, etc.

        nueva_ruta = self.lineEditRuta.text()
        if nueva_ruta != ruta_actual: # solo actualizar si la nueva ruta es diferente a la actual
            if nueva_ruta != "": # no se permite valor en blanco
                self.conjunto.setRutaRespaldos(nueva_ruta)
            else: # restaura el valor de la ruta actual
                self.lineEditRuta.setText(str(self.conjunto.getRutaRespaldos()))

        if debe_actualizar:
            self.actualizar_etiquetas()

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

    # Este metodo se llama cada vez que se cambia de atributo del combo box
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
        self.actualizar_label_mediana(atributo)
        self.actualizar_label_media(atributo)
        self.actualizar_label_desviacion(atributo)

    
    def actualizar_atributo(self):
        """Evento clic del boton para actualizar un atributo"""
        dominio = self.editDominioAtributo.text()
        nom = self.editNombreAtributo.text()
        nombre_atributo = self.comboBoxAtributos.currentText()
        atributo = self.conjunto.getAtributo(nombre_atributo)

        if nom == "": # no se puede poner un nombre vacio a un atributo
            self.editNombreAtributo.setText(atributo.getNombre())
            QMessageBox.information(self, "Error", "El nombre no puede estar vacío")
            return

        if self.comboBoxTipoAtributo.currentIndex() == self.POS_NUMERICO_COMBO:
            tipo = "numerico"
        else:
            tipo = "categorico"
        
        index = self.comboBoxAtributos.currentIndex()

        # actualizar nombre
        if nom != atributo.getNombre(): # solo cambia el nombre si es diferente al anterior
            if not nom in self.conjunto.getNombresAtributos(): # no puede haber nombres de atributo repetidos
                atributo.setNombre(nom)
                self.comboBoxAtributos.setItemText(index, nom)
            else:
                QMessageBox.information(self, "Error", "El nombre ya existe")

        # actualizar tipo
        if tipo != atributo.getTipo(): # solo cambia el tipo si es diferente al anterior
            atributo.setTipo(tipo) # al cambiar el tipo es necesario actualizar la instancia atributo
            atributo = self.conjunto.getAtributo(atributo.getNombre()) # actualiza el atributo ya que al cambiar de tipo se cambia el tipo de instancias
            if tipo == "categorico": # si el nuevo tipo es categorico entonces debe agregarlo a las opciones del combo box target
                nuevo_tipo = self.CATEGORICO
                icono = QIcon("iconos/categorico.ico")
                self.contenedorMetricas.setVisible(False) # oculta la moda, media, mediana, ...
                self.btnBoxPlot.setVisible(False) # oculta el boton boxplot
                self.btnHistograma.setVisible(True) # muetra el boton histograma
                self.comboBoxTarget.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre())
            else:
                nuevo_tipo = self.NUMERICO
                icono = QIcon("iconos/numerico.ico")
                self.actualizarMetricas(atributo) # muestra la moda, media, mediana, ...
                self.btnHistograma.setVisible(False) # oculta el boton histograma
                self.btnBoxPlot.setVisible(True) # muestra el boton boxplot
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
    
    def mostrar_boxplot(self):
        self.ventana = boxplot(self.conjunto, self.comboBoxAtributos.currentText())
        self.ventana.show()

    def mostrar_histograma(self):
        self.ventana = histograma(self.conjunto, self.comboBoxAtributos.currentText())
        self.ventana.show()

    def hacer_respaldo(self, nombre, guardar_indices=True):
        """Crea un respaldo del csv y del archivo de propiedades"""
        nombre_respaldo = str(self.num_version) + "_" + nombre
        if self.respaldos.hacer_respaldo(nombre_respaldo, guardar_indices):
            self.num_version += 1
            action = QAction(self)
            action.setText(nombre_respaldo + ".json")
            action.triggered.connect(lambda x: self.iniciar_version(nombre_respaldo + ".json"))
            self.menuVersiones.addAction(action)
        else:
            print("error al crear respaldo")

    def iniciar_version(self, nombre):
        """Método que se ejecuta al iniciar una versión de los respaldos desde el menubar"""
        self.close()
        self.ventana = MainWindow(self.conjunto.getRutaRespaldos() + nombre)
        self.ventana.show()

    def cargar_respaldos(self):
        """Carga los nombres de los respaldos que hay en la ruta de respaldos"""
        ruta_respaldos = self.conjunto.getRutaRespaldos()

        # itera a traves de todos los respaldos y los agrega al menubar de las versiones
        if os.path.isdir(ruta_respaldos): # si existe la ruta
            for respaldo in glob(ruta_respaldos + "*.json"):
                nombre_respaldo = os.path.basename(respaldo) # extrae solo el nombre del archivo
                action = QAction(self)
                action.setText(nombre_respaldo)

                # chk es necesario para que triggered envie su estado actual (True o False)
                # el argumento por defecto es necesario para que lambda obtenga una copia de
                # la variable actual del ciclo
                action.triggered.connect(lambda chk, nombre_respaldo=nombre_respaldo: self.iniciar_version(nombre_respaldo))
                self.menuVersiones.addAction(action)
                self.num_version += 1


    ###############################################
    # EVENTOS PARA LOS ALGORITMOS #
    def comprobar_target(self):
        target = self.conjunto.getTarget()
        if target == None or target == "":
            QMessageBox.critical(self, "Error", "El target no esta definido")
            return False

        return True

    def zeroR(self):
        if self.comprobar_target():
            msg = "Frecuencias para el atributo " + self.conjunto.getTarget()
            frecuencias = zero_r.generar_frecuencias(self.conjunto.panda,
                self.conjunto.getTarget())

            msg += "\n\n"
            for key, val in frecuencias.items():
                msg += key + ":  " + str(val) + "\n"

            clase, umbral = zero_r.obtenerMayor(frecuencias)
            msg += "\nUmbral: " + str(round(umbral, 4))

            QMessageBox.information(self, "Zero-R", msg)

    def mostrar_ventana_oneR(self):
        if self.comprobar_target():
            self.ventana = VentanaOneR(self.conjunto.panda,
                self.conjunto.getTarget())
            self.ventana.show()

    def mostrar_ventana_naive_bayes(self):
        pass


    def mostrar_ventana_knn(self):
        if self.comprobar_target():
            self.ventana = VentanaKNN(self.conjunto.panda,
                self.conjunto.getTarget())
            self.ventana.show()


        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()