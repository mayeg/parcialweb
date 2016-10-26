
from dto.venta import Venta

class VentaDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def crearVenta(self, venta):
        try:
            query = "INSERT INTO venta (numeroventa, idcliente) VALUES (%s, %s)"
            param = (venta.getNumeroFactura(), venta.getIdCliente().getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def get_venta_numero(self, numero):
        try:
            query = "SELECT * FROM venta WHERE numerofactura=%s "
            param = (numero,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Venta(numerofactura=data[0])

        except Exception as e:
            print e.message
            return None