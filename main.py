import csv
from TalleresColeccion import ColeccionTallerCapacitacion
from ColeccionPersona import ColeccionPersona
from ColeccionInscripcion import ColeccionInscripcion

def cargar_archivo():
    # print('Cargando')
    archivo = open('Talleres.csv', encoding='utf-8-sig')
    reader = csv.reader(archivo, delimiter=';')
    bandera = True
    for fila in reader:
        if bandera:
            tamaño = int(fila[0])
            talleres_C = ColeccionTallerCapacitacion(tamaño)
            bandera = False
            # print('creando arreglo')
        else:
            talleres_C.agregar_taller(int(fila[0]), fila[1], int(fila[2]), int(fila[3]))
    return talleres_C

def menu():
    print("\n--- MENÚ ---")
    print("1. Inscribir persona en un taller")
    print("2. Consultar inscripción")
    print("3. Consultar inscriptos en un taller")
    print("4. Registrar pago")
    print("5. Guardar inscripciones")
    print("0. Salir")


def item1(persona_C, inscripcion_C, arreglo):
    print("Inscribir persona en un taller \n")
    persona = persona_C.agregar_persona()
    nombre_taller = input('Ingrese nombre del taller: ')
    taller = arreglo.buscar_taller(nombre_taller)
    if taller is not None:
        inscripcion_C.inscribir_persona(persona, taller)
    else:
        print(f"No se encontró el taller '{nombre_taller}'")
        nombre_taller = input('Ingrese otro taller: ')


def item2(inscripcion_C):
    print(" Consultar inscripción")
    dni_a_buscar = int(input('Ingrese DNI para buscar Inscripcion: '))
    inscripcion_C.buscar_inscripcion_por_dni(dni_a_buscar)

def item3(inscripcion_C):
    print(" Consultar inscriptos en un taller")
    id_a_buscar = int(input('Ingrese id del Taller: '))
    inscripcion_C.consultar_inscriptos_taller(id_a_buscar)

def item4(inscripcion_C):
    print(" Registrar pago")
    dni_a_buscar = int(input('Ingrese DNI para registrar Pago: '))
    inscripcion_C.registrar_Pago(dni_a_buscar)

def item5(inscripcion_C):
    print(" Guardando inscripciones")
    inscripcion_C.guardar_inscripciones()


if __name__ == '__main__':
    arreglo = cargar_archivo()
    #arreglo.mostrar()
    inscripcion_C = ColeccionInscripcion()
    persona_C = ColeccionPersona()
    opcion = None

    while opcion != 0:
        menu()
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            item1(persona_C, inscripcion_C, arreglo)
        elif opcion == 2:
            item2(inscripcion_C)
        elif opcion == 3:
            item3(inscripcion_C)
        elif opcion == 4:
            item4(inscripcion_C)
        elif opcion == 5:
            item5(inscripcion_C)
        elif opcion == 0:
            print('Saliendo...')
            break
        else:
            opcion = int(input('Ingrese una opcion valida: '))
