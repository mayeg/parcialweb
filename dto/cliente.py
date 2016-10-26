# -*- coding: utf-8 -*-


class Cliente:

    def __init__(self, id=0, nombres="",
                 apellidos="", direccion="", telefono=""):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__direccion = direccion
        self.__telefono = telefono

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombres(self):
        return self.__nombres

    def setNombres(self, nombres):
        self.__nombres = nombres

    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def get_dict(self):
        return {
            'nombres': self.__nombres,
            'id': self.__id,
            'apellidos': self.__apellidos
        }
