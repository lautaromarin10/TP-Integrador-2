from utilidades import conjunto_sin_repetidos

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
