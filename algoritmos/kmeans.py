import pandas
import numpy as np


class KMeans:

    def __init__(self, data, corridas=10, iteraciones=100):
        self.datos = data.values
        self.corridas = corridas
        self.iteraciones = iteraciones

        self.centroides = None
        self.asignados = np.zeros(self.datos.shape[0]) # Crea un arreglo que inicializa en 0's
        self.silhouettes = np.zeros(self.datos.shape[0])
        self.NUM_CLUSTERS_NO_CAMBIAN = 5 # condicion de paro para el algoritmo

    def setCorridas(self, corridas):
        self.corridas = corridas


    def setIteraciones(self, iteraciones):
        self.iteraciones = iteraciones


    def _generar_centroides_iniciales(self, n_centroides):
        """ Selecciona los centroides iniciales aleatoriamente """
        index_aleatorios = np.random.choice(self.datos.shape[0], size=n_centroides)
        self.centroides = self.datos[index_aleatorios, :].astype(float)


    def _recalcular_centroides(self):
        """ Reemplaza los centroides por la media de las instancias
        en cada cluster """
        for i in range(len(self.centroides)):
            self.centroides[i] = np.mean(self.datos[self.asignados == i], axis=0)


    def generar_clusters(self, n_clusters):
        distancias = np.zeros((len(self.datos), n_clusters))
        copia_asignados = np.zeros(len(self.datos))

        promedio_mayor = float('-inf')
        mejor_asignados = np.zeros(len(self.datos))

        for i in range(self.corridas):
            num_veces_iguales = 0
            self._generar_centroides_iniciales(n_clusters)
            for j in range(self.iteraciones):

                for k in range(n_clusters):
                    # calcula distancia de cada instancia con cada centroide - (Distancia Euclidiana)
                    distancias[:, k] = np.sqrt( np.sum( (self.datos - self.centroides[k] )**2, axis=1 ) )

                # obtiene el cluster con menor distancia
                self.asignados = np.argmin(distancias, axis=1) # Te devuelve el indice del valor menor

                # si asignados es igual a copia_asignados aumenta en
                # uno el numero de veces iguales, si los clusters
                # asignados no cambian N veces seguidas entonces termina
                if np.all(self.asignados == copia_asignados):
                    num_veces_iguales += 1
                    if num_veces_iguales == self.NUM_CLUSTERS_NO_CAMBIAN:
                        break
                else:
                    num_veces_iguales = 0

                copia_asignados = self.asignados.copy()
                self._recalcular_centroides()

            promedio = self._calcular_silhouette()
            if promedio > promedio_mayor:
                mejor_silhouette = self.silhouettes.copy()
                mejor_asignados = self.asignados.copy()
                promedio_mayor = promedio

        return mejor_asignados, mejor_silhouette.round(4), promedio_mayor


    def _calcular_silhouette(self):
        for i in range(self.datos.shape[0]):
            cluster = self.asignados[i] # cluster al que pertenece la instancia
            instancia = self.datos[i]
            
            # obtener promedio de la distancia entre la instancia y 
            # las demás instancias del mismo cluster
            # (Distancia Euclidiana)
            a = np.mean( np.sqrt( np.sum( (self.datos[ self.asignados == cluster ] - instancia )**2, axis=1 ) ) )


            promedio_otros_clusters = []
            for c in range(self.centroides.shape[0]):
                if c == cluster:
                    continue

                # promedio de la distancia entre la instancia y las otras
                # instancias del cluster c
                promedio = np.mean( np.sqrt( np.sum( (self.datos[self.asignados == c] - instancia)**2, axis=1 ) ) )
                promedio_otros_clusters.append(promedio)

            # minimo del promedio de la distancia con otros clusters
            b = min(promedio_otros_clusters)

            self.silhouettes[i] = (b - a) / max(a, b)

        # calcula promedios de la métrica silhouette de cada cluster
        promedio_silhouette = np.zeros(self.centroides.shape[0])
        for i in range(self.centroides.shape[0]):
            promedio_silhouette[i] = np.mean(self.silhouettes[ self.asignados == i ])

        # retorna el promedio de los promedios del silhouette de cada cluster
        return np.mean(promedio_silhouette)
