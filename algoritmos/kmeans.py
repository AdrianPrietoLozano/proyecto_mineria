import pandas
import numpy as np


class KMeans:

    def __init__(self, data, corridas=10, iteraciones=100):
        self.datos = data.values
        self.corridas = corridas
        self.iteraciones = iteraciones

        self.centroides = None
        self.asignados = np.zeros(self.datos.shape[0])
        self.silhouettes = np.zeros(self.datos.shape[0])
        self.NUM_CLUSTERS_NO_CAMBIAN = 5 # condicion de paro para el algoritmo

    def setCorridas(self, corridas):
        self.corridas = corridas

    def setIteraciones(self, iteraciones):
        self.iteraciones = iteraciones


    def _generar_centroides_iniciales(self, n_centroides):
        self.centroides = self.datos[np.random.randint(self.datos.shape[0], size=n_centroides), :]

    def _recalcular_centroides(self):
        for i in range(len(self.centroides)):
            self.centroides[i] = np.mean(self.datos[self.asignados == i], axis=0)

    def _distancia_entre(self, fila1, fila2):
        return np.sqrt(np.sum((fila1 - fila2)**2))

    def _mejor_cluster(self, fila):
        distancias = np.zeros(len(self.centroides))

        for i in range(len(self.centroides)):
            distancias[i] = self._distancia_entre(fila, self.centroides[i])

        return np.argmin(distancias)

    def generar_clusters(self, n_clusters):
        distancias = np.zeros((len(self.datos), n_clusters))
        copia_asignados = np.zeros(len(self.datos))

        promedio_menor = float('inf')
        mejor_asignados = np.zeros(len(self.datos))
        #mejor_silhouette = np.zeros(len(self.datos))

        for i in range(self.corridas):
            num_veces_iguales = 0
            self._generar_centroides_iniciales(n_clusters)
            for j in range(self.iteraciones):

                for k in range(n_clusters):
                    distancias[:,k] = np.linalg.norm(self.datos - self.centroides[k], axis=1)
                
                #for j in range(len(self.datos)):
                    #asignados[j] = self._mejor_cluster(self.datos[j])
                
                """
                for k in range(n_clusters):
                    distancias[:, k] = np.apply_along_axis(self._distancia_entre,
                        axis=1, arr=self.datos, fila2=self.centroides[k])
                """
                
                
                """
                for k in range(n_clusters):
                    for m in range(len(self.datos)):
                        distancias[m,k] = self._distancia_entre(self.datos[m], self.centroides[k])
                """
                
                #for m in range(self.datos.shape[0]):
                    #for k in range(n_clusters):
                        #distancias[m,k] = self._distancia_entre(self.datos[m], self.centroides[k])

                #print(distancias)
                self.asignados = np.argmin(distancias, axis=1)
                #print()
                #print(asignados)
                if np.all(self.asignados == copia_asignados):
                    num_veces_iguales += 1
                    if num_veces_iguales == self.NUM_CLUSTERS_NO_CAMBIAN:
                        break
                else:
                    num_veces_iguales = 0

                #if copia_asignados == asignados:
                    #break;

                copia_asignados = self.asignados.copy()
                #recalcular self.centroides
                self._recalcular_centroides()

            # aqui debe calcular promedio
            #promedio_silhouette = self.calcular_silhouette()
            #promedio_silhouette = 0.3
            promedio = self.calcular_promedio_promedios()
            print(promedio)
            #if promedio_silhouette > promedio_mayor:
            if promedio < promedio_menor:
                #mejor_silhouette = self.silhouettes.copy()
                mejor_asignados = self.asignados.copy()
                #promedio_mayor = promedio_silhouette
                promedio_mayor = promedio

        print(mejor_asignados)
        #print(mejor_silhouette)
        print(promedio_mayor)


    def calcular_promedio_promedios(self):
        promedios = []
        for i in range(self.centroides.shape[0]):
            arreglo = self.datos[self.asignados == i]
            if arreglo.shape[0] == 0:
                promedios.append(500)
            else:
                promedio_cluster = np.mean(np.apply_along_axis(self._distancia_entre, 
                    axis=1, arr=arreglo, fila2=self.centroides[i]))
                promedios.append(promedio_cluster)

        return np.mean(promedios)


    def calcular_silhouette(self):
        for i in range(self.datos.shape[0]):
            cluster = self.asignados[i]
            instancia = self.datos[i]
            #np.mean(self.datos[ asignados == cluster ])
            a = np.mean(np.linalg.norm(self.datos[ self.asignados == cluster ] - instancia, axis=1))

            promedio_otros_clusters = []
            for j in range(self.centroides.shape[0]):
                if j == cluster:
                    continue

                promedio_otros_clusters.append(np.mean(np.linalg.norm(self.datos[self.asignados == j] - instancia, axis=1)))

            b = min(promedio_otros_clusters)

            try:
                self.silhouettes[i] = (b - a) / max(a, b)
            except Exception:
                self.silhouettes[i] = 0

        promedio_silhouette = np.zeros(self.centroides.shape[0])
        for i in range(self.centroides.shape[0]):
            promedio_silhouette[i] = np.mean(self.silhouettes[ self.asignados == i ])


        return np.mean(promedio_silhouette)






"""
data = pandas.read_csv("iris.csv", skipinitialspace=True)
data.drop("class", inplace=True, axis=1)

print("inicio")
k_means = KMeans(data, 10, 100)
k_means.generar_clusters(9)

"""