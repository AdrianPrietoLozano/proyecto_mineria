from ventana_histograma_ui import *
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from pandas.api.types import is_numeric_dtype
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
        self.figura = None
        self.datos_panda = self.quitarValoresFaltantes()
        self.btnGuardar.clicked.connect(self.guardar)
        self.generar_Histograma()

    
    def generar_Histograma(self):
        if is_numeric_dtype(self.datos_panda[self.nombre]):
            QMessageBox.critical(self, "Error", "El atributo " + self.nombre + " no es categórico")
            self.close()
            return

        carpetaAux = "generarHistograma"
        if not os.path.isdir(carpetaAux):
            self.crearCarpeta(carpetaAux)        
        nombreCarpeta = carpetaAux + "/"
        nombreHistograma = "histograma.png"
        #plt.figure(figsize = (10, 0))

        #sns.catplot(x=self.nombre, hue="class", kind="count", data=self.conjunto.panda)
        #sns.catplot(x= self.nombre, hue= self.conjunto.getTarget(), kind="count", palette="pastel", edgecolor=".6", data=self.conjunto.panda)


        target = self.conjunto.getTarget()
        if target != None and target != "" and target in self.conjunto.getNombresAtributos():
            # hacer boxplot como lo 
            self.figura = sns.catplot(x=self.nombre, hue=target, kind="count", palette="pastel", data=self.datos_panda)
        else:
            self.figura = sns.catplot(x=self.nombre, kind="count", palette="pastel", data=self.datos_panda)

        self.figura.set_xticklabels(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(nombreCarpeta + nombreHistograma)
        grafica = QPixmap(nombreCarpeta + nombreHistograma)
        self.label.setPixmap(grafica)


    def crearCarpeta(self, carpeta):
        try:
            os.mkdir(carpeta)
        except:
            pass


    def guardar(self):
        ruta_respaldos = self.conjunto.getRutaRespaldos()
        nomFinal = str(histograma.num_version) + "_histograma_" + self.nombre + ".png"
        
        if not os.path.isdir(ruta_respaldos):
            self.crearCarpeta(ruta_respaldos)
        #plt.figure(figsize = (10, 0))
        
        plt.savefig(ruta_respaldos + nomFinal)
        histograma.num_version += 1
        QMessageBox.information(self, "Guardado", "Se guardó en " + ruta_respaldos + nomFinal)


    def quitarValoresFaltantes(self):
        """Retorna un nuevo pandas sin los valores faltantes"""
        # quita valores faltantes del atributo al que se hará el boxplot
        aux = self.conjunto.panda[self.conjunto.panda[self.nombre] != self.conjunto.getSimboloFaltante()]

        target = self.conjunto.getTarget()
        if target != None and target != "" and target in self.conjunto.getNombresAtributos(): # si el target esta definido entoces quita sus valores faltantes
            aux = aux[aux[target] != self.conjunto.getSimboloFaltante()]

        #aux = aux.infer_objects() # vuelve a verificar los tipos de datos

        # intenta cambiar el tipo a numerico
        try:
            aux[self.nombre] = pd.to_numeric(aux[self.nombre])
        except:
            pass

        return aux

	