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
        # The length of the outer list.
        return len(self.panda)

    def columnCount(self, index=QModelIndex()):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.panda.columns)

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return str(self.panda.columns[section])
        if orientation == Qt.Vertical:
            return str(self.panda.index[section])

    def removeColumns(self, column, count, parent=QModelIndex()):
        try:
            self.beginRemoveColumns(parent, column, count)
            self.panda.drop([self.panda.columns[column]], axis='columns', inplace=True)
            self.endRemoveColumns()
            return True
        except:
            return False