class Persona:

    def __init__(self, nombre='', direccion='', dni=0):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__DNI = dni

    def __str__(self):
        return f'{self.__DNI}, {self.__nombre}, {self.__direccion}'

    def Datos_P(self):
        return f'\nNombre: {self.__nombre} \nDni: {self.__DNI} \nDireccion: {self.__direccion}'

    def get_nombre_P(self):
        return self.__nombre

    def get_direccion_P(self):
        return self.__direccion

    def get_dni_P(self):
        return self.__DNI