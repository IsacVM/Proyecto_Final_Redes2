#------------------------Programa de Cifrado----------------------------------------------
#FUENTE: https://asecuritysite.com/subjects/chapter88

import numpy as np
from cifrado.mixcolumn import mix_column
from cifrado.sub_Bytes import (
    str_to_bin,
    str_split_dec,
    split_list,
    SubBytesHex,
    SubBytesHex_for_matriz,
    SubBytesInvHex
)
from cifrado.AddRoundKey import (
    AddRoundKey,
    AddRoundKey_ini,
    AddRoundKey_matriz,
    Key_schedule
)
from cifrado.shif_rows import (
    shift_rows,
    shift_rows_inverse
)


def cifrar(usr_msg,clave):
    #--------------AddRoundKey --------------------------------
    #Procedemos con la matriz de nuestra 'clave'
    clave_bin = str_to_bin(clave)
    matriz_clave=str_split_dec(clave_bin,8)
    for i in range(len(matriz_clave)):
        matriz_clave[i]= format(matriz_clave[i], 'x')
    matriz_clave=np.array(split_list(matriz_clave)).transpose()
    m_addRK=AddRoundKey(usr_msg,matriz_clave)
    #print("Primer Matriz AddRoundKey\n",m_addRK)


    for i in range(11):
        #clprint("Iteración: ",i)
        #--------------SubBytes --------------------------------
        matriz_SB=SubBytesHex_for_matriz(m_addRK)
        #print("Matriz SubBytes\n",matriz_SB)
        # matriz_InvSB=SubBytesInvHex(matriz_SB)
        # print("Matriz SubBytes Inversa\n",matriz_InvSB)

        #--------------Shift Rows --------------------------------
        matriz_n=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        matriz_n_i=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        matriz_shift=shift_rows(matriz_SB,matriz_n)
        # matriz_shift_inverse=shift_rows_inverse(matriz_shift,matriz_n_i)
        #print ("Matriz Shift-Rows\n",matriz_shift)
        #print ("Matriz Shift-Rows-Inverse\n",matriz_shift_inverse)

        #--------------Mix colums-----------------------------------------------------------------
        if i!=10:
            m_Mix=mix_column(matriz_shift)
        
        #--------------KEY SCHEDULE--& AddRoundKey--------------------------------------------------------------
        #print('KEY SCHEDULE')
        i= 0 if i==10 else i
        nueva_RK=Key_schedule(matriz_clave,number_iteration=i)
        #matriz de retorno
        m_addRK=AddRoundKey(m_Mix,nueva_RK,is_for_usr_msg=False)

    return m_addRK


#-----------------------------main---------------------------------------------------
if __name__=="__main__":
    from utils import input_amount 

    usr_msg= input_amount(message="Ingresa mensaje: ",max_lenght=16)
    data_cifrada=cifrar(usr_msg=usr_msg,clave='My_Add_Round_Key')
    