# Utilidades para operaciones_con_dni
def conjunto_sin_repetidos(conjunto: list):
    digitos_sin_repetir = []
    
    for numero in conjunto:
        # Convertir el número a string y luego cada dígito de vuelta a int
        digitos = [int(digito) for digito in str(numero)]
        for d in digitos:
            if d not in digitos_sin_repetir:
                digitos_sin_repetir.append(d)
                
    return digitos_sin_repetir

# Utilidades
def verificar_dni(dni: int):
    return len(str(dni)) == 8

def solicitar_DNI():

    cantidad = int(input("Ingrese la cantidad de DNIs a solicitar\n"))
    lista_dni = []

    if cantidad < 0:
        print("La cantidad no puede ser negativa ni cero, vuelve a intentarlo nuevamente\n")
        solicitar_DNI()

    for i in range(cantidad):
        dni = int(input(f"Ingrese el {i + 1} DNI\n"))

        while(not verificar_dni(dni)):
            print("El DNI igresado no cuenta con el largo permitido (8). Por favor intentalo nuevamente\n")
            dni = int(input(f"Ingrese el {i + 1} DNI\n"))

        lista_dni.append(dni)

    return [lista_dni]


def verificar_año(año: int):
    return len(str(año)) == 4


def es_año_par(año: int):
    return año % 2 == 0

def uno_si(condicion):
    #Retorna verdadero en caso de que la condicion sea verdadera
    #Integer
    return 1 if condicion else 0

def año_mayor_a_2000(año: int):
    return año > 2000


def es_año_bisiesto(año: int):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


def generar_edades(años: list):
    año_actual = 2025
    lista_edades = []

    for año in años:
        lista_edades.append(año_actual - año)

    return lista_edades


def producto_cartesiano_por_edades(año, edades):
    producto = []
    for edad in edades:
        producto.append([año, edad])
    return producto

def union_conjuntos(conjunto1: list, conjunto2: list):
    """Devuelve la unión de dos conjuntos (todos los elementos de ambos)"""
    union = list(set(conjunto1) | set(conjunto2))
    print(f"Union entre el conjunto {conjunto1} y el conjunto {conjunto2}: {union}")
    return union

def interseccion_conjuntos(conjunto1: list, conjunto2: list):
    """Devuelve los elementos comunes entre dos conjuntos"""
    interseccion = list(set(conjunto1) & set(conjunto2))
    print(f"Interseccion entre el conjunto {conjunto1} y el conjunto {conjunto2}: {interseccion}")
    return interseccion

def diferencia_conjuntos(conjunto1: list, conjunto2: list):
    """Devuelve los elementos que están en conjunto1 pero no en conjunto2"""
    diferencia =  list(set(conjunto1) - set(conjunto2))
    print(f"Diferencia entre el conjunto {conjunto1} y el conjunto {conjunto2}: {diferencia}")

def diferencia_simetrica_conjuntos(conjunto1: list, conjunto2: list):
    """Devuelve los elementos que están en un conjunto pero no en ambos"""
    diferencia = list(set(conjunto1) ^ set(conjunto2))
    print(f"Diferencia simetrica entre el conjunto {conjunto1} y el conjunto {conjunto2}: {diferencia}")

def unificacion_conjuntos(conjuntos):

    conjunto1 = conjuntos[0]
    
    if len(conjuntos) >= 2:
        conjunto2 = conjuntos[1]
    else:
        print("No existe un segundo DNI para hacer operaciones entre conjuntos")
        return

    union_conjuntos(conjunto1, conjunto2)
    interseccion_conjuntos(conjunto1, conjunto2)
    diferencia_conjuntos(conjunto1, conjunto2)
    diferencia_simetrica_conjuntos(conjunto1, conjunto2)