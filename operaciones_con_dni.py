from utilidades import verificar_dni

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

def conjunto_sin_repetidos(conjunto: list):

    conjunto_sin_repetidos = []

    for numero in conjunto:
        if not numero in conjunto_sin_repetidos:
            conjunto_sin_repetidos.append(numero)

    return conjunto_sin_repetidos

def generar_conjuntos_con_digitos_unicos(conjuntos: list):

    conjunto_digitos_unicos = []

    if conjuntos:
        for conjunto in conjuntos:
            conjunto_digitos_unicos.append(conjunto_sin_repetidos(conjunto))

    return conjunto_digitos_unicos
