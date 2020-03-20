# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_boxplot_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_histograma(object):
    def setupUi(self, histograma):
        histograma.setObjectName("histograma")
        histograma.resize(928, 449)
        self.verticalLayout = QtWidgets.QVBoxLayout(histograma)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(histograma)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btnGuardar = QtWidgets.QPushButton(histograma)
        self.btnGuardar.setObjectName("btnGuardar")
        self.verticalLayout.addWidget(self.btnGuardar)

        self.retranslateUi(histograma)
        QtCore.QMetaObject.connectSlotsByName(histograma)

    def retranslateUi(self, histograma):
        _translate = QtCore.QCoreApplication.translate
        histograma.setWindowTitle(_translate("histograma", "BoxPlot"))
        self.label.setText(_translate("histograma", "TextLabel"))
        self.btnGuardar.setText(_translate("histograma", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    histograma = QtWidgets.QWidget()
    ui = Ui_histograma()
    ui.setupUi(histograma)
    histograma.show()
    sys.exit(app.exec_())
