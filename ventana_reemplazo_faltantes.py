from ventana_reemplazo_faltantes_ui import *
from PyQt5.QtWidgets import QWidget
from algoritmos.reemplazo_faltantes import *
import numpy as np
import pandas


class VentanaReemplazoFaltantes(QWidget, Ui_Form):

    def __init__(self, data, target, simbolo_faltante, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.simbolo_faltante = simbolo_faltante
        self.data = data.replace(self.simbolo_faltante, np.nan).apply(pandas.to_numeric, errors="ignore")
        self.target = target
        self.atributos_numericos_modificar = []
        self.target_es_numerico = False

        if self.target is None or self.target == "" or self.target not in self.data.columns:
            self.groupBoxTarget.setVisible(False)
            self.target = None
        else:
            if np.issubdtype(self.data[self.target].dtype, np.number):
                self.radioButtonTarget.setText("media")
                self.target_es_numerico = True

        self.btnAceptar.clicked.connect(self.iniciar_reemplazo)

        self._llenar_interfaz()

    def iniciar_reemplazo(self):
        metodos = {}
        for atributo in self.atributos_numericos_modificar:
            if atributo == self.target:
                continue

            radio = self.findChild(QtWidgets.QRadioButton, "media" + atributo)
            if radio != None:
                metodos[atributo] = "media" if radio.isChecked() else "mediana"

        reemplazo = ReemplazoFaltantes(self.data, self.target, self.simbolo_faltante, metodos)
        if self.groupBoxTarget.isVisible(): # si el target esta definido
            if self.radioButtonTarget.isChecked():
                if self.target_es_numerico: # si el target es numérico se elige la media
                    metodo_target = "media"
                    reemplazo.reemplazar_target_por_media()
                else: # si el target no es numerico se elige la moda
                    metodo_target = "moda"
                    reemplazo.reemplazar_target_por_moda()
            else:
                metodo_target = "eliminar"
                reemplazo.eliminar_filas_target_faltante()
        
        reemplazo.iniciar_reemplazo()
        print(reemplazo.data)
        

    def _llenar_interfaz(self):
        pos = 0
        for atributo in self.data.columns:
            if atributo == self.target:
                self.labelTarget.setText(atributo)
            if np.issubdtype(self.data[atributo].dtype, np.number):
                self._generar_frame(atributo, pos)
                self.atributos_numericos_modificar.append(atributo)
                pos += 1

    def _generar_frame(self, atributo, pos):
        label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        label.setObjectName("label" + atributo)
        label.setText(atributo)
        self.formLayout.setWidget(pos, QtWidgets.QFormLayout.LabelRole, label)

        frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        frame.setMinimumSize(QtCore.QSize(0, 20))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame" + atributo)
        horizontalLayout = QtWidgets.QHBoxLayout(frame)
        horizontalLayout.setContentsMargins(9, 2, 0, 2)

        radioButtonMedia = QtWidgets.QRadioButton(frame)
        radioButtonMedia.setObjectName("media" + atributo)
        radioButtonMedia.setText("Media")
        horizontalLayout.addWidget(radioButtonMedia)

        radioButtonMediana = QtWidgets.QRadioButton(frame)
        radioButtonMediana.setObjectName("mediana" + atributo)
        radioButtonMediana.setText("Mediana")
        horizontalLayout.addWidget(radioButtonMediana)

        if self.es_casi_distribucion_normal(atributo):
            radioButtonMedia.setChecked(True)
        else:
            radioButtonMediana.setChecked(True)

        self.formLayout.setWidget(pos, QtWidgets.QFormLayout.FieldRole, frame)

    def es_casi_distribucion_normal(self, atributo):
        # FALTA DETECTAR SI UNA DISTRIBUCIÓN ES NORMAL
        return True