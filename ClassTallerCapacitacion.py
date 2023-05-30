class TallerCapacitacion:

    def __init__(self, id=0, nombre_Taller='', vacante=0, monto_Insc= 0):
        self.__id_Taller = id
        self.__nombre_Taller = nombre_Taller
        self.__Vacante = vacante
        self.__monto_Inscripcion = monto_Insc

    def __str__(self):
        return f' {self.__nombre_Taller}, ID:{self.__id_Taller}, Vacantes:{self.__Vacante}, Monto de Inscripcion:{self.__monto_Inscripcion}'

    def get_id(self):
        return self.__id_Taller

    def get_nombre_Taller(self):
        return self.__nombre_Taller

    def get_vacante(self):
        return self.__Vacante

    def restar_vacante(self, vacante):
        self.__Vacante = vacante

    def get_monto_Inscripcion(self):
        return self.__monto_Inscripcion
