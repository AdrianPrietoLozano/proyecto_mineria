from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor

# Es necesaria esta clase para que se muestre todo el conjunto de datos en la interfaz grafica
class TableModelPandas(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.panda = data

    def data(self, index, role):
        """Este método es llamado automáticamente por pyqt al mostrar la tabla"""
        value = str(self.panda.iloc[index.row(), index.column()])

        if role == Qt.DisplayRole:
            return value

    def rowCount(self, index=QModelIndex()):
        """Retorna el número de instancias en el dataset"""
        return len(self.panda)

    def columnCount(self, index=QModelIndex()):
        """Retorna el número de columnas en el dataset"""
        return len(self.panda.columns)

    def headerData(self, section, orientation, role):
        """Este método es llamado automáticamente por pyqt al mostrar la tabla.
        Sirve para mostrar los nombres de las columnas (horizontal) y el
        id de cada instancia (vertical)
        """
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal: # mostrar nombre de columna
            return str(self.panda.columns[section])
        if orientation == Qt.Vertical: # mostrar id de instancia
            return str(self.panda.index[section])

    def removeColumns(self, column, count, parent=QModelIndex()):
        """Elimina una columna de la tabla y del pandas"""
        try:
            self.beginRemoveColumns(parent, column, count)
            self.panda.drop([self.panda.columns[column]], axis='columns', inplace=True) # Para eliminar una columna del pandas, eliminamos desde el mismo dataframe
            self.endRemoveColumns()
            return True
        except:
            return False

    def insertarColumnaAlFinal(self, nombre, parent=QModelIndex()):
        """Inserta una columna al final"""
        if nombre in self.panda.columns: # no se permiten nombre de atributos repetidos
            return False

        indexColumn = len(self.panda.columns) # insertará la columna al final
        return self.insertColumns(indexColumn, indexColumn, nombre)

    def insertColumns(self, column, count, nombre, parent=QModelIndex()):
        """Inserta una columna en el pandas"""
        try:
            self.beginInsertColumns(parent, column, count)
            self.panda[nombre] = "?"
            self.endInsertColumns()
            return True
        except:
            return False

    def insertRows(self, row, count, new_row, parent=QModelIndex()):
        """Inserta una fila de la tabla y del pandas"""
        try:
            self.beginInsertRows(parent, row, count)
            num = len(self.panda)
            # insertará al final del dataset

            index_ultima_instancia = self.panda.index[num - 1] # index de la ultima instancia
            # la nueva instancia tendrá de index el index de la ultima instancia mas 1
            index_nueva_instancia = index_ultima_instancia + 1
            self.panda.loc[index_nueva_instancia] = new_row # inserta una instancia la pandas
            self.endInsertRows()
            return True
        except:
            return False

    def eliminarMultiplesFilas(self, rows, parent=QModelIndex()):
        """Inicia el proceso para eliminar multiples filas"""
        total_eliminadas = 0
        for row in rows:
            fila_en_tabla = self.encontrarFilaEnTabla(row)
            if fila_en_tabla != -1:
                if self.removeRows(fila_en_tabla, fila_en_tabla, parent):
                    total_eliminadas += 1

        return total_eliminadas

    def encontrarFilaEnTabla(self, row):
        """Dado un id del pandas busca su correspondiente en la tabla"""
        try:
            return self.panda.index.get_loc(row)
        except:
            return -1

    def removeRows(self, row, count, parent=QModelIndex()):
        """Elimina una columna de la tabla y del pandas"""
        try:
            self.beginRemoveRows(parent, row, count)
            self.panda.drop(self.panda.index[row], inplace=True)
            self.endRemoveRows()
            return True
        except:
            return False
        


