from prettytable import PrettyTable as pt
import math
infinito=math.inf


def mostrar_tabla(lista_ids_dispositivos,lista_old,lista_nombres_old,lista_recv,lista_actual,lista_nombres_vecinos_actual):
    id_recibio=lista_ids_dispositivos[ lista_old.index(0) ]
    id_mando=lista_ids_dispositivos[ lista_recv.index(0) ]

    headers = ["ID"] + ['OLD '+id_recibio,id_mando,'NEW '+id_recibio+':'+id_recibio+'<---'+id_mando]

    tb = pt()
    #Add headers
    tb.field_names = headers
    #Add rows
    renglones=len(lista_ids_dispositivos)

    for index in range(renglones):
        id_dispositivo=lista_ids_dispositivos[index]
        
        nombre_vecino_ex=lista_nombres_old[index]
        old_value=f"{lista_old[index]}({nombre_vecino_ex})" 
        
        recv_value=lista_recv[index]

        nombre_vecino=lista_nombres_vecinos_actual[index]
        current_value=f"{lista_actual[index]}({nombre_vecino})"
        
        
        row=[id_dispositivo,old_value,recv_value,current_value]
        tb.add_row(row)
    return tb


# Valor de la lista asociadas a los nodos A,B,C de la siguiente forma: [A,B,C]

#old=[0,2,infinito]    #lista anterior a actualizarse (Ex. old A)
#recv=[2,0,6]   #lista recibida de algun nodo
#actual=[0,2,6]   #lista con peso actualizados (Ex. new A)
#mostrar_tabla(old, recv, actual)