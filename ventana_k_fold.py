from ventana_k_fold_ui import *
#from algoritmos.k_fold import KFoldCrossValidation
from k_fold import KFoldCrossValidation
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget

class VentanaKFold(QWidget, Ui_Form):

    def __init__(self, data, target, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.k_fold = KFoldCrossValidation(data, target)
        self.es_multi_clase = True

        self.btnAceptar.clicked.connect(self.iniciar_evaluacion)
        self.labelCargando.setVisible(False)

        # si los posibles valores del target son 2
        if len(data[target].unique()) == 2:
            self.es_multi_clase = False
            posibles_valores = data[target].unique().astype(str).tolist()
            self.comboBoxValorPositivo.addItems(posibles_valores)
        else:
            self.groupBoxValorPositivo.setVisible(False)

    def iniciar_evaluacion(self):
        self.btnAceptar.setEnabled(False) # desactiva boton
        self.labelCargando.setVisible(True)
        self.eliminar_tablas()
        self.repaint() # para que se actualice la etiqueta

        num_folds = int(self.numFolds.currentText())

        if not self.es_multi_clase:
            index_val_positivo = self.comboBoxValorPositivo.currentIndex()
            index_val_negativo = 0 if index_val_positivo == 1 else 1
            val_positivo = self.comboBoxValorPositivo.itemText(index_val_positivo)
            val_negativo = self.comboBoxValorPositivo.itemText(index_val_negativo)

            self.k_fold.setValorPositivo(val_positivo)
            self.k_fold.setValorNegativo(val_negativo)
        
        self.k_fold.setK(num_folds)
        resultado = self.k_fold.iniciar_validacion()
        self.mostrar_tablas(resultado)
        self.btnAceptar.setEnabled(True)
        self.labelCargando.setVisible(False)


    def mostrar_tablas(self, resultado):
        if self.es_multi_clase:
            tablas = resultado[0]
            exactitudes = resultado[1]

            for algoritmo in tablas:
                label = QtWidgets.QLabel(self)
                label.setText(algoritmo + ", exactitud promedio: " + str(exactitudes[algoritmo]))
                self.verticalLayout.addWidget(label)

                tabla = QtWidgets.QTableView(self.frameTablas)
                tabla.setModel(TableModelPandas(tablas[algoritmo]))
                self.verticalLayout.addWidget(tabla)
        else:
            tabla = QtWidgets.QTableView(self.frameTablas)
            tabla.setModel(TableModelPandas(resultado))
            self.verticalLayout.addWidget(tabla)

    def eliminar_tablas(self):
        """ Elimina las tablas """
        for i in reversed(range(self.verticalLayout.count())): 
            widgetAEliminar = self.verticalLayout.itemAt(i).widget()
            self.verticalLayout.removeWidget(widgetAEliminar)
            widgetAEliminar.setParent(None)