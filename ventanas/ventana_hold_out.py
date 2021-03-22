from ventana_hold_out_ui import *
#from algoritmos.k_fold import KFoldCrossValidation
# Importar mi clase del algoritmo
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget, QMessageBox
import numpy as np
import pandas

from holdOut_main import *

class VentanaHoldOut(QWidget, Ui_Form):

    def __init__(self, data, target, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.data = data.apply(pandas.to_numeric, errors="ignore")
        self.target = target
        #self.es_multi_clase = True
        self.arrayOrden = pandas.unique(self.data[self.target]).tolist()
        # si el target es de tipo numérico, entonces es un problema de regresión
        # KNN es el único de estos algoritmos que funciona para regresión
        self.es_regresion = False
        if np.issubdtype(self.data[self.target].dtype, np.number):
            self.es_regresion = True

        self.btnAceptar.clicked.connect(self.iniciar_evaluacion)
        self.labelCargando.setVisible(False)

        # si los posibles valores del target son 2 y el problema no es de regresion
        #muestra la opcion para elegir el valor positivo y el negativo
        """
        if len(self.data[self.target].unique()) == 2:
            self.es_multi_clase = False
            if not self.es_regresion:
                posibles_valores = self.data[self.target].unique().astype(str).tolist()
                self.comboBoxValorPositivo.addItems(posibles_valores)
            else:
                self.groupBoxValorPositivo.setVisible(False)
        else:
            self.groupBoxValorPositivo.setVisible(False)
        """

    def iniciar_evaluacion(self):
        algoritmo = self.comboBoxAlgoritmo.currentText()
        
        if self.es_regresion:
            if algoritmo == "One R" or algoritmo == "Naive Bayes":
                QMessageBox.critical(self, "Error", \
                    "El algoritmo seleccionado no funciona con problemas de regresión")
                return

        if algoritmo == "One R" and np.dtype(np.number) in self.data.dtypes.values:
            QMessageBox.critical(self, "Error", \
                    "One R solo funciona con todas las columnas categóricas")
            return

        self.btnAceptar.setEnabled(False) # desactiva boton
        self.labelCargando.setVisible(True)
        self.tablaResultados.setModel(None)
        self.labelAlgoritmo.setText("")
        self.repaint() # para que se actualice la etiqueta

        # def main_HoldOut(data, target, bandera_cat_num, algoritmo, iteraciones, arrayOrden):
        
        if self.es_regresion == False:
            exactitudFinal, dataframeFinal = main_HoldOut(self.data, self.target, self.es_regresion, algoritmo, self.numeroIteraciones.value(), self.arrayOrden)
            msg = "{}, exactitud promedio: {}".format(self.comboBoxAlgoritmo.currentText(), exactitudFinal)
            self.labelAlgoritmo.setText(msg)
            self.tablaResultados.setModel(TableModelPandas(dataframeFinal))
        
        # def numerico_HoldOut(data, target, bandera_cat_num, algoritmo, iteraciones):

        else:
            dataframeFinal = numerico_HoldOut(self.data, self.target, self.numeroIteraciones.value())
            self.tablaResultados.setModel(TableModelPandas(dataframeFinal))
        """
        positivo, negativo = None, None
        if not self.es_multi_clase and not self.es_regresion:
            index_val_positivo = self.comboBoxValorPositivo.currentIndex()
            index_val_negativo = 0 if index_val_positivo == 1 else 1
            val_positivo = self.comboBoxValorPositivo.itemText(index_val_positivo)
            val_negativo = self.comboBoxValorPositivo.itemText(index_val_negativo)

            positivo = val_positivo
            negativo = val_negativo
        
        k_fold = KFoldCrossValidation(self.data, self.target, num_folds,
            algoritmo, positivo, negativo)
        resultado = k_fold.iniciar_validacion()
        """

        #revisar TODO: Here
        #self.mostrar_tablas(resultado)
        self.btnAceptar.setEnabled(True)
        self.labelCargando.setVisible(False)


    def mostrar_tablas(self, resultado):
        if self.es_multi_clase and not self.es_regresion: # Borrar - Cuerpo no
            tabla = resultado[0]
            exactitud = resultado[1]

            msg = "{}, exactitud promedio: {}".format(self.comboBoxAlgoritmo.currentText(), exactitud)
            self.labelAlgoritmo.setText(msg)
            self.tablaResultados.setModel(TableModelPandas(tabla))
        else: # Borrar
            self.labelAlgoritmo.setText("")
            # Aquí voy a mostrar dos 
            self.tablaResultados.setModel(TableModelPandas(resultado))

    """
    def eliminar_tablas(self):
        for i in reversed(range(self.verticalLayout.count())): 
            widgetAEliminar = self.verticalLayout.itemAt(i).widget()
            self.verticalLayout.removeWidget(widgetAEliminar)
            widgetAEliminar.setParent(None)
    """