# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo_elegir_propiedades_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(437, 158)
        self.lineEditRuta = QtWidgets.QLineEdit(Dialog)
        self.lineEditRuta.setGeometry(QtCore.QRect(20, 79, 311, 21))
        self.lineEditRuta.setObjectName("lineEditRuta")
        self.elegir_archivo = QtWidgets.QPushButton(Dialog)
        self.elegir_archivo.setGeometry(QtCore.QRect(340, 80, 81, 21))
        self.elegir_archivo.setObjectName("elegir_archivo")
        self.botonAceptar = QtWidgets.QPushButton(Dialog)
        self.botonAceptar.setGeometry(QtCore.QRect(260, 120, 75, 23))
        self.botonAceptar.setObjectName("botonAceptar")
        self.botonCancelar = QtWidgets.QPushButton(Dialog)
        self.botonCancelar.setGeometry(QtCore.QRect(350, 120, 75, 23))
        self.botonCancelar.setObjectName("botonCancelar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.elegir_archivo.setText(_translate("Dialog", "Elegir archivo"))
        self.botonAceptar.setText(_translate("Dialog", "OK"))
        self.botonCancelar.setText(_translate("Dialog", "Cancelar"))
        self.label.setText(_translate("Dialog", "Selecciona el archivo de propiedades (.json)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
