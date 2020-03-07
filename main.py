from dialogo_elegir_propiedades import *
import pandas as pd

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dialogo = DialgoElegirPropiedades()
    dialogo.show()
    app.exec_()
    