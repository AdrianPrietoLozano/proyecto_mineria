# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_descripcion_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(554, 303)
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
        self.textDescripcion = QtWidgets.QPlainTextEdit(Form)
        self.textDescripcion.setObjectName("textDescripcion")
        self.verticalLayout.addWidget(self.textDescripcion)
        self.btnActualizar = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnActualizar.sizePolicy().hasHeightForWidth())
        self.btnActualizar.setSizePolicy(sizePolicy)
        self.btnActualizar.setObjectName("btnActualizar")
        self.verticalLayout.addWidget(self.btnActualizar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Descripción del conjunto de datos"))
        self.label.setText(_translate("Form", "Descripción del conjunto de datos"))
        self.btnActualizar.setText(_translate("Form", "Actualizar y cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
