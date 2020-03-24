from ventana_boxplot_ui import *
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from pandas.api.types import is_numeric_dtype
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class boxplot(QWidget, Ui_Form):
    
    num_version = 1

    def __init__(self, conjunto_datos, nombre, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.conjunto = conjunto_datos
        self.nombre = nombre
        self.figura = None # aquí se guardará el boxplot
        self.btnGuardar.clicked.connect(self.guardar)
        self.datos_panda = self.quitarValoresFaltantes()
        self.generar_BoxPlot()
    


    def generar_BoxPlot(self):

        # si el atributo no es numérico no se puede crear el boxplot
        if not is_numeric_dtype(self.datos_panda[self.nombre]):
            QMessageBox.critical(self, "Error", "El atributo " + self.nombre + " no es numérico")
            self.close()
            return

        carpetaAux = "generarBoxplot"
        if not os.path.isdir(carpetaAux):
            self.crearCarpeta(carpetaAux)        
        nombreCarpeta = carpetaAux + "/"
        nombreBoxplot = "Boxplot.png"
        plt.figure(figsize = (16, 6))

        target = self.conjunto.getTarget()
        if target != None and target != "" and target in self.conjunto.getNombresAtributos():
            # hacer boxplot como lo 
            self.figura = sns.boxplot(y=target, x=self.nombre, data=self.datos_panda, palette="Blues")
        else:
            self.figura = sns.boxplot(x=self.nombre, data=self.datos_panda, palette="Blues")

        plt.savefig(nombreCarpeta + nombreBoxplot)
        grafica = QPixmap(nombreCarpeta + nombreBoxplot)
        self.label.setPixmap(grafica)


        """
        if self.cambiarTipo():
            carpetaAux = "generarBoxplot"
            if not os.path.isdir(carpetaAux):
                self.crearCarpeta(carpetaAux)        
            nombreCarpeta = carpetaAux + "/"
            nombreBoxplot = "Boxplot.png"
            plt.figure(figsize = (16, 6))

            tipoAuxiliar = self.conjunto.panda[self.nombre].dtype
            
            print("Entra breakpoint 1: ", tipoAuxiliar)
            self.conjunto.panda[self.nombre] = self.conjunto.panda[self.nombre].astype("float64")
            print("Entra breakpoint 2: ", self.conjunto.panda[self.nombre].dtype)

            sns.boxplot(y = self.conjunto.getTarget(), x = self.nombre, data = self.conjunto.panda, palette="Blues")

            print("Entra breakpoint 3: ", self.conjunto.panda[self.nombre].dtype)
            self.conjunto.panda[self.nombre] = self.conjunto.panda[self.nombre].astype(tipoAuxiliar)
            print("Entra breakpoint 4: ", self.conjunto.panda[self.nombre].dtype)

            plt.savefig(nombreCarpeta + nombreBoxplot)
            grafica = QPixmap(nombreCarpeta + nombreBoxplot)
            self.label.setPixmap(grafica)
        else:
            print("No se puede generar el Boxplot")
            self.close()
        """


    def crearCarpeta(self, carpeta):
        try:
            os.mkdir(carpeta)
        except:
            pass


    def guardar(self):
        self.close()
        """
        ruta_respaldos = self.conjunto.getRutaRespaldos()
        nomFinal = str(boxplot.num_version) + "_boxplot_" + self.nombre + ".png"
        
        if not os.path.isdir(ruta_respaldos):
            self.crearCarpeta(ruta_respaldos)
        self.figura.get_figure().savefig(ruta_respaldos + nomFinal)
        boxplot.num_version += 1

        QMessageBox.information(self, "Guardado", "Se guardó en " + ruta_respaldos + nomFinal)
        """
    
    #1_boxplot_atributo

    def quitarValoresFaltantes(self):
        """Retorna un nuevo pandas sin los valores faltantes"""
        # quita valores faltantes del atributo al que se hará el boxplot
        aux = self.conjunto.panda[self.conjunto.panda[self.nombre] != self.conjunto.getSimboloFaltante()]

        target = self.conjunto.getTarget()
        if target != None and target != "" and target in self.conjunto.getNombresAtributos(): # si el target esta definido entoces quita sus valores faltantes
            aux = aux[aux[target] != self.conjunto.getSimboloFaltante()]

        #aux = aux.infer_objects() # vuelve a verificar los tipos de datos

        # intenta cambier el tipo a numerico
        try:
            aux[self.nombre] = pd.to_numeric(aux[self.nombre])
        except:
            pass

        return aux

