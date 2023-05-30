import numpy as np
from ClassTallerCapacitacion import TallerCapacitacion
class ColeccionTallerCapacitacion:
    __dimension = int
    __actual = int
    __Talleres = object
    __incremento = 5

    def __init__(self, dimension):
        self.__Talleres = np.empty(dimension, dtype=TallerCapacitacion)
        self.__dimension = dimension
        self.__actual = 0

    def agregar_taller(self, id, nombre,vacante, monto):
        #Se agrega un taller al arreglo
        if self.__actual == self.__dimension:
            self.__dimension += self.__incremento
            self.__Talleres.resize(self.__dimension)
        self.__Talleres[self.__actual] = TallerCapacitacion(id, nombre, vacante, monto)
        self.__actual += 1

    def mostrar(self):
        for taller in self.__Talleres[:self.__dimension]:
            print(taller)

    def buscar_taller(self, nombre_taller):
        i = 0
        while i < len(self.__Talleres[:self.__actual]):
            taller = self.__Talleres[i]
            if str(taller.get_nombre_Taller()) == nombre_taller:
                return taller
            else:
                i += 1
