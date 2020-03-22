from ventana_histograma_ui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
import os
import matplotlib.pyplot as plt
import seaborn as sns


class histograma(QWidget, Ui_Form):
    num_version = 1

    def __init__(self, conjunto_datos,nombre, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.conjunto = conjunto_datos
        self.nombre = nombre

        self.btnGuardar.clicked.connect(self.guardar)
        self.generar_Histograma()

    
    def generar_Histograma(self):
        carpetaAux = "generarHistograma"
        if not os.path.isdir(carpetaAux):
            self.crearCarpeta(carpetaAux)        
        nombreCarpeta = carpetaAux + "/"
        nombreHistograma = "histograma.png"
        #plt.figure(figsize = (10, 0))
        sns.catplot(x= self.nombre, hue= self.conjunto.getTarget(), kind="count",palette="pastel", edgecolor=".6",data= self.conjunto.panda)
        plt.savefig(nombreCarpeta + nombreHistograma)
        grafica = QPixmap(nombreCarpeta + nombreHistograma)
        self.label.setPixmap(grafica)


    def crearCarpeta(self, carpeta):
        try:
            os.mkdir(carpeta)
        except:
            pass


    def guardar(self):
        ruta = self.conjunto.getRutaRespaldos()
        nomFinal = str(histograma.num_version) + "_histograma_" + self.nombre + ".png"
        
        if not os.path.isdir(ruta):
            self.crearCarpeta(ruta)
        #plt.figure(figsize = (10, 0))
        sns.catplot(x= self.nombre, hue= self.conjunto.getTarget(), kind="count",palette="pastel", edgecolor=".6",data= self.conjunto.panda)
        plt.savefig(ruta + nomFinal)
        histograma.num_version += 1

	