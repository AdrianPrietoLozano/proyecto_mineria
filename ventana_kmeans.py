from ventana_k_means_ui import *
from algoritmos.kmeans import KMeans
import numpy as np
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget, QMessageBox

class VentanaKMeans(QWidget, Ui_Form):

    def __init__(self, data, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.data = data
        self.kmeans = KMeans(self.data)

        #self.btnAceptar.clicked.connect(self.procesar_instancia)

