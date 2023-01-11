import copy
import socket
import pickle
from enrutamiento.vector_distancia import (
  actualizar_pesos,
  autor_index
)
from enrutamiento.mostrar_vector import (
  mostrar_tabla
)
from enrutamiento.constantes import (
  DICT_DATOS_PARTICULARES_POR_DISPOSITIVO,
  DICT_TODOS_LOS_NODOS_RED
)
from enrutamiento import convenciones

import time
import math
import uuid
import json

INFINITO=math.inf
SIZE_BUFFER=3096
ENCODING="utf-8"

class PrintTxt():
  def __init__(self,nombre_archivo):
    self.nombre_archivo=nombre_archivo
    self.clean_file()
  
  def clean_file(self):
    with open(self.nombre_archivo,'w') as secre:
      secre.write("")
    
  def println(self,data:str=None):
    if data==None or data=="":
      data=""
    data+="\n"
    with open(self.nombre_archivo,'a') as secre:
      secre.write(data)

  def print(self,data:str):
    with open(self.nombre_archivo,'a') as secre:
      secre.write(data)


def input_amount(message,max_lenght): 
    x=input(message)[:max_lenght]
    return x

def target_revisar_conexion_vecino(DISPOSITIVO_ID,indice_vecino):
  REGISTRO_MENSAJES_ROUTERS=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get("REGISTRO_MENSAJES_ROUTERS")
  vector_distancia=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get("VECTOR_RENGLON_PESOS")[1]
  vector_distancia_nombres=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get("VECTOR_RENGLON_PESOS")[0]

  while True:
    prev_value=REGISTRO_MENSAJES_ROUTERS[indice_vecino]
    time.sleep(10)
    new_value=REGISTRO_MENSAJES_ROUTERS[indice_vecino]
    if prev_value==new_value:
      vector_distancia[indice_vecino]=INFINITO
      vector_distancia_old=copy.deepcopy(vector_distancia)
      vector_distancia_nombres_old=copy.deepcopy(vector_distancia_nombres)


      vector_distancia[indice_vecino]=INFINITO
      vector_distancia_nombres[indice_vecino]=None

      vector_infinito=[INFINITO]*len(vector_distancia)
      vector_infinito[indice_vecino]=0

      print("**************************************")
      tabla=mostrar_tabla(
        lista_ids_dispositivos=list(DICT_TODOS_LOS_NODOS_RED.keys()),
        lista_old=vector_distancia_old,
        lista_nombres_old=vector_distancia_nombres_old,
        lista_recv=vector_infinito,
        lista_actual=vector_distancia,
        lista_nombres_vecinos_actual=vector_distancia_nombres
      )


def target_server_enrutamiento(DISPOSITIVO_ID,archivo_enrutamiento,ip_server,port_server):
  REGISTRO_MENSAJES_ROUTERS=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get("REGISTRO_MENSAJES_ROUTERS")
  vector_distancia_nombres=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get("VECTOR_RENGLON_PESOS")[0]
  vector_distancia=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get("VECTOR_RENGLON_PESOS")[1]
  
  my_socket=socket.socket(
      family=socket.AF_INET,      # socket.AF_INET = Internet protocol IPv4
                                  # socket.AF_INET6 = Internet protocol IPv6
      type=socket.SOCK_STREAM     # socket.SOCK_STREAM = Protocol TCP
                                  # socket.AF_INET6 = Protocol UDP
      )
  my_socket.bind( (ip_server,port_server) )
  my_socket.listen()

  numero_tabla=0
  while True:
    try:
      numero_tabla+=1
      my_client,addres=my_socket.accept()
      message_client=my_client.recv(SIZE_BUFFER)
      vector_distancia_llego_nombres,vector_distancia_llego=pickle.loads(message_client) 
      vector_distancia_nuevo_nombres,vector_distancia_nuevo=actualizar_pesos(
          (vector_distancia_nombres,vector_distancia),
          (vector_distancia_llego_nombres,vector_distancia_llego)
      )
      index_vecino=autor_index(vector_distancia_llego)
      REGISTRO_MENSAJES_ROUTERS[index_vecino]+=1
      archivo_enrutamiento.println()
      # print()

      archivo_enrutamiento.println("***************************************")
      # print("***************************************")

      archivo_enrutamiento.println(f"    TABLA '{DISPOSITIVO_ID}' NUMERO:{numero_tabla}       ")
      # print(f"    TABLA '{DISPOSITIVO_ID}' NUMERO:{numero_tabla}       ")


      archivo_enrutamiento.println("***************************************")
      # print("***************************************")

      archivo_enrutamiento.println()
      # print()


      tabla=mostrar_tabla(
          lista_ids_dispositivos=list(DICT_TODOS_LOS_NODOS_RED.keys()),
          lista_old=vector_distancia,
          lista_nombres_old=vector_distancia_nombres,
          lista_recv=vector_distancia_llego,
          lista_actual=vector_distancia_nuevo,
          lista_nombres_vecinos_actual=vector_distancia_nuevo_nombres
      )
      archivo_enrutamiento.println(str(tabla))


      # actualizar vector renglon por referencia:
      numero_nodos=len(vector_distancia)
      indice=0
      while indice<numero_nodos:
          vector_distancia[indice]=vector_distancia_nuevo[indice]
          vector_distancia_nombres[indice]=vector_distancia_nuevo_nombres[indice]
          indice+=1
      else:
          pass
    except KeyboardInterrupt:
      my_socket.close()
      my_socket=None
      break


