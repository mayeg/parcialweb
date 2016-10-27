
from dto.venta import Venta

class VentaDao:
    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def crear_venta(self, venta):
        try:
            query = "INSERT INTO venta (idcliente, valoriva, valordescuentos, " \
                    "valortotal) VALUES (%s, %s, %s, %s)"
            param = (venta.getIdCliente().getId(),
                     venta.getValorIva(), venta.getValorDescuentos(),
                     venta.getValorTotal())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def get_ultima_venta(self):
        try:
            query = "SELECT * FROM venta ORDER BY numerofactura DESC LIMIT 1"
            self.__cur.execute(query)
            ven = self.__cur.fetchone()
            if ven is None:
                return None
            venta = Venta(ven[0], ven[1], ven[2], ven[3], ven[4])
            return venta
        except:
            return Venta()