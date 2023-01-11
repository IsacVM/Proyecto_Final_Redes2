from enrutamiento.constantes import (
    DICT_TODOS_LOS_NODOS_RED,
)
import threading
from utils import (
    target_server_enrutamiento,
    target_server_flujo_mensajes,
    target_mandar_datos,
    target_chat
)
from enrutamiento.constantes import (
    DICT_TODOS_LOS_NODOS_RED,
    DICT_DATOS_PARTICULARES_POR_DISPOSITIVO
)
from utils import PrintTxt




def get_index_vecino_por_nombre(nombre_vecino):
    return int(nombre_vecino[-1])


if __name__=='__main__':
    import sys
    DISPOSITIVO_ID=sys.argv[1]

    if DISPOSITIVO_ID in DICT_TODOS_LOS_NODOS_RED:
        #######################################################################
        # creando archivos y adjuntando sus encabezados
        #######################################################################

        archivo_enrutamiento=PrintTxt(f"{DISPOSITIVO_ID}_enrutamiento.txt")
        archivo_flujo_datos=PrintTxt(f"{DISPOSITIVO_ID}_data.txt")
        archivo_enrutamiento.println(f"ID DE DISPOSITIVO: '{DISPOSITIVO_ID}'")
        vector_renglon_pesos=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get('VECTOR_RENGLON_PESOS')[1]
        nombre_vecinos=DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get('NOMBRES_VECINOS')
        archivo_enrutamiento.println(f"VECTOR RENGLON:{vector_renglon_pesos}")
        archivo_enrutamiento.println(f"VECINOS:{nombre_vecinos}")

        tuple_info_nodo=DICT_TODOS_LOS_NODOS_RED.get(DISPOSITIVO_ID,None)

        if tuple_info_nodo:
            ip_nodo,puerto_enrutamiento,puerto_flujo_mensajes=tuple_info_nodo

            # Servidor que se encargara de responder o actualizar la tabla de enrutamiento
            hilo_recibe_vector_distancia = threading.Thread(
                target=target_server_enrutamiento,
                args=(DISPOSITIVO_ID,archivo_enrutamiento,ip_nodo,puerto_enrutamiento)
            )

            # Sevidor para ver el flujo de los mensajes
            hilo_recibe_flujo_mensaje = threading.Thread(
                target=target_server_flujo_mensajes,
                args=(DISPOSITIVO_ID,archivo_flujo_datos,ip_nodo,puerto_flujo_mensajes)
            )
            hilo_recibe_vector_distancia.start()
            hilo_recibe_flujo_mensaje.start()

            # Creando cada hilo que le mantendra a cada vecino informado
            for nombre_vecino in DICT_DATOS_PARTICULARES_POR_DISPOSITIVO.get(DISPOSITIVO_ID).get('NOMBRES_VECINOS'):
                ip_nodo,puerto_enrutamiento,puerto_flujo_mensajes=DICT_TODOS_LOS_NODOS_RED[nombre_vecino]
                hilo_recibe_flujo_mensaje = threading.Thread(
                    target=target_mandar_datos,
                    args=(DISPOSITIVO_ID,nombre_vecino,ip_nodo,puerto_enrutamiento)
                )
                hilo_recibe_flujo_mensaje.start()

            hilo_chat = threading.Thread(
                target=target_chat,
                args=(DISPOSITIVO_ID,)
            )
            hilo_chat.start()
        else:
            print("NODO NO EXISTENTE DENTRO DE LA RED LOCAL...")


        # print(ROUTER_A_VECINOS)




        # index=0
        # for interfaz_red,mac_address in ROUTER_A_TUPLA_INTERFAZ_Y_MAC_ADDRESS_VECINOS:
        #     pass

        
        #   hilo_manda_vector_distancia = threading.Thread(
        #       target=target_mandar_datos,
        #       args=(REGISTRO_MENSAJES_ROUTERS,mac_address,interfaz_red,VECTOR_RENGLON_PESOS)
        #   )
        #   hilo_manda_vector_distancia.start()


        #   hilo_recibe_vector_distancia = threading.Thread(
        #       target=target_recibir_datos,
        #       args=(REGISTRO_MENSAJES_ROUTERS,mac_address,interfaz_red,VECTOR_RENGLON_PESOS)
        #   )
        #   hilo_recibe_vector_distancia.start()

        #   hilo_checa=threading.Thread(
        #       target=target_revisar_conexion_vecino,
        #       args=(REGISTRO_MENSAJES_ROUTERS,VECTOR_RENGLON_PESOS,ROUTER_A_VECINOS[index])
        #   )
        #   hilo_checa.start()
        #   index+=1

    else:
        print("El ID del dispositivo que ingresaste no existe")