def target_chat(DISPOSITIVO_ID):
  while True:
    mensaje=input(f"{DISPOSITIVO_ID}...(refrescar=solo enter)$$: ")
    if mensaje=='':
      pass
    else:
      id_destino,mensaje=mensaje.split(" ",maxsplit=1)
      if id_destino in DICT_TODOS_LOS_NODOS_RED:
        index_destino=convenciones.get_index(id_destino)
        distancia_destino=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO[DISPOSITIVO_ID]['VECTOR_RENGLON_PESOS'][1][index_destino]
        if distancia_destino!=INFINITO:
          id_dispositivo_siguiente=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO[DISPOSITIVO_ID]['VECTOR_RENGLON_PESOS'][0][index_destino]
          ip_siguiente,puerto_enrutamiento,puerto_flujo_mensajes=DICT_TODOS_LOS_NODOS_RED[id_dispositivo_siguiente]
          historial_ruta=[DISPOSITIVO_ID]
          dict_datos_mandar={
            'id':str(uuid.uuid4()),
            'origen':DISPOSITIVO_ID,
            'destino':id_destino,
            'anterior':DISPOSITIVO_ID,
            'siguiente':id_dispositivo_siguiente,
            'historial_ruta':historial_ruta,
            'distancia_esperada':distancia_destino,
            'mensaje':mensaje
          }
          my_socket=socket.socket(
              family=socket.AF_INET,      # socket.AF_INET = Internet protocol IPv4
                                          # socket.AF_INET6 = Internet protocol IPv6
              type=socket.SOCK_STREAM     # socket.SOCK_STREAM = Protocol TCP
                                          # socket.AF_INET6 = Protocol UDP
              )
          try:
            my_socket.connect( (ip_siguiente,puerto_flujo_mensajes) )
            message_bytes=bytes( pickle.dumps(dict_datos_mandar) )
            my_socket.send( message_bytes)
            my_socket.close()
            print(f"Exito al mandar mensaje")
          except:
            print(f"Fallo al mandar mensaje")
            my_socket.close()
        else:
          print("Este dispositivo no puede llegar al destino")
      else:
        print("Al dispositivo que le quieres mandar mensaje no existe")


