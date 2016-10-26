

class Producto:
    def __init__(self, id=0, nombre="", tipo="", precioventa=0, existencias=0,
                 costounitario=0, saldoinventario=0):

        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__precioventa = precioventa
        self.__existencias = existencias
        self.__costounitario = costounitario
        self.__saldoinventario = saldoinventario

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombres(self, nombre):
        self.__nombre = nombre

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getPrecioVenta(self):
        return self.__precioventa

    def setPrecioVenta(self, precioventa):
        self.__precioventa = precioventa

    def getExistencias(self):
        return self.__existencias

    def setExistencias(self, existencias):
        self.__existencias = existencias

    def getCostoUnitario(self):
        return self.__costounitario

    def setCostoUnitario(self, costounitario):
        self.__costounitario = costounitario

    def getSaldoInventario(self):
        return self.__saldoinventario

    def setSaldoInventario(self, saldoinventario):
        self.__saldoinventario = saldoinventario

    def get_dict(self):
        return {
            'nombre': self.__nombre,
            'id': self.__id,
            'tipo': self.__tipo
        }