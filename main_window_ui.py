# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.groupBox.setPalette(palette)
        self.groupBox.setObjectName("groupBox")
        self.groupBoxNumericos = QtWidgets.QGroupBox(self.groupBox)
        self.groupBoxNumericos.setGeometry(QtCore.QRect(10, 23, 211, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxNumericos.sizePolicy().hasHeightForWidth())
        self.groupBoxNumericos.setSizePolicy(sizePolicy)
        self.groupBoxNumericos.setObjectName("groupBoxNumericos")
        self.comboBoxNumericos = QtWidgets.QComboBox(self.groupBoxNumericos)
        self.comboBoxNumericos.setGeometry(QtCore.QRect(10, 23, 191, 20))
        self.comboBoxNumericos.setObjectName("comboBoxNumericos")
        self.label = QtWidgets.QLabel(self.groupBoxNumericos)
        self.label.setGeometry(QtCore.QRect(10, 49, 37, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBoxNumericos)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 20, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBoxNumericos)
        self.label_3.setGeometry(QtCore.QRect(10, 101, 37, 16))
        self.label_3.setObjectName("label_3")
        self.nombreAtributoNumerico = QtWidgets.QLineEdit(self.groupBoxNumericos)
        self.nombreAtributoNumerico.setGeometry(QtCore.QRect(50, 50, 151, 20))
        self.nombreAtributoNumerico.setObjectName("nombreAtributoNumerico")
        self.dominioAtributoNumerico = QtWidgets.QLineEdit(self.groupBoxNumericos)
        self.dominioAtributoNumerico.setGeometry(QtCore.QRect(50, 101, 151, 20))
        self.dominioAtributoNumerico.setObjectName("dominioAtributoNumerico")
        self.tipoAtributoNumerico = QtWidgets.QLineEdit(self.groupBoxNumericos)
        self.tipoAtributoNumerico.setGeometry(QtCore.QRect(50, 75, 151, 20))
        self.tipoAtributoNumerico.setObjectName("tipoAtributoNumerico")
        self.btnActualizarNumericos = QtWidgets.QPushButton(self.groupBoxNumericos)
        self.btnActualizarNumericos.setGeometry(QtCore.QRect(50, 127, 151, 23))
        self.btnActualizarNumericos.setObjectName("btnActualizarNumericos")
        self.label_12 = QtWidgets.QLabel(self.groupBoxNumericos)
        self.label_12.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_12.setObjectName("label_12")
        self.labelFueraDominioNumerico = QtWidgets.QLabel(self.groupBoxNumericos)
        self.labelFueraDominioNumerico.setGeometry(QtCore.QRect(100, 160, 91, 16))
        self.labelFueraDominioNumerico.setObjectName("labelFueraDominioNumerico")
        self.groupBoxCategoricos = QtWidgets.QGroupBox(self.groupBox)
        self.groupBoxCategoricos.setGeometry(QtCore.QRect(10, 229, 211, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxCategoricos.sizePolicy().hasHeightForWidth())
        self.groupBoxCategoricos.setSizePolicy(sizePolicy)
        self.groupBoxCategoricos.setObjectName("groupBoxCategoricos")
        self.comboBoxCategoricos = QtWidgets.QComboBox(self.groupBoxCategoricos)
        self.comboBoxCategoricos.setGeometry(QtCore.QRect(10, 23, 191, 20))
        self.comboBoxCategoricos.setObjectName("comboBoxCategoricos")
        self.label_4 = QtWidgets.QLabel(self.groupBoxCategoricos)
        self.label_4.setGeometry(QtCore.QRect(10, 49, 37, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBoxCategoricos)
        self.label_5.setGeometry(QtCore.QRect(10, 75, 20, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBoxCategoricos)
        self.label_6.setGeometry(QtCore.QRect(10, 101, 37, 16))
        self.label_6.setObjectName("label_6")
        self.nombreAtributoCate = QtWidgets.QLineEdit(self.groupBoxCategoricos)
        self.nombreAtributoCate.setGeometry(QtCore.QRect(53, 49, 151, 20))
        self.nombreAtributoCate.setObjectName("nombreAtributoCate")
        self.dominioAtributoCate = QtWidgets.QLineEdit(self.groupBoxCategoricos)
        self.dominioAtributoCate.setGeometry(QtCore.QRect(53, 101, 151, 20))
        self.dominioAtributoCate.setObjectName("dominioAtributoCate")
        self.tipoAtributoCate = QtWidgets.QLineEdit(self.groupBoxCategoricos)
        self.tipoAtributoCate.setGeometry(QtCore.QRect(53, 75, 151, 20))
        self.tipoAtributoCate.setObjectName("tipoAtributoCate")
        self.btnActualizarCategoricos = QtWidgets.QPushButton(self.groupBoxCategoricos)
        self.btnActualizarCategoricos.setGeometry(QtCore.QRect(53, 127, 151, 23))
        self.btnActualizarCategoricos.setObjectName("btnActualizarCategoricos")
        self.label_13 = QtWidgets.QLabel(self.groupBoxCategoricos)
        self.label_13.setGeometry(QtCore.QRect(10, 160, 86, 16))
        self.label_13.setObjectName("label_13")
        self.labelFueraDominioCategorico = QtWidgets.QLabel(self.groupBoxCategoricos)
        self.labelFueraDominioCategorico.setGeometry(QtCore.QRect(100, 160, 101, 16))
        self.labelFueraDominioCategorico.setObjectName("labelFueraDominioCategorico")
        self.groupBoxCategoricos.raise_()
        self.groupBoxNumericos.raise_()
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 41, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 31, 16))
        self.label_11.setObjectName("label_11")
        self.labelNumInstancias = QtWidgets.QLabel(self.groupBox_2)
        self.labelNumInstancias.setGeometry(QtCore.QRect(120, 20, 47, 13))
        self.labelNumInstancias.setObjectName("labelNumInstancias")
        self.labelNumAtributos = QtWidgets.QLabel(self.groupBox_2)
        self.labelNumAtributos.setGeometry(QtCore.QRect(120, 40, 47, 13))
        self.labelNumAtributos.setObjectName("labelNumAtributos")
        self.labelTarget = QtWidgets.QLabel(self.groupBox_2)
        self.labelTarget.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.labelTarget.setObjectName("labelTarget")
        self.labelValorFaltante = QtWidgets.QLabel(self.groupBox_2)
        self.labelValorFaltante.setGeometry(QtCore.QRect(130, 80, 47, 13))
        self.labelValorFaltante.setObjectName("labelValorFaltante")
        self.labelRuta = QtWidgets.QLabel(self.groupBox_2)
        self.labelRuta.setGeometry(QtCore.QRect(40, 100, 47, 13))
        self.labelRuta.setObjectName("labelRuta")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.frame)
        self.tabla = QtWidgets.QTableView(self.centralwidget)
        self.tabla.setSortingEnabled(True)
        self.tabla.setObjectName("tabla")
        self.horizontalLayout.addWidget(self.tabla)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Atributos"))
        self.groupBoxNumericos.setTitle(_translate("MainWindow", "Numéricos"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Tipo"))
        self.label_3.setText(_translate("MainWindow", "Dominio"))
        self.btnActualizarNumericos.setText(_translate("MainWindow", "Actualizar"))
        self.label_12.setText(_translate("MainWindow", "Fuera de dominio:"))
        self.labelFueraDominioNumerico.setText(_translate("MainWindow", "N/A"))
        self.groupBoxCategoricos.setTitle(_translate("MainWindow", "Categóricos"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_5.setText(_translate("MainWindow", "Tipo"))
        self.label_6.setText(_translate("MainWindow", "Dominio"))
        self.btnActualizarCategoricos.setText(_translate("MainWindow", "Actualizar"))
        self.label_13.setText(_translate("MainWindow", "Fuera de dominio:"))
        self.labelFueraDominioCategorico.setText(_translate("MainWindow", "N/A"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Información"))
        self.label_7.setText(_translate("MainWindow", "Número de instancias: "))
        self.label_8.setText(_translate("MainWindow", "Número de atributos: "))
        self.label_9.setText(_translate("MainWindow", "Target: "))
        self.label_10.setText(_translate("MainWindow", "Varialble valor faltante: "))
        self.label_11.setText(_translate("MainWindow", "Ruta: "))
        self.labelNumInstancias.setText(_translate("MainWindow", "N/A"))
        self.labelNumAtributos.setText(_translate("MainWindow", "N/A"))
        self.labelTarget.setText(_translate("MainWindow", "N/A"))
        self.labelValorFaltante.setText(_translate("MainWindow", "N/A"))
        self.labelRuta.setText(_translate("MainWindow", "N/A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
