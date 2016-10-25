
from dto import candidato
from dto import voto

class CandidatoDao:

    def __init__(self):
        from proyecto import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_voto_candidato(self):
        pass

    def registrar_candidato(self):
        pass

    def registrar_voto(self, candidato):
        pass

    def listar_candidatos(self):
        pass





