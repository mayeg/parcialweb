from dto.producto import Producto
from dto.venta import Venta

class DetalleVenta:
    def __init__(self, idproducto=0, idfactura=0, cantidad=0, valoriva=0,
                 valordescuentos=0, total=0):

        self.__idproducto = Producto(id=idproducto)
        self.__idfactura = Venta(numerofactura=idfactura)
        self.__cantidad = cantidad
        self.__valoriva = valoriva
        self.__valordescuentos = valordescuentos
        self.__total = total

    def getIdProducto(self):
        return self.__idproducto

    def setIdProducto(self, idproducto):
        self.__idproducto = idproducto

    def getIdFactura(self):
        return self.__idfactura

    def setIdFactura(self, idfactura):
        self.__idfactura = idfactura

    def getCantidad(self):
        return self.__cantidad

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def setValorDescuentos(self, valordescuentos):
        self.__valordescuentos = valordescuentos

    def getValorIva(self):
        return self.__valoriva

    def setValorIva(self, valoriva):
        self.__valoriva = valoriva

    def getTotal(self):
        return self.__total

    def setTotal(self, total):
        self.__total = total