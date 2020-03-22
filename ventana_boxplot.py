from ventana_boxplot_ui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
import os
import matplotlib.pyplot as plt
import seaborn as sns



class boxplot(QWidget, Ui_Form):
    
    num_version = 1

    def __init__(self, conjunto_datos,nombre,*args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.conjunto = conjunto_datos
        self.nombre = nombre
        self.btnGuardar.clicked.connect(self.guardar)
        self.generar_BoxPlot()
        
        
    
    def generar_BoxPlot(self):
        carpetaAux = "generarBoxplot"
        if not os.path.isdir(carpetaAux):
            self.crearCarpeta(carpetaAux)        
        nombreCarpeta = carpetaAux + "/"
        nombreBoxplot = "Boxplot.png"
        plt.figure(figsize = (16, 6))
        sns.boxplot(y = self.conjunto.getTarget(), x = self.nombre, data = self.conjunto.panda, palette="Blues")
        plt.savefig(nombreCarpeta + nombreBoxplot)
        grafica = QPixmap(nombreCarpeta + nombreBoxplot)
        self.label.setPixmap(grafica)


    def crearCarpeta(self, carpeta):
        try:
            os.mkdir(carpeta)
        except:
            pass


    def guardar(self):
        ruta = self.conjunto.getRutaRespaldos()
        nomFinal = str(boxplot.num_version) + "_boxplot_" + self.nombre + ".png"
        
        if not os.path.isdir(ruta):
            self.crearCarpeta(ruta)
        plt.figure(figsize = (16, 6))
        sns.boxplot(y = self.conjunto.getTarget(), x = self.nombre, data = self.conjunto.panda, palette="Blues")
        plt.savefig(ruta + nomFinal)
        boxplot.num_version += 1
    
    #1_boxplot_atributo


