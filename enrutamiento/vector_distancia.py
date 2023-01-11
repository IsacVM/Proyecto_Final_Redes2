
import math
import copy

#Definición de infinito, infinito es de tipo FLOAT
INFINITO=math.inf

def get_vecinos(vector_pesos):
    list_indices_vecinos=[]
    for indice,peso in enumerate(vector_pesos):
        if peso!=INFINITO and peso!=0:
            list_indices_vecinos.append(indice)
    return list_indices_vecinos


############ QUIEN ES EL QUE MANDA ##################
def autor_index(lista):
    autor = lista.index(0)
    return autor

#lista es old_lista
#lista_2 es la lista que se le manda para actualizar lista
########### CONSTANTE PARA SUMAR ###################

def constante_suma(lista,lista_2):
    autor = autor_index(lista)
    constante = lista_2[autor]
    return constante


################ OPERACIÓN ####################
def actualizar_pesos(lista, lista_2):
    lista_nombres,lista=lista
    lista_2_nombres,lista_2=lista_2

    constante = constante_suma(lista,lista_2)
    index_vecino=autor_index(lista_2)
    index_vecino=lista_2_nombres[index_vecino]
    new_lista=[]
    new_lista_nombres=[]
    for index in range(len(lista_2)):
        old_lista=lista[index]
        update_lista=lista_2[index]
        old_nombre=lista_nombres[index]
        update_nombre=lista_2_nombres[index]
        update_lista_cte = float(constante)+float(update_lista)
        if float(old_lista)> update_lista_cte:
            new_lista.append(update_lista_cte)
            new_lista_nombres.append(index_vecino)
        else:
            new_lista.append(old_lista)
            new_lista_nombres.append(old_nombre)

    return new_lista_nombres,new_lista
