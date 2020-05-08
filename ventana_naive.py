from ventana_naive_ui import *
from algoritmos.naive import NaiveBayes
import numpy as np
import pandas
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableView, QLabel, QComboBox


class VentanaNaiveBayes(QWidget, Ui_Form):

    def __init__(self, data, target,  *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.data = data
        self.target = target
        self.naive = NaiveBayes(self.data, self.target)

        self.generar_campos()
        self.btnAceptar.clicked.connect(self.procesar_instancia)

    def procesar_instancia(self):
        """ Se ejecuta al presionar el boton aceptar """
        #self.tablaDistancias.setModel(None) # limpia la tabla
        self.limpiar_datos()

        lista_valores = self.obtener_valores_campos()

        if len(lista_valores) == 0:
            QMessageBox.critical(self, "Error", "Debes llenar los campos")
        else:
            # Falta verificar que los datos sean del tipo correcto
            resultado, procedimiento = self.naive.get_prediccion(lista_valores)
            self.mostrar_tablas_frecuencias()
            self.mostrar_tablas_verosimilitudes()
            self.textProcedimiento.setPlainText(procedimiento)

            target_final = max(resultado, key=resultado.get)
            self.labelResultado.setText(target_final)



    def obtener_valores_campos(self):
        """ Retorna en una lista los valores de los atributos insetados por el usuario """
        atributos = self.data.columns
        diccionario_valores = {}

        for atributo in atributos:
            if atributo == self.target:
                continue
            tipo_atributo = self.data[atributo].dtype

            if np.issubdtype(tipo_atributo, np.number):
                edit = self.findChild(QtWidgets.QLineEdit, "edit_" + atributo)
                val = edit.text()
                try: # hace la conversion de string a numérico
                    val = float(val)
                except:
                    pass

            else:
                combo = self.findChild(QtWidgets.QComboBox, "combo_" + atributo)
                val = combo.currentText()

            if val != "":
                diccionario_valores[atributo] = val

        return diccionario_valores

    def generar_campos(self):
        """Genera los campos dinamicamente y los muestra"""
        atributos = self.data.columns

        # Crea QLineEdit y QLabel dinamicamente
        for i in range(len(atributos)):
            if atributos[i] == self.target:
                continue

            # si es numérico
            if np.issubdtype(self.data[atributos[i]].dtype, np.number):
                field = QtWidgets.QLineEdit(self.formLayoutWidget)
                field.setObjectName("edit_" + atributos[i])

            else: # si es categórico
                field = QComboBox(self.formLayoutWidget)
                field.setObjectName("combo_" + atributos[i])
                field.addItems([""] + self.data[atributos[i]].unique().astype(str).tolist())

            label = QtWidgets.QLabel(self.formLayoutWidget)
            label.setText(atributos[i])

            self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, label)
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, field)

        #self.scrollAreaWidgetContents.setLayout(self.formLayout)

    def mostrar_tablas_frecuencias(self):
        frecuencias = self.naive.frecuencias
        for atributo in frecuencias:
            label = QLabel(self)
            label.setText(atributo)
            self.verticalLayout_6.addWidget(label)

            tabla = QTableView(self.scrollAreaWidgetContents)
            tabla.setMinimumSize(QtCore.QSize(0, 120))
            modelo = TableModelPandas(frecuencias[atributo])
            tabla.setModel(modelo)

            self.verticalLayout_6.addWidget(tabla)

        label = QLabel(self)
        label.setText(self.target)
        self.verticalLayout_6.addWidget(label)

        tabla = QTableView(self.scrollAreaWidgetContents)
        tabla.setMinimumSize(QtCore.QSize(0, 120))
        modelo = TableModelPandas(self.naive.frec_target)
        tabla.setModel(modelo)

        self.verticalLayout_6.addWidget(tabla)
        

    def mostrar_tablas_verosimilitudes(self):
        for atributo in self.naive.probabilidades:
            label = QLabel(self)
            label.setText(atributo)
            self.verticalLayout_7.addWidget(label)

            tabla = QTableView(self.scrollAreaWidgetContents_2)
            tabla.setMinimumSize(QtCore.QSize(0, 120))
            modelo = TableModelPandas(self.naive.probabilidades[atributo])
            tabla.setModel(modelo)

            self.verticalLayout_7.addWidget(tabla)


    def limpiar_datos(self):
        
        #### limpiar las tablas ####

        self.textProcedimiento.clear()
        self.labelResultado.clear()

    
    