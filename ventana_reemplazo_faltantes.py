from ventana_reemplazo_faltantes_ui import *
from PyQt5.QtWidgets import QWidget
import numpy as np


class VentanaReemplazoFaltantes(QWidget, Ui_Form):

    def __init__(self, data, target, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.data = data
        self.target = target

        if self.target == None or self.target == "" or self.target not in self.data.columns:
            self.groupBoxTarget.setVisible(False)

        self.btnAceptar.clicked.connect(self.iniciar_reemplazo)

        self._llenar_interfaz()

    def iniciar_reemplazo(self):
        metodos = {}
        for atributo in self.data.columns:
            if atributo == self.target:
                continue

            radio = self.findChild(QtWidgets.QRadioButton, "media" + atributo)
            metodos[atributo] = "media" if radio.isChecked() else "mediana"

        print(metodos)


    def _llenar_interfaz(self):
        pos = 0
        for atributo in self.data.columns:
            if atributo == self.target:
                self.labelTarget.setText(atributo)
            if np.issubdtype(self.data[atributo].dtype, np.number):
                self._generar_frame(atributo, pos)
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

        self.formLayout.setWidget(pos, QtWidgets.QFormLayout.FieldRole, frame)