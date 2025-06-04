from utilidades import solicitar_DNI, uno_si
#Condición de Dígito Mayoritario Compartido

def conjuntos_con_minimo_5_elementos(conjuntos):
    #Evalua si los conjuntos tiene como minimo 5 elementos

    if all(len(conjunto) > 4 for conjunto in conjuntos):
        print("Todos los conjuntos tienen como minimo 5 elementos")
    else:
        print("Existe al menos un conjunto que no tiene 5 elementos como minimo")



def existe_digito_en_minimo_tres_conjuntos(conjuntos):
    #Evalua si existe un digito en comun en minimo tres conjuntos

    for i in range(0,10):  # Evalua cada digito existente
        aparicion = 0
        for conjunto in conjuntos:
            aparicion = aparicion + uno_si(i in conjunto)
        if aparicion >= 3:  #Retorna Verdadero en caso de que un numero este en minimo 3 conjuntos
            print("Aparece un digito en minimo tres conjuntos ")
            return
            
    print("No existe ningun digito en minimo 3 conjuntos")

def condicion_mayoritario_compartido(conjuntos):
    #Evalua si se cumple la Condición de Dígito Mayoritario Compartido"
    #Booleano
    if conjuntos_con_minimo_5_elementos(conjuntos) and existe_digito_en_minimo_tres_conjuntos(conjuntos):
        print("Hay Condición de Dígito Mayoritario Compartido")
    else:
        print("No se cumple la Condición de Dígito Mayoritario Compartido")

def integrador_digito_mayoritario():
    conjuntos_dni = solicitar_DNI()
    print(conjuntos_dni)
    conjuntos_con_minimo_5_elementos(conjuntos_dni)
    existe_digito_en_minimo_tres_conjuntos(conjuntos_dni)
    condicion_mayoritario_compartido(conjuntos_dni)