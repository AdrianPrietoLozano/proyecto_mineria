import json
import os


class Respaldos:

	def __init__(self, conjunto):
		self.conjunto = conjunto

	def hacer_respaldo(self, nombre):

		carpeta_respaldos = self.conjunto.getRutaRespaldos()

		if not os.path.isdir(carpeta_respaldos):# si no existe la carpeta de respaldos intenta crearla
			try:
				os.mkdir(carpeta_respaldos) # crea carpeta
			except: # si no se pudo crear la carpeta retorna False
				return False

		csv_original = self.conjunto.getPathCsv()

		nombre_respaldo = carpeta_respaldos + nombre
		self.conjunto.panda.to_csv(nombre_respaldo + ".csv", index=False, header=None)

		self.conjunto.setPathCsv(nombre_respaldo + ".csv") # el respaldo debe hacer referencia a la nueva version del csv

		# guarda el archivo de propiedades
		with open(nombre_respaldo + ".json", "w") as fp:
			json.dump(self.conjunto.data, fp)
			fp.close()

		self.conjunto.setPathCsv(csv_original) # restablecer el nombre del csv original
		return True

