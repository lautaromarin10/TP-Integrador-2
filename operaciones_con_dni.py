from utilidades import solicitar_DNI, unificacion_conjuntos

def generar_conjuntos_con_digitos_unicos(conjuntos: list):

    conjunto_digitos_unicos = []

    if conjuntos:
        for lista_dni in conjuntos:
            digitos_por_dni = []
            for dni in lista_dni:
                # Convertir el DNI a string y extraer dígitos únicos
                digitos = [int(d) for d in str(dni)]
                digitos_unicos = list(set(digitos))
                digitos_por_dni.append(digitos_unicos)
            conjunto_digitos_unicos.extend(digitos_por_dni)

    print(f"En base a estos conjuntos: {conjuntos}")
    print(f"Generamos la lista de conjuntos únicos por DNI: {conjunto_digitos_unicos}")
    return conjunto_digitos_unicos

#Conteo de frecuencia de cada digito en cada DNI:
def frecuencia_digitos(dni):
    conteo = {str(i): 0 for i in range(10)}
    for dig in str(dni):
        conteo[dig] += 1
    return conteo

def frecuencia_digitos_conjuntos_dni(conjuntos: list):

    lista_dni = conjuntos[0]

    for dni in lista_dni:
        print(f"Frecuencia de digitos del DNI {dni}: {frecuencia_digitos(dni)}")


#Suma total de los digitos en cada DNI
def suma_digitos(dni):
    return sum(int(d) for d in str(dni))

def suma_de_todos_los_dni(conjuntos: list):

    lista_dni = conjuntos[0]

    for dni in lista_dni:
        print(f"La suma de los digitos unicos de {dni} da como resultado {suma_digitos(dni)}")


def integrador_operacion_con_dni():
    conjunto_dni = solicitar_DNI()
    frecuencia_digitos_conjuntos_dni(conjunto_dni)
    conjunto_dni_digitos_unicos = generar_conjuntos_con_digitos_unicos(conjunto_dni)
    unificacion_conjuntos(conjunto_dni_digitos_unicos)
    suma_de_todos_los_dni(conjunto_dni)

integrador_operacion_con_dni()