#Condición de Dígito Mayoritario Compartido

def conjuntos_con_minimo_5_elementos(conjuntos):
    #Evalua si los conjuntos tiene como minimo 5 elementos
    #Booleano
    conjuntos_validos = True

    for conjunto in conjuntos:
        conjuntos_validos = conjuntos_validos and len(conjunto) > 4
    
    return conjuntos_validos

def uno_si(condicion):
    #Retorna verdadero en caso de que la condicion sea verdadera
    #Integer
    return 1 if condicion else 0

def existe_digito_en_minimo_tres_conjuntos(conjuntos):
    #Evalua si existe un digito en comun en minimo tres conjuntos
    #Booleano

    for i in range(0,10):  # Evalua cada digito existente
        aparicion = 0
        for conjunto in conjuntos:
            aparicion = aparicion + uno_si(i in conjunto)
        if aparicion >= 3:  #Retorna Verdadero en caso de que un numero este en minimo 3 conjuntos
            return True
    return False
    

def condicion_mayoritario_compartido(conjuntos):
    #Evalua si se cumple la Condición de Dígito Mayoritario Compartido"
    #Booleano

    if conjuntos_con_minimo_5_elementos(conjuntos) and existe_digito_en_minimo_tres_conjuntos(conjuntos):
        print("Hay Condición de Dígito Mayoritario Compartido")
    else:
        print("No se cumple la Condición de Dígito Mayoritario Compartido")