UNIFICADOR_VECINDAD=0
##################################################
#  CONSTANTES:
##################################################
import math
import random
from enrutamiento import convenciones

#Definición de infinito, infinito es de tipo FLOAT
INFINITO=math.inf


# PUERTOS DISPONILES... 1,024 to 49,151
DICT_TODOS_LOS_NODOS_RED={
    'ISAC~1':("25.51.250.55",30000,30031),
    'DAFNE~2':("25.6.211.129",30100,30101),
    'ALAN~3':("25.43.227.248",30034,30035)
}

DICT_VECINOS={
  'ISAC~1':['DAFNE~2','ALAN~3'],
  'DAFNE~2':['ISAC~1'],
  'ALAN~3':['ISAC~1'],
}

max_value=15
random.seed(UNIFICADOR_VECINDAD)
DICT_DATOS_PARTICULARES_POR_DISPOSITIVO={}
dict_combinaciones_con_valor={}
for id_dispositivo,lista_ids_vecinos in DICT_VECINOS.items():
    vector_renglon_pesos=[INFINITO]*len(DICT_VECINOS)
    vector_renglon_nombres=[None]*len(DICT_VECINOS)
    
    index_dispositivo=convenciones.get_index(id_dispositivo)
    vector_renglon_pesos[index_dispositivo]=0
    vector_renglon_nombres[index_dispositivo]=id_dispositivo
    
    lista_ids_pesos_vecinos=[]
    for id_vecino in lista_ids_vecinos:
      index_vecino=convenciones.get_index(id_vecino)
      if int(index_dispositivo)<int(index_vecino):
          combinacion=id_dispositivo,id_vecino
      else:
          combinacion=id_vecino,id_dispositivo
      dict_combinaciones_con_valor[combinacion]=dict_combinaciones_con_valor.get( combinacion,random.randint(1,max_value) )
      vector_renglon_pesos[index_vecino]=dict_combinaciones_con_valor[combinacion]
      vector_renglon_nombres[index_vecino]=id_vecino
    dict_datos={
        'VECTOR_RENGLON_PESOS':(vector_renglon_nombres,vector_renglon_pesos,),
        'NOMBRES_VECINOS':DICT_VECINOS[id_dispositivo],
        'REGISTRO_MENSAJES_ROUTERS':[0]*len(DICT_VECINOS)
    }
    DICT_DATOS_PARTICULARES_POR_DISPOSITIVO[id_dispositivo]=dict_datos
