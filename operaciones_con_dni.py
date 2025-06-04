from utilidades import verificar_dni
from utilidades import conjunto_sin_repetidos

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

    return lista_dni

def generar_conjuntos_con_digitos_unicos(conjuntos: list):

    conjunto_digitos_unicos = []

    if conjuntos:
        for conjunto in conjuntos:
            conjunto_digitos_unicos.append(conjunto_sin_repetidos(conjunto))

    return conjunto_digitos_unicos

#Conteo de frecuencia de cada digito en cada DNI:
def frecuencia_digitos(dni):
    conteo = {str(i): 0 for i in range(10)}
    for dig in str(dni):
        conteo[dig] += 1
    return conteo

#Suma total de los digitos en cada DNI
def suma_digitos(dni):
    return sum(int(d) for d in str(dni))
