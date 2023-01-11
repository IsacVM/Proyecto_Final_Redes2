#------------------------Programa de Cifrado----------------------------------------------
#FUENTE: https://asecuritysite.com/subjects/chapter88

import numpy as np

from mixColum import mixColumn
from sub_Bytes import (
    str_to_bin,
    str_split_dec,
    split_list,
    SubBytesHex,
    SubBytesHex_for_matriz,
    SubBytesInvHex
)
from AddRoundKey import (
    AddRound_Key,
    AddRoundKey_ini,
    AddRoundKey_matriz,
    Key_schedule
)
from shif_rows import (
    shift_rows,
    shift_rows_inverse
)


def cifrar(usr_msg,clave):
    #--------------AddRoundKey --------------------------------
    #Ronda 1

    #Procedemos con la matriz de nuestra 'clave'
    clave_bin = str_to_bin(clave)
    matriz_clave=str_split_dec(clave_bin,8)
    for i in range(len(matriz_clave)):
        matriz_clave[i]= format(matriz_clave[i], 'x')
    matriz_clave=np.array(split_list(matriz_clave)).transpose()
    m_addRK=AddRound_Key(usr_msg,matriz_clave,is_for_usr_msg=True)
    #print("Primer Matriz AddRoundKey\n",m_addRK)
    print("Ronda inicial")
    #De Ronda 1 hasta la Ronda 9
    for i in range(1,10):
        print("Ronda #: ",i)
        #--------------SubBytes --------------------------------
        matriz_SB=SubBytesHex_for_matriz(m_addRK)
        print("Matriz SubBytes\n",matriz_SB)
        # matriz_InvSB=SubBytesInvHex(matriz_SB)
        # print("Matriz SubBytes Inversa\n",matriz_InvSB)

        #--------------Shift Rows --------------------------------
        matriz_n=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        matriz_shift=shift_rows(matriz_SB,matriz_n)
        matriz_shift=np.array(matriz_shift).transpose() #para que las columnas sean filas
        # matriz_shift_inverse=shift_rows_inverse(matriz_shift,matriz_n_i)
        print ("Matriz Shift-Rows\n",matriz_shift)
        #print ("Matriz Shift-Rows\n",np.array(matriz_shift).transpose())
        #print ("Matriz Shift-Rows-Inverse\n",matriz_shift_inverse)

        #--------------Mix colums-----------------------------------------------------------------
        #if i!=10:
        v_shift=[]
        for i in matriz_shift:
            v_shift=v_shift+list(i)

        #PASAMOS a dec vector shift
        for i in range(len(v_shift)): 
            v_shift[i]=int(v_shift[i],16)

        #separar en bloques de columna
        print ("Antes del Mix en decimal m_shift\n ",v_shift)    

        mixColumn(v_shift)
        print ("Matriz Mix Column\n",v_shift)

        m_Mix=split_list(v_shift)
        
        #--------------KEY SCHEDULE--& AddRoundKey--------------------------------------------------------------
        #print('KEY SCHEDULE')
        #i= 0 if i==10 else i
        nueva_RK=Key_schedule(matriz_clave,number_iteration=i)
        print ("Matriz Round Key\n",nueva_RK)
        #matriz de retorno
        m_addRK=AddRound_Key(m_Mix,nueva_RK,is_for_usr_msg=False)
        print ("Matriz ADD Round Key\n",m_addRK)

    #Ronda 10 Final :
    #--------------SubBytes --------------------------------
    matriz_SB=SubBytesHex_for_matriz(m_addRK)
    #--------------Shift Rows --------------------------------
    matriz_n=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    matriz_shift=shift_rows(matriz_SB,matriz_n)
    #--------------Mix colums-----------------------------------------------------------------
    m_Mix=mix_column(matriz_shift)
    #--------------KEY SCHEDULE--& AddRoundKey--------------------------------------------------------------
    nueva_RK=Key_schedule(matriz_clave,number_iteration=10)
    #matriz de retorno
    m_addRK=AddRound_Key(m_Mix,nueva_RK,is_for_usr_msg=False)

    return m_addRK



#-----------------------------main---------------------------------------------------
#if __name__=="__main__":
#    from utils import input_amount 

#usr_msg= input_amount(message="Ingresa mensaje: ",max_lenght=16)
usr_msg= input("Ingresa mensaje: ")
data_cifrada=cifrar(usr_msg,'Thats my Kung Fu')
print(data_cifrada)