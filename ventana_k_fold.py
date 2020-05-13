from ventana_k_fold_ui import *
#from algoritmos.k_fold import KFoldCrossValidation
from k_fold import KFoldCrossValidation
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget

class VentanaKFold(QWidget, Ui_Form):

    def __init__(self, data, target, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.data = data
        self.target = target
        self.es_multi_clase = True

        self.btnAceptar.clicked.connect(self.iniciar_evaluacion)
        self.labelCargando.setVisible(False)
        self.INDEX_LEAVE_ONE_OUT = 4

        # si los posibles valores del target son 2 muestra la opcion para
        # elegir el valor positivo y el negativo
        if len(self.data[self.target].unique()) == 2:
            self.es_multi_clase = False
            posibles_valores = self.data[self.target].unique().astype(str).tolist()
            self.comboBoxValorPositivo.addItems(posibles_valores)
        else:
            self.groupBoxValorPositivo.setVisible(False)

    def iniciar_evaluacion(self):
        self.btnAceptar.setEnabled(False) # desactiva boton
        self.labelCargando.setVisible(True)
        self.tablaResultados.setModel(None)
        self.labelAlgoritmo.setText("")
        self.repaint() # para que se actualice la etiqueta

        if self.numFolds.currentIndex() == self.INDEX_LEAVE_ONE_OUT:
            num_folds = len(self.data)
        else:
            num_folds = int(self.numFolds.currentText())

        positivo, negativo = None, None
        if not self.es_multi_clase:
            index_val_positivo = self.comboBoxValorPositivo.currentIndex()
            index_val_negativo = 0 if index_val_positivo == 1 else 1
            val_positivo = self.comboBoxValorPositivo.itemText(index_val_positivo)
            val_negativo = self.comboBoxValorPositivo.itemText(index_val_negativo)

            positivo = val_positivo
            negativo = val_negativo
        
        algoritmo = self.comboBoxAlgoritmo.currentText()
        k_fold = KFoldCrossValidation(self.data, self.target, num_folds,
            algoritmo, positivo, negativo)
        resultado = k_fold.iniciar_validacion()
        self.mostrar_tablas(resultado)
        self.btnAceptar.setEnabled(True)
        self.labelCargando.setVisible(False)


    def mostrar_tablas(self, resultado):
        if self.es_multi_clase:
            tabla = resultado[0]
            exactitud = resultado[1]

            msg = "{}, exactitud promedio: {}".format(self.comboBoxAlgoritmo.currentText(), exactitud)
            self.labelAlgoritmo.setText(msg)
            self.tablaResultados.setModel(TableModelPandas(tabla))
        else:
            self.labelAlgoritmo.setText("")
            self.tablaResultados.setModel(TableModelPandas(resultado))

    """
    def eliminar_tablas(self):
        for i in reversed(range(self.verticalLayout.count())): 
            widgetAEliminar = self.verticalLayout.itemAt(i).widget()
            self.verticalLayout.removeWidget(widgetAEliminar)
            widgetAEliminar.setParent(None)
    """