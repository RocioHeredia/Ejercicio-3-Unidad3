from ClassPersona import Persona
class ColeccionPersona:
    def __init__(self):
        self.__personas = []

    def agregar_persona(self):
        nombre = input('Ingrese nombre de la persona: ')
        dni = input('Ingrese DNI de la persona: ')
        direccion = input('Ingrese direccion de la persona: ')
        persona = Persona(nombre, direccion, dni)
        self.__personas.append(persona)
        return persona
