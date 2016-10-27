from dto.producto import Producto
from dto.cliente import Cliente
from dto.detalle_venta import DetalleVenta


class DetalleVentaDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def crearDetalleVenta(self, detalle):
        try:
            print detalle.getIdProducto().getId()
            print detalle.getIdFactura().getNumeroFactura()
            query = "INSERT INTO detalleventa (idproducto, idfactura, cantidad, valoriva, " \
                    "valordescuento, total) VALUES (%s, %s, %s, %s, %s, %s)"
            param = (str(detalle.getIdProducto().getId()), int(detalle.getIdFactura().getNumeroFactura()), int(detalle.getCantidad()),
                     float(detalle.getValorIva()), float(detalle.getValorDescuentos()), float(detalle.getTotal()))
            self.__cur.execute(query, param)
            self.__conn.commit()
            print "aqui"
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False


    def get_total_cantidad(self):
        try:
            query = "SELECT p.id, p.nombre, d.suma FROM producto p , " \
                    "(SELECT SUM(t.total) AS suma , t.idproducto " \
                    "FROM detalleventa t " \
                    "GROUP By t.idproducto) d " \
                    "WHERE d.idproducto = p.id ORDER By d.suma DESC"
            self.__cur.execute(query)
            data = self.__cur.fetchall()
            resultado = list()
            print "data", data
            if data is None:
                return []
            for usuario in data:
                producto = Producto(id=usuario[0], nombre=usuario[1])
                detalleventa = DetalleVenta(total=usuario[2])
                detalleventa.setIdProducto(producto)
                resultado.append(detalleventa)
            return resultado
        except Exception as e:
            print "error"
            print e.message, e.__class__
            return []