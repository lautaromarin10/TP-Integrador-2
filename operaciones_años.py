from utilidades import *

def solicitar_años():

    cantidad = int(input("Ingrese la cantidad de años a solicitar\n"))
    lista_años = []

    if cantidad < 0:
        print("La cantidad no puede ser negativa ni cero, vuelve a intentarlo nuevamente\n")
        solicitar_años()

    for i in range(cantidad):
        año = int(input(f"Ingrese el {i + 1} Año\n"))

        while(not verificar_año(año)):
            print("El Año igresado no cuenta con el largo permitido (4). Por favor intentalo nuevamente\n")
            año = int(input(f"Ingrese el {i + 1} Año\n"))

        lista_años.append(año)

    return lista_años

def contar_pares_e_impares(años: list):
    años_estado = [0,0] #Par, impar

    for año in años:
        if es_año_par(año):
            años_estado[0] = años_estado[0] + 1
        else: 
            años_estado[1] = años_estado[1] + 1
    
    print(f"hay {años_estado[0]} años pares y {años_estado[1]} impares")

    return años_estado

def son_gen_z(años: list):
    if all(año_mayor_a_2000(año) for año in años):
        print("Gen Z")

def hay_año_especial(años: list):
    if any(es_año_bisiesto(año) for año in años):
        print("Tenemos un año especial")

def producto_cartesiano(años: list):    
    lista_edades = generar_edades(años)
    producto_cartesiano = []

    for año in años:
        producto_cartesiano.append(producto_cartesiano_por_edades(año, lista_edades))

    print(f"Producto cartesiano generado entre los conjuntos y las edades \n {producto_cartesiano}")

    return producto_cartesiano

def integrador_operaciones_años():
    #Funcion que integra todo el desarrollo anteriro

    lista_años = solicitar_años()
    contar_pares_e_impares(lista_años)
    son_gen_z(lista_años)
    hay_año_especial(lista_años)
    producto_cartesiano(lista_años)
