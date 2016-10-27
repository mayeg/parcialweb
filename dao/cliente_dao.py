# -*- coding: utf-8 -*-
from dto.cliente import Cliente


class ClienteDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_clientes(self):
        try:
            query = "SELECT * FROM cliente"
            self.__cur.execute(query)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for c in data:
                cliente = Cliente(
                    id=c[0], nombres=c[1], apellidos=c[2])
                resultado.append(cliente)
            return resultado
        except Exception as e:
            print e.message
            return []

    def get_cliente(self, id):
        try:
            query = "SELECT * FROM cliente WHERE id=%s"
            param = (id,)
            self.__cur.execute(query, param)
            cliente = self.__cur.fetchone()
            if cliente is None:
                return None
            cliente = Cliente(id=cliente[0], nombres=cliente[1],
                              apellidos=cliente[2], direccion=cliente[3],
                              telefono=cliente[4])
            return cliente
        except:
            return Cliente()
