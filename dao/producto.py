
from dto.producto import Producto


class ProductoDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_productos(self):
        try:
            query = "SELECT * FROM producto "
            self.__cur.execute(query)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for producto in data:
                producto = Producto(id=producto[0], nombre=producto[1],
                                    tipo=producto[2], precioventa=producto[3],
                                    existencias=producto[4],
                                    costounitario=producto[5],
                                    saldoinventario=producto[6])
                resultado.append(producto)
            return resultado
        except Exception as e:
            print e.message
            return []

    def get_producto_nombre(self, nombre):
        try:
            query = "SELECT * FROM producto WHERE nombre=%s "
            param = (nombre,)
            self.__cur.execute(query,param)
            data = self.__cur.fetchone()
            if data is None:
                return None

            return Producto(id=data[0], nombre=data[1], tipo=data[2], precioventa=data[3],
                            existencias=[4])
        except Exception as e:
            print e.message
            return []

    def modificar_existencias(self, producto):
        try:
            query = "UPDATE producto SET existencias= %s WHERE id=%s "
            param = (producto.getExistencias(), producto.getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

