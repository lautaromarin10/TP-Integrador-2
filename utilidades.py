#Conteo de frecuencia de cada digito en cada DNI:
def frecuencia_digitos(dni):
    conteo = {str(i): 0 for i in range(10)}
    for dig in str(dni):
        conteo[dig] += 1
    return conteo

#Suma total de los digitos en cada DNI
def suma_digitos(dni):
    return sum(int(d) for d in str(dni))

#Utilidades
def verificar_dni(dni: int):
    return len(str(dni)) == 8

def verificar_año(año: int):
    return len(str(año)) == 4

def es_año_par(año: int):
    return año % 2 == 0

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
        producto.append([año,edad])
    return producto