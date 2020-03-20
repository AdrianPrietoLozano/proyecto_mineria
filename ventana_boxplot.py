from ventana_boxplot_ui import *
from PyQt5.QtWidgets import QWidget


class boxplot(QWidget, Ui_Form):
    def __init__(self, conjunto_datos,nombre,*args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.conjunto = conjunto_datos
        self.nombre = nombre
        self.btnGuardar.clicked.connect(self.guardar)
        
    
    def generar_BoxPlot():
        pass
    
    def guardar():
        pass


