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
        MainWindow.resize(765, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 690))
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
        self.groupBoxAtributos = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAtributos.sizePolicy().hasHeightForWidth())
        self.groupBoxAtributos.setSizePolicy(sizePolicy)
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
        self.groupBoxAtributos.setPalette(palette)
        self.groupBoxAtributos.setObjectName("groupBoxAtributos")
        self.comboBoxAtributos = QtWidgets.QComboBox(self.groupBoxAtributos)
        self.comboBoxAtributos.setGeometry(QtCore.QRect(10, 20, 211, 20))
        self.comboBoxAtributos.setStyleSheet("QComboBox QAbstractItemView::item { margin: 10px; padding: 10px; }")
        self.comboBoxAtributos.setIconSize(QtCore.QSize(12, 12))
        self.comboBoxAtributos.setObjectName("comboBoxAtributos")
        self.label = QtWidgets.QLabel(self.groupBoxAtributos)
        self.label.setGeometry(QtCore.QRect(10, 59, 37, 16))
        self.label.setObjectName("label")
        self.btnActualizar = QtWidgets.QPushButton(self.groupBoxAtributos)
        self.btnActualizar.setGeometry(QtCore.QRect(50, 137, 171, 23))
        self.btnActualizar.setObjectName("btnActualizar")
        self.label_12 = QtWidgets.QLabel(self.groupBoxAtributos)
        self.label_12.setGeometry(QtCore.QRect(10, 210, 91, 16))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.groupBoxAtributos)
        self.label_14.setGeometry(QtCore.QRect(10, 240, 91, 16))
        self.label_14.setObjectName("label_14")
        self.editDominioAtributo = QtWidgets.QLineEdit(self.groupBoxAtributos)
        self.editDominioAtributo.setGeometry(QtCore.QRect(50, 111, 171, 20))
        self.editDominioAtributo.setObjectName("editDominioAtributo")
        self.editNombreAtributo = QtWidgets.QLineEdit(self.groupBoxAtributos)
        self.editNombreAtributo.setGeometry(QtCore.QRect(50, 60, 171, 20))
        self.editNombreAtributo.setObjectName("editNombreAtributo")
        self.label_3 = QtWidgets.QLabel(self.groupBoxAtributos)
        self.label_3.setGeometry(QtCore.QRect(10, 111, 37, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBoxAtributos)
        self.label_2.setGeometry(QtCore.QRect(10, 85, 20, 16))
        self.label_2.setObjectName("label_2")
        self.labelFueraDominio = QtWidgets.QLabel(self.groupBoxAtributos)
        self.labelFueraDominio.setGeometry(QtCore.QRect(100, 210, 91, 16))
        self.labelFueraDominio.setObjectName("labelFueraDominio")
        self.labelValoresFaltantes = QtWidgets.QLabel(self.groupBoxAtributos)
        self.labelValoresFaltantes.setGeometry(QtCore.QRect(100, 240, 91, 16))
        self.labelValoresFaltantes.setObjectName("labelValoresFaltantes")
        self.line = QtWidgets.QFrame(self.groupBoxAtributos)
        self.line.setGeometry(QtCore.QRect(0, 200, 230, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.contenedorMetricas = QtWidgets.QFrame(self.groupBoxAtributos)
        self.contenedorMetricas.setGeometry(QtCore.QRect(0, 260, 231, 101))
        self.contenedorMetricas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedorMetricas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedorMetricas.setObjectName("contenedorMetricas")
        self.label_17 = QtWidgets.QLabel(self.contenedorMetricas)
        self.label_17.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.label_17.setObjectName("label_17")
        self.labelMedia = QtWidgets.QLabel(self.contenedorMetricas)
        self.labelMedia.setGeometry(QtCore.QRect(60, 27, 131, 20))
        self.labelMedia.setObjectName("labelMedia")
        self.label_16 = QtWidgets.QLabel(self.contenedorMetricas)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 41, 16))
        self.label_16.setObjectName("label_16")
        self.labelMediana = QtWidgets.QLabel(self.contenedorMetricas)
        self.labelMediana.setGeometry(QtCore.QRect(60, 48, 131, 20))
        self.labelMediana.setObjectName("labelMediana")
        self.label_15 = QtWidgets.QLabel(self.contenedorMetricas)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(self.contenedorMetricas)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_18.setObjectName("label_18")
        self.labelDesviacionEstandar = QtWidgets.QLabel(self.contenedorMetricas)
        self.labelDesviacionEstandar.setGeometry(QtCore.QRect(120, 68, 61, 20))
        self.labelDesviacionEstandar.setObjectName("labelDesviacionEstandar")
        self.btnModas = QtWidgets.QPushButton(self.contenedorMetricas)
        self.btnModas.setGeometry(QtCore.QRect(50, 6, 91, 23))
        self.btnModas.setObjectName("btnModas")
        self.btnEliminarAtributo = QtWidgets.QPushButton(self.groupBoxAtributos)
        self.btnEliminarAtributo.setGeometry(QtCore.QRect(50, 170, 171, 23))
        self.btnEliminarAtributo.setObjectName("btnEliminarAtributo")
        self.btnFueraDominio = QtWidgets.QPushButton(self.groupBoxAtributos)
        self.btnFueraDominio.setGeometry(QtCore.QRect(190, 210, 31, 21))
        self.btnFueraDominio.setObjectName("btnFueraDominio")
        self.btnFaltantes = QtWidgets.QPushButton(self.groupBoxAtributos)
        self.btnFaltantes.setGeometry(QtCore.QRect(190, 240, 31, 21))
        self.btnFaltantes.setObjectName("btnFaltantes")
        self.btnBoxPlot = QtWidgets.QPushButton(self.groupBoxAtributos)
        self.btnBoxPlot.setGeometry(QtCore.QRect(10, 360, 211, 23))
        self.btnBoxPlot.setObjectName("btnBoxPlot")
        self.btnHistograma = QtWidgets.QPushButton(self.groupBoxAtributos)
        self.btnHistograma.setGeometry(QtCore.QRect(10, 360, 211, 23))
        self.btnHistograma.setObjectName("btnHistograma")
        self.comboBoxTipoAtributo = QtWidgets.QComboBox(self.groupBoxAtributos)
        self.comboBoxTipoAtributo.setGeometry(QtCore.QRect(50, 85, 171, 21))
        self.comboBoxTipoAtributo.setIconSize(QtCore.QSize(12, 12))
        self.comboBoxTipoAtributo.setObjectName("comboBoxTipoAtributo")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/numerico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxTipoAtributo.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconos/categorico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxTipoAtributo.addItem(icon1, "")
        self.verticalLayout.addWidget(self.groupBoxAtributos)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 170))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 170))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_8.setObjectName("label_8")
        self.labelNumInstancias = QtWidgets.QLabel(self.groupBox_2)
        self.labelNumInstancias.setGeometry(QtCore.QRect(120, 20, 47, 13))
        self.labelNumInstancias.setObjectName("labelNumInstancias")
        self.labelNumAtributos = QtWidgets.QLabel(self.groupBox_2)
        self.labelNumAtributos.setGeometry(QtCore.QRect(120, 40, 47, 13))
        self.labelNumAtributos.setObjectName("labelNumAtributos")
        self.btnActualizarInfo = QtWidgets.QPushButton(self.groupBox_2)
        self.btnActualizarInfo.setGeometry(QtCore.QRect(80, 140, 141, 23))
        self.btnActualizarInfo.setObjectName("btnActualizarInfo")
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 230, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(0, 0))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEditValorFaltante = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditValorFaltante.setGeometry(QtCore.QRect(60, 90, 161, 20))
        self.lineEditValorFaltante.setObjectName("lineEditValorFaltante")
        self.lineEditRuta = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditRuta.setGeometry(QtCore.QRect(60, 116, 161, 20))
        self.lineEditRuta.setObjectName("lineEditRuta")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 64, 37, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 116, 37, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_6.setObjectName("label_6")
        self.comboBoxTarget = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxTarget.setGeometry(QtCore.QRect(60, 65, 161, 21))
        self.comboBoxTarget.setIconSize(QtCore.QSize(12, 12))
        self.comboBoxTarget.setObjectName("comboBoxTarget")
        self.comboBoxTarget.addItem("")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.btnDescripcion = QtWidgets.QPushButton(self.frame)
        self.btnDescripcion.setObjectName("btnDescripcion")
        self.verticalLayout.addWidget(self.btnDescripcion)
        self.horizontalLayout.addWidget(self.frame)
        self.tabla = QtWidgets.QTableView(self.centralwidget)
        self.tabla.setSortingEnabled(False)
        self.tabla.setObjectName("tabla")
        self.horizontalLayout.addWidget(self.tabla)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        self.menuVersiones = QtWidgets.QMenu(self.menubar)
        self.menuVersiones.setObjectName("menuVersiones")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAlgoritmos = QtWidgets.QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName("menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionZero_R = QtWidgets.QAction(MainWindow)
        self.actionZero_R.setObjectName("actionZero_R")
        self.actionOne_R = QtWidgets.QAction(MainWindow)
        self.actionOne_R.setObjectName("actionOne_R")
        self.actionNaive_Bayes = QtWidgets.QAction(MainWindow)
        self.actionNaive_Bayes.setObjectName("actionNaive_Bayes")
        self.actionK_NN = QtWidgets.QAction(MainWindow)
        self.actionK_NN.setObjectName("actionK_NN")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuAlgoritmos.addAction(self.actionZero_R)
        self.menuAlgoritmos.addAction(self.actionOne_R)
        self.menuAlgoritmos.addAction(self.actionNaive_Bayes)
        self.menuAlgoritmos.addAction(self.actionK_NN)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVersiones.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto Minería"))
        self.groupBoxAtributos.setTitle(_translate("MainWindow", "Atributos"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.btnActualizar.setText(_translate("MainWindow", "Actualizar"))
        self.label_12.setText(_translate("MainWindow", "Fuera de dominio:"))
        self.label_14.setText(_translate("MainWindow", "Valores faltantes:"))
        self.label_3.setText(_translate("MainWindow", "Dominio"))
        self.label_2.setText(_translate("MainWindow", "Tipo"))
        self.labelFueraDominio.setText(_translate("MainWindow", "N/A"))
        self.labelValoresFaltantes.setText(_translate("MainWindow", "N/A"))
        self.label_17.setText(_translate("MainWindow", "Mediana:"))
        self.labelMedia.setText(_translate("MainWindow", "N/A"))
        self.label_16.setText(_translate("MainWindow", "Media:"))
        self.labelMediana.setText(_translate("MainWindow", "N/A"))
        self.label_15.setText(_translate("MainWindow", "Moda:"))
        self.label_18.setText(_translate("MainWindow", "Desviación estándar:"))
        self.labelDesviacionEstandar.setText(_translate("MainWindow", "N/A"))
        self.btnModas.setText(_translate("MainWindow", "Ver modas"))
        self.btnEliminarAtributo.setText(_translate("MainWindow", "Eliminar atributo"))
        self.btnFueraDominio.setText(_translate("MainWindow", "Ver"))
        self.btnFaltantes.setText(_translate("MainWindow", "Ver"))
        self.btnBoxPlot.setText(_translate("MainWindow", "Box plot"))
        self.btnHistograma.setText(_translate("MainWindow", "Histograma"))
        self.comboBoxTipoAtributo.setItemText(0, _translate("MainWindow", "Numérico"))
        self.comboBoxTipoAtributo.setItemText(1, _translate("MainWindow", "Categórico"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Información"))
        self.label_7.setText(_translate("MainWindow", "Número de instancias: "))
        self.label_8.setText(_translate("MainWindow", "Número de atributos: "))
        self.labelNumInstancias.setText(_translate("MainWindow", "N/A"))
        self.labelNumAtributos.setText(_translate("MainWindow", "N/A"))
        self.btnActualizarInfo.setText(_translate("MainWindow", "Actualizar"))
        self.label_4.setText(_translate("MainWindow", "Target"))
        self.label_5.setText(_translate("MainWindow", "Ruta"))
        self.label_6.setText(_translate("MainWindow", "Faltante"))
        self.comboBoxTarget.setItemText(0, _translate("MainWindow", "--Ninguno"))
        self.btnDescripcion.setText(_translate("MainWindow", "Descripción del dataset"))
        self.menuVersiones.setTitle(_translate("MainWindow", "Versiones"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAlgoritmos.setTitle(_translate("MainWindow", "Algoritmos"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action.setText(_translate("MainWindow", "asdf"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionZero_R.setText(_translate("MainWindow", "Zero-R"))
        self.actionOne_R.setText(_translate("MainWindow", "One-R"))
        self.actionNaive_Bayes.setText(_translate("MainWindow", "Naive Bayes"))
        self.actionK_NN.setText(_translate("MainWindow", "K-NN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
