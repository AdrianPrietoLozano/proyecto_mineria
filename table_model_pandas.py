from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor

class TableModelPandas(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def data(self, index, role):
    	value = str(self._data.iloc[index.row(), index.column()])

    	if role == Qt.BackgroundRole and value == '?': # no funciona
    		return QtGui.QColor('red')

    	if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return value

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data.columns)

    def headerData(self, section, orientation, role):
    	if role != Qt.DisplayRole:
    		return None
    	if orientation == Qt.Horizontal:
    		return str(self._data.columns[section])
    	if orientation == Qt.Vertical:
    		return str(self._data.index[section])