# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_base_datos_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(591, 445)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxTablas = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxTablas.sizePolicy().hasHeightForWidth())
        self.groupBoxTablas.setSizePolicy(sizePolicy)
        self.groupBoxTablas.setMinimumSize(QtCore.QSize(180, 0))
        self.groupBoxTablas.setMaximumSize(QtCore.QSize(180, 16777215))
        self.groupBoxTablas.setObjectName("groupBoxTablas")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxTablas)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout.addWidget(self.groupBoxTablas)
        self.textQuery = QtWidgets.QPlainTextEdit(self.frame)
        self.textQuery.setObjectName("textQuery")
        self.horizontalLayout.addWidget(self.textQuery)
        self.verticalLayout_2.addWidget(self.frame)
        self.btnAceptar = QtWidgets.QPushButton(Form)
        self.btnAceptar.setObjectName("btnAceptar")
        self.verticalLayout_2.addWidget(self.btnAceptar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Base de datos"))
        self.label.setText(_translate("Form", "Ejecutar query"))
        self.groupBoxTablas.setTitle(_translate("Form", "Tablas"))
        self.btnAceptar.setText(_translate("Form", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
