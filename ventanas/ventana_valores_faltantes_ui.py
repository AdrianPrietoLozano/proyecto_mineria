# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_valores_faltantes_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.labelDescripcion = QtWidgets.QLabel(Form)
        self.labelDescripcion.setObjectName("labelDescripcion")
        self.verticalLayout.addWidget(self.labelDescripcion)
        self.textFaltantes = QtWidgets.QPlainTextEdit(Form)
        self.textFaltantes.setEnabled(True)
        self.textFaltantes.setReadOnly(True)
        self.textFaltantes.setObjectName("textFaltantes")
        self.verticalLayout.addWidget(self.textFaltantes)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCopiar = QtWidgets.QPushButton(self.frame)
        self.btnCopiar.setObjectName("btnCopiar")
        self.horizontalLayout.addWidget(self.btnCopiar)
        self.btnCerrar = QtWidgets.QPushButton(self.frame)
        self.btnCerrar.setObjectName("btnCerrar")
        self.horizontalLayout.addWidget(self.btnCerrar)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Valores faltantes"))
        self.label.setText(_translate("Form", "Instancias con valores faltantes"))
        self.labelDescripcion.setText(_translate("Form", "Identificadores de las instancias que tiene valores faltantes para el atributo "))
        self.btnCopiar.setText(_translate("Form", "Copiar"))
        self.btnCerrar.setText(_translate("Form", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
