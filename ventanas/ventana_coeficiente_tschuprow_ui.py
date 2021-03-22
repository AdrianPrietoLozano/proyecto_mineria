# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_coeficiente_tschuprow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 242)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox1 = QtWidgets.QComboBox(self.frame)
        self.comboBox1.setIconSize(QtCore.QSize(12, 12))
        self.comboBox1.setObjectName("comboBox1")
        self.horizontalLayout.addWidget(self.comboBox1)
        self.comboBox2 = QtWidgets.QComboBox(self.frame)
        self.comboBox2.setIconSize(QtCore.QSize(12, 12))
        self.comboBox2.setObjectName("comboBox2")
        self.horizontalLayout.addWidget(self.comboBox2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnCalcular = QtWidgets.QPushButton(self.frame_2)
        self.btnCalcular.setMinimumSize(QtCore.QSize(100, 0))
        self.btnCalcular.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnCalcular.setObjectName("btnCalcular")
        self.horizontalLayout_2.addWidget(self.btnCalcular)
        self.labelResultado = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelResultado.sizePolicy().hasHeightForWidth())
        self.labelResultado.setSizePolicy(sizePolicy)
        self.labelResultado.setObjectName("labelResultado")
        self.horizontalLayout_2.addWidget(self.labelResultado)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Coeficiente de Tschuprow"))
        self.label_2.setText(_translate("Form", "Coeficiente de contingencia de Tschuprow"))
        self.btnCalcular.setText(_translate("Form", "Calcular"))
        self.labelResultado.setText(_translate("Form", "N/A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
