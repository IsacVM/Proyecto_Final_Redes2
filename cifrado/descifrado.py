#------------------------Programa de Descifrado---------------------------------------------


import numpy as np
from cifrado.mixcolumn import (
    mix_column, 
    Inv_mix_column)
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
    Key_schedule
)
from cifrado.shif_rows import (
    shift_rows,
    shift_rows_inverse
)


def des_cifrar(data_cifrada):
    #--------------AddRoundKey --------------------------------
    #Procedemos con la matriz de nuestra 'clave'
    clave='My_Add_Round_Key'
    clave_bin = str_to_bin(clave)
    matriz_clave=str_split_dec(clave_bin,8)
    for i in range(len(matriz_clave)):
        matriz_clave[i]= format(matriz_clave[i], 'x')
    matriz_clave=np.array(split_list(matriz_clave)).transpose()
    m_addRK=AddRoundKey(data_cifrada,matriz_clave)
  


    for i in range(11):
        #--------------Inv Shift Rows --------------------------------
        matriz_n=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        matriz_n_i=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        #matriz_shift=shift_rows(matriz_SB,matriz_n)
        matriz_shift_inverse=shift_rows_inverse(m_addRK,matriz_n_i)
        #print ("Matriz Shift-Rows-Inverse\n",matriz_shift_inverse)

        #--------------Inv SubBytes --------------------------------
        matriz_InvSB=SubBytesInvHex(matriz_shift_inverse)
        #print("Matriz SubBytes Inversa\n",matriz_InvSB)

        #--------------Inv Mix colums-----------------------------------------------------------------
        if i!=10:
            m_InvMc=Inv_mix_column(matriz_InvSB)
        
        #--------------KEY SCHEDULE--& AddRoundKey--------------------------------------------------------------
        #print('KEY SCHEDULE')
        i= 0 if i==10 else i
        nueva_RK=Key_schedule(matriz_clave,number_iteration=i)
        #matriz de retorno
        m_addRK=AddRoundKey(m_InvMc,nueva_RK,is_for_usr_msg=False)

    return m_addRK


#-----------------------------main---------------------------------------------------
if __name__=="__main__":
    from utils import input_amount 
    
    data_des_cifrada=cifrar(data_cifrada)
    print("Matriz de Des_Cifrado\n",data_des_cifrada)