
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
            for usuario in data:
                producto = Producto(id=usuario[0], nombre=usuario[1],)
                list.append(producto)
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

