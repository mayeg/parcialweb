
from dto.cliente import Cliente


class Venta:

    def __init__(self, numerofactura=0, valortotal=0, valordescuentos=0,
                 valoriva=0, idcliente=0):

        self.__numerofactura = numerofactura
        self.__valortotal = valortotal
        self.__valordescuentos = valordescuentos
        self.__valoriva = valoriva
        self.__idcliente = Cliente(id=idcliente)

    def getNumeroFactura(self):
        return self.__numerofactura

    def setNumeroFactura(self, numerofactura):
        self.__numerofactura = numerofactura

    def getValorTotal(self):
        return self.__valortotal

    def setValorTotal(self, valortotal):
        self.__valortotal = valortotal

    def getValorDescuentos(self):
        return self.__valordescuentos

    def setValorDescuentos(self, valordescuentos):
        self.__valordescuentos = valordescuentos

    def getValorIva(self):
        return self.__valoriva

    def setValorIva(self, valoriva):
        self.__valoriva = valoriva

    def getIdCliente(self):
        return self.__idcliente

    def setIdCliente(self, idecliente):
        self.__idcliente = idecliente



    def get_dict(self):
        return {
            'numerofactura': self.__numerofactura,
            'idcliente': self.__idcliente.getId(),
            'valortotal': self.__valortotal
        }