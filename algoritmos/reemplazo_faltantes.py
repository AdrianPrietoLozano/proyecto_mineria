import pandas
import numpy as np


class ReemplazoFaltantes:

	def __init__(self, data, target, simbolo_faltante, metodos):
		self.data = data
		self.target = target
		self.simbolo_faltante = simbolo_faltante
		self.metodos = metodos

		self.es_regresion = False
		self.data = self.data.replace(self.simbolo_faltante, np.nan).apply(pandas.to_numeric, errors="ignore")

		# si el target es numérico significa que es un problema de regresión
		if np.issubdtype(self.data[self.target], np.number):
			self.es_regresion = True

	def reemplazar_target_por_moda(self):
		if self.target != None:
			moda = self.data[self.target].mode()[0]
			self.data[self.target].fillna(moda, inplace=True)

	def reemplazar_target_por_media(self):
		if self.target != None and np.issubdtype(self.data[self.target].dtype, np.number):
			media = self.data[self.target].mean()
			self.data[self.target].fillna(media, inplace=True)

	def eliminar_filas_target_faltante(self):
		if self.target != None:
			self.data = self.data[self.data[self.target].notna()]

	def iniciar_reemplazo(self):
		if self.target is not None and not self.es_regresion: # SI ES PROBLEMA DE CLASIIFICACIÓN
			for valor in self.data[self.target].unique():
				self.data[self.data[self.target] == valor] = \
					self.data[self.data[self.target] == valor].apply(lambda col: self.reemplazar_columna(col), axis=0)
				#self.data[self.data[self.target] == valor].apply(lambda col: self.reemplazar_columna(col), axis=0)
		else:
			self.data[:] = self.data.apply(lambda col: self.reemplazar_columna(col), axis=0)

	def reemplazar_columna(self, columna):
		if np.issubdtype(columna.dtype, np.number): # es numérica
			try:
				metodo = self.metodos[columna.name]
			except Exception:
				metodo = "media"
				
			if metodo == "media":
				valor = columna.mean()
			else:
				valor = columna.median()
		else: # es categorica usar la moda
			valor = columna.mode()[0]

		return columna.fillna(valor)
		#print("valor:", valor)
		#columna.fillna(valor, inplace=True)

	def get_datos(self):
		return self.data


"""
def iniciar_reemplazo(data, metodo):
	if True: # SI ES PROBLEMA DE CLASIIFICACIÓN
		for valor in data[TARGET].unique():
			reemplazar_dataframe(data[data[TARGET] == valor], metodo)


def reemplazar_dataframe(data, metodo):
	for columna in data.columns:
		if np.issubdtype(data[columna].dtype, np.number): # es numérico
			valor = data[columna].mean() if metodo == "media" else data[columna].median()
			reemplazar_columna(data[columna], valor)
		else: # si es categórico reeemplazar por la moda
			reemplazar_columna(data[columna], data[columna].mode()[0])

"""



"""
FALTANTE = "?"
TARGET = "class"

data = pandas.read_csv("iris.csv", skipinitialspace=True)
pandas.set_option('display.max_rows', 300)

# poner valores faltantes a NaN e intentar hacer conversion de tipos

print("ANTES")
print(data)
print("------------------------------------------------\n\n")


metodos = {'sepal length': 'media',
	'sepal width': 'mediana',
	'petal length': 'media',
	'petal width': 'mediana'}
reemplazo = ReemplazoFaltantes(data, TARGET, FALTANTE, metodos)
reemplazo.reemplazar_target_por_moda()
reemplazo.iniciar_reemplazo()

print("DESPUES")
print(reemplazo.data)
"""


