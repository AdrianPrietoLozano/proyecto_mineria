# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_k_means_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(685, 566)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 0, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBoxK = QtWidgets.QSpinBox(self.frame)
        self.spinBoxK.setMinimum(2)
        self.spinBoxK.setMaximum(8)
        self.spinBoxK.setObjectName("spinBoxK")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBoxK)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBoxCorridas = QtWidgets.QSpinBox(self.frame)
        self.spinBoxCorridas.setMinimum(1)
        self.spinBoxCorridas.setMaximum(30)
        self.spinBoxCorridas.setProperty("value", 10)
        self.spinBoxCorridas.setObjectName("spinBoxCorridas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxCorridas)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBoxIteraciones = QtWidgets.QSpinBox(self.frame)
        self.spinBoxIteraciones.setMinimum(1)
        self.spinBoxIteraciones.setMaximum(500)
        self.spinBoxIteraciones.setProperty("value", 100)
        self.spinBoxIteraciones.setObjectName("spinBoxIteraciones")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxIteraciones)
        self.verticalLayout.addLayout(self.formLayout)
        self.btnAceptar = QtWidgets.QPushButton(self.frame)
        self.btnAceptar.setObjectName("btnAceptar")
        self.verticalLayout.addWidget(self.btnAceptar)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.labelPromedioSilhouette = QtWidgets.QLabel(self.frame_2)
        self.labelPromedioSilhouette.setText("")
        self.labelPromedioSilhouette.setObjectName("labelPromedioSilhouette")
        self.verticalLayout_2.addWidget(self.labelPromedioSilhouette)
        self.tablaResultado = QtWidgets.QTableView(self.frame_2)
        self.tablaResultado.setObjectName("tablaResultado")
        self.verticalLayout_2.addWidget(self.tablaResultado)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "K-Means"))
        self.label.setText(_translate("Form", "K"))
        self.label_2.setText(_translate("Form", "Corridas"))
        self.label_3.setText(_translate("Form", "Iteraciones"))
        self.btnAceptar.setText(_translate("Form", "Aceptar"))
        self.label_4.setText(_translate("Form", "Resultado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
