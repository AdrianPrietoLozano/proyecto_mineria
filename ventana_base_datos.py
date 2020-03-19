from ventana_base_datos_ui import *
from main_window import MainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
import mysql.connector

"""
"SELECT bienraiz.id, titulo, precio, m2, rooms, baths, cars, descripcion, colonia.nombre AS colonia, municipio.nombre FROM bienraiz LEFT JOIN colonia ON bienraiz.id_colonia = colonia.id LEFT JOIN municipio ON municipio.id = colonia.id_municipio ORDER BY precio DESC"
"""



class VentanaBaseDatos(QWidget, Ui_Form):
	def __init__(self, datos_conexion, archivo_propiedddes, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.btnAceptar.clicked.connect(self.aceptar)

		self.datos_conexion = datos_conexion
		self.propiedades = archivo_propiedddes
		self.conexion = self.intentar_conectarse_BD()

		if self.conexion == None:
			self.close()
			QMessageBox.critical(self, "Error",
				"No fue posible conectarse a la base de datos");
		else:
			self.cursor = self.conexion.cursor()
			self.mostrar_tablas()

	def aceptar(self):
		"""Este método se ejecuta al dar clic sobre el boton aceptar"""
		# debe comprobar que el query sea valido
		# debe iniciar main windows y pasarle la conexion y el query
		self.close()
		self.main = MainWindow(self.propiedades, self.conexion, self.textQuery.toPlainText())
		self.main.show()

	
	def intentar_conectarse_BD(self):
		try:
			datos = self.datos_conexion.split(";");
			print(datos)
			usuario = datos[0]
			contrasenia = datos[1]
			base_datos = datos[2]
			host = datos[3]

			return mysql.connector.connect(user=usuario,
				password=contrasenia,
				database=base_datos,
				host=host)
		except:
			return None

	def mostrar_tablas(self):
		"""Muestra las tablas que hay en la base de datos"""
		self.cursor.execute("SHOW TABLES")
		tablas = self.cursor.fetchall()

		for i in range(len(tablas)):
			label = QtWidgets.QLabel(self.groupBoxTablas)
			label.setObjectName("label" + str(i))
			self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, label)
			label.setText(tablas[i][0])