def target_server_flujo_mensajes(DISPOSITIVO_ID,archivo_flujo_datos,ip_server,port_server): 
  my_socket=socket.socket(
      family=socket.AF_INET,      # socket.AF_INET = Internet protocol IPv4
                                  # socket.AF_INET6 = Internet protocol IPv6
      type=socket.SOCK_STREAM     # socket.SOCK_STREAM = Protocol TCP
                                  # socket.AF_INET6 = Protocol UDP
      )
  my_socket.bind( (ip_server,port_server) )
  my_socket.listen()

  numero_tabla=0
  while True:
      try:
          numero_tabla+=1
          my_client,addres=my_socket.accept()
          message_client=my_client.recv(SIZE_BUFFER)
          dict_mensaje_llego=pickle.loads(message_client)

          archivo_flujo_datos.println("***************************************")
          archivo_flujo_datos.println(f"    MENSAJE ID: '{dict_mensaje_llego['id']}' ")
          archivo_flujo_datos.println("***************************************")
          archivo_flujo_datos.println(
                json.dumps(dict_mensaje_llego,indent=3)
          )
          archivo_flujo_datos.println()
          archivo_flujo_datos.println()

          if dict_mensaje_llego['destino']==DISPOSITIVO_ID:
            mensaje=dict_mensaje_llego['mensaje']
            texto_mostrar=f"El dispositivio {dict_mensaje_llego['origen']} te mando el siguiente mensaje: {mensaje}"
            archivo_flujo_datos.println(texto_mostrar)

          else:
              index_destino=convenciones.get_index(dict_mensaje_llego['destino'])
              distancia_destino=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO[DISPOSITIVO_ID]['VECTOR_RENGLON_PESOS'][1][index_destino]
              if distancia_destino!=INFINITO:
                id_dispositivo_siguiente=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO[DISPOSITIVO_ID]['VECTOR_RENGLON_PESOS'][0][index_destino]
                ip_siguiente,puerto_enrutamiento,puerto_flujo_mensajes=DICT_TODOS_LOS_NODOS_RED[id_dispositivo_siguiente]
                historial_ruta=dict_mensaje_llego['historial_ruta']+[DISPOSITIVO_ID]
                dict_mensaje_llego['siguiente']=id_dispositivo_siguiente
                dict_mensaje_llego['historial_ruta']=historial_ruta
                dict_mensaje_llego['anterior']=DISPOSITIVO_ID
                archivo_flujo_datos.println(
                      "Mensaje que se enviara:"
                )
                archivo_flujo_datos.println(
                      json.dumps(dict_mensaje_llego,indent=3)
                )

                my_socket=socket.socket(
                    family=socket.AF_INET,      # socket.AF_INET = Internet protocol IPv4
                                                # socket.AF_INET6 = Internet protocol IPv6
                    type=socket.SOCK_STREAM     # socket.SOCK_STREAM = Protocol TCP
                                                # socket.AF_INET6 = Protocol UDP
                    )
                try:
                  my_socket.connect( (ip_siguiente,puerto_flujo_mensajes) )
                  message_bytes=bytes( pickle.dumps(dict_mensaje_llego) )
                  my_socket.send( message_bytes)
                  my_socket.close()
                  archivo_flujo_datos.print(f"Exito al mandar mensaje")
                except:
                  archivo_flujo_datos.print(f"Fallo al mandar mensaje")
                  my_socket.close()
              else:
                archivo_flujo_datos.print("Este dispositivo no puede llegar al destino")
 
          # print("ruta_completa",ruta_completa)
          # print("ruta_actual",ruta_actual)
          # print("mensaje",manesaje)
      except KeyboardInterrupt:
          my_socket.close()
          my_socket=None
          # print("Finish comunication.")
          break


  
def target_mandar_datos(DISPOSITIVO_ID,vecino_id,ip_server,port_server):
  
  # port_serv: 1,024 to 49,151
  no_mensajes_enviados=1
  while True:
    try:
      my_socket=socket.socket(
          family=socket.AF_INET,      # socket.AF_INET = Internet protocol IPv4
                                      # socket.AF_INET6 = Internet protocol IPv6
          type=socket.SOCK_STREAM     # socket.SOCK_STREAM = Protocol TCP
                                      # socket.AF_INET6 = Protocol UDP
          )
      try:
        vector_distancia=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get("VECTOR_RENGLON_PESOS")
        my_socket.connect( (ip_server,port_server) )
        message_bytes=bytes( pickle.dumps(vector_distancia) )
        my_socket.send( message_bytes)
        my_socket.close()
        # print(f"Exito al mandar mensaje numero: {no_mensajes_enviados} de:{DISPOSITIVO_ID} a: {vecino_id} ip:{ip_server}, puerto:{port_server}")
      except:
        # print(f"Exito al mandar mensaje numero: {no_mensajes_enviados} de:{DISPOSITIVO_ID} a: {vecino_id} ip:{ip_server}, puerto:{port_server}")
        my_socket.close()
    except:
      pass
      # print(f"Exito al mandar mensaje numero: {no_mensajes_enviados} de:{DISPOSITIVO_ID} a: {vecino_id} ip:{ip_server}, puerto:{port_server}")
    time.sleep(2)


