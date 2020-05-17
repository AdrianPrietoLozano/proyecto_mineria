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

        self.btnAceptar.clicked.connect(self.iniciar_algoritmo)

    def iniciar_algoritmo(self):
        self.btnAceptar.setEnabled(False) # desactiva boton
        self.tablaResultado.setModel(None)
        self.labelPromedioSilhouette.setText("")
        self.repaint() # para que se actualice la etiqueta

        k = self.spinBoxK.value()
        corridas = self.spinBoxCorridas.value()
        iteraciones = self.spinBoxIteraciones.value()

        self.kmeans.setCorridas(corridas)
        self.kmeans.setIteraciones(iteraciones)

        resultados = self.kmeans.generar_clusters(n_clusters=k)
        self.data["Cluster"] = resultados[0]
        self.data["Silhouette"] = resultados[1]
        promedio_silhouette = resultados[2]

        self.tablaResultado.setModel(TableModelPandas(self.data))
        self.labelPromedioSilhouette.setText("Silhouette score: " + \
            str(promedio_silhouette))

        self.btnAceptar.setEnabled(True)

