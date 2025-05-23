def verificar_dni(dni):
    return True if len(str(dni)) == 8 else False


def solicitar_DNI():

    cantidad = int(input("Ingrese la cantidad de DNIs a solicitar\n"))
    lista_dni = []

    if cantidad < 0:
        print("La cantidad no puede ser negativa, vuelve a intentarlo nuevamente\n")
        solicitar_DNI()

    for i in range(cantidad):
        dni = int(input(f"Ingrese el {i + 1} DNI\n"))

        while(not verificar_dni(dni)):
            print("El DNI igresado no cuenta con el largo permitido (8). Por favor intentalo nuevamente\n")
            dni = int(input(f"Ingrese el {i + 1} DNI\n"))

        lista_dni.append(dni)

    return lista_dni


print(solicitar_DNI())