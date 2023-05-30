class Inscripcion:
    __fechaInscriocion = ''
    __pago = ''
    __persona = object
    __taller = object

    def __init__(self, persona, taller, fecha_ins='', pago=bool):
        self.__fechaInscripcion = fecha_ins
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def __str__(self):
        cadena = f'Fecha de inscripcion: {self.__fechaInscripcion}'
        if self.__pago:
            cadena += f', Pago: {self.__pago}'
        if self.__persona:
            cadena += f', Persona: {self.__persona.__str__()}'
        if self.__taller:
            cadena += f', Taller: {self.__taller.__str__()}'
        return cadena

    def get_fechaInscripcion(self):
        return self.__fechaInscripcion

    def realizo_pago(self):
        self.__pago = True

    def get_persona(self):
        return self.__persona

    def get_taller(self):
        return self.__taller

    def get_pago_inscripcion(self):
        return self.__pago
