import numpy as np
from ClassInscripcion import Inscripcion


class ColeccionInscripcion:
    __dimension = int
    __actual = int
    __Inscripcion = object
    __incremento = 5

    def __init__(self, dimension=0):
        self.__Inscripcion = np.empty(dimension, dtype=Inscripcion)
        self.__dimension = dimension
        self.__actual = 0

    def agregar_Inscripcion(self, fecha, pago, persona, taller):
        #Se agrega una inscripcion al arreglo
        if self.__actual == self.__dimension:
            self.__dimension += self.__incremento
            self.__Inscripcion.resize(self.__dimension)

        self.__Inscripcion[self.__actual] = Inscripcion(fecha, pago, persona, taller)
        self.__actual += 1

    def inscribir_persona(self, persona, taller):
        if taller.get_vacante() > 0:
            taller.restar_vacante(taller.get_vacante() - 1)
            fecha_inscripcion = str(input('Ingrese Fecha de inscripcion: '))
            self.agregar_Inscripcion(persona, taller, fecha_inscripcion, False)
            print(f'Persona inscrita en el taller {taller}')
        else:
            print('No hay Vacante')

    def mostrar_inscripciones(self):
        print('Inscripciones Realizadas')
        for inscripcion in self.__Inscripcion[:self.__dimension]:
            if inscripcion:
                print(inscripcion)

    def buscar_inscripcion_por_dni(self, dni):

        i = 0
        while i < len(self.__Inscripcion[:self.__actual]):
            inscripcion = self.__Inscripcion[i]
            if int(inscripcion.get_persona().get_dni_P()) == dni:
                print(f'{inscripcion.get_persona().get_nombre_P()} esta inscripto en {inscripcion.get_taller().get_nombre_Taller()} ')
                if not inscripcion.get_pago_inscripcion():
                    print(f'y adeuda {inscripcion.get_taller().get_monto_Inscripcion()} pesos')
                else:
                    print('y no adeuda.')
            i += 1

    def consultar_inscriptos_taller(self, id_taller):
        i = 0
        print(f'\nLOS INSCRIPTOS EN EL TALLER CON ID: {id_taller}')
        while i < len(self.__Inscripcion[:self.__actual]):
            inscripcion = self.__Inscripcion[i]
            if int(inscripcion.get_taller().get_id()) == id_taller:
                print(inscripcion.get_persona().Datos_P())
            i += 1

    def registrar_Pago(self, dni_a_buscar):
        i = 0

        while i < len(self.__Inscripcion[:self.__actual]):
            inscripcion = self.__Inscripcion[i]
            if int(inscripcion.get_persona().get_dni_P()) == dni_a_buscar:
                if not bool(inscripcion.get_pago_inscripcion()):
                    inscripcion.realizo_pago()
                    print('Pago Realizado')
                else:
                    print('Esta persona ya realizó el pago.')
            i += 1


    def guardar_inscripciones(self):
        with open('inscripciones.csv', 'w') as archivo:
            for inscripcion in self.__Inscripcion[:self.__actual]:
                dni = int(inscripcion.get_persona().get_dni_P())
                id_taller = int(inscripcion.get_taller().get_id())
                fecha_inscripcion = inscripcion.get_fechaInscripcion()
                pago = inscripcion.get_pago_inscripcion()
                archivo.write(f'{dni}; {id_taller}; {fecha_inscripcion}; {pago}\n')
        print("Las inscripciones se han guardado exitosamente en el archivo.")
