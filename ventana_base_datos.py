from ventana_base_datos_ui import *
from main_window import MainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox

"""
"SELECT bienraiz.id, titulo, precio, m2, rooms, baths, cars, descripcion, colonia.nombre AS colonia, municipio.nombre FROM bienraiz LEFT JOIN colonia ON bienraiz.id_colonia = colonia.id LEFT JOIN municipio ON municipio.id = colonia.id_municipio ORDER BY precio DESC"
"""


class VentanaBaseDatos(QWidget, Ui_Form):
	def __init__(self, conexion, archivo_propiedddes, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.btnAceptar.clicked.connect(self.aceptar)
		self.conexion = conexion
		self.propiedades = archivo_propiedddes

		self.cursor = self.conexion.cursor()
		self.mostrar_tablas()

	def aceptar(self):
		"""Este método se ejecuta al dar clic sobre el boton aceptar"""
		# debe comprobar que el query sea valido
		# debe iniciar main windows y pasarle la conexion y el query

		if self.es_query_valido():
			self.close()
			self.main = MainWindow(self.propiedades, self.conexion, self.textQuery.toPlainText())
			self.main.show()
		else:
			QMessageBox.critical(self, "Error", "El query no es válido")

	def es_query_valido(self):
		"""Retorna True si el query es válido, en caso contrario retorna False"""
		try:
			query = self.textQuery.toPlainText()
			self.cursor.execute(query)
			self.cursor.fetchall()
			return True
		except:
			return False


	def mostrar_tablas(self):
		"""Muestra las tablas que hay en la base de datos"""
		self.cursor.execute("SHOW TABLES")
		tablas = self.cursor.fetchall()

		for i in range(len(tablas)):
			label = QtWidgets.QLabel(self.groupBoxTablas)
			label.setObjectName("label" + str(i))
			self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, label)
			label.setText(tablas[i][0])
