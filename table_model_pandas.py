from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor

class TableModelPandas(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.panda = data

    def data(self, index, role):
        value = str(self.panda.iloc[index.row(), index.column()])

        if role == Qt.DisplayRole:
            return value

    def rowCount(self, index=QModelIndex()):
        return len(self.panda)

    def columnCount(self, index=QModelIndex()):
        return len(self.panda.columns)

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return str(self.panda.columns[section])
        if orientation == Qt.Vertical:
            return str(self.panda.index[section])

    def removeColumns(self, column, count, parent=QModelIndex()):
        """Elimina una columna de la tabla y del pandas"""
        try:
            self.beginRemoveColumns(parent, column, count)
            self.panda.drop([self.panda.columns[column]], axis='columns', inplace=True)
            self.endRemoveColumns()
            return True
        except:
            return False

    def insertRows(self, row, count, new_row, parent=QModelIndex()):
        """Inserta una fila de la tabla y del pandas"""
        try:
            self.beginInsertRows(parent, row, count)
            num = len(self.panda)
            self.panda.loc[num] = new_row
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
        


