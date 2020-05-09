from ventana_k_fold_ui import *
from algoritmos.k_fold import KFoldCrossValidation
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget

class VentanaKFold(QWidget, Ui_Form):

    def __init__(self, data, target, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.k_fold = KFoldCrossValidation(data, target)

        self.btnAceptar.clicked.connect(self.iniciar_evaluacion)

    def iniciar_evaluacion(self):
        self.tablaResultado.setModel() # limpia la tabla
        self.btnAceptar.setEnabled(False) # desactiva boton

        num_folds = int(self.numFolds.currentText())
        self.k_fold.setK(num_folds)
        resultado = self.k_fold.validation()
        self.tablaResultado.setModel(TableModelPandas(resultado))
        self.btnAceptar.setEnabled(True)