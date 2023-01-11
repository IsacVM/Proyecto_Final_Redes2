import numpy as np
from sub_Bytes import (
    SubBytesHex,
    SubBytesInvHex,
    SubBytes_of_4B
)

def RotWord(matriz_clave):
    last_colum=matriz_clave.transpose()[3]
    return np.roll(last_colum,-1)

def Key_schedule(matriz_clave,number_iteration):
    colum_RotWord=RotWord(matriz_clave)
    #print("RotWord\n",colum_RotWord)

    #--------------AddRoundKey---SubBytes (se aplica subBytes a RotWord_c)----------------
    #m_prueba=(['08','0C','10','04'])

    colum_SB4=SubBytes_of_4B(colum_RotWord)
    #print("SubBytes de 4 Bytes\n",colum_SB4)  

    #--------------AddRoundKey---XOR and Rcon table-----
    #----Se hace XOR entre colum_SB4 con la segunda columna de matriz clave y con primara columna de tabla Rcon

    Rcon_table=[['01','00','00','00'],['02','00','00','00'],['04','00','00','00'],['08','00','00','00'],['10','00','00','00'],['20','00','00','00'],['40','00','00','00'],['80','00','00','00'],['1b','00','00','00'],['36','00','00','00']]
    colum_Rcon=Rcon_table[number_iteration-1]# el Round 1 debe tener el indice '0'
    #print(colum_Rcon)

    #Rcon 1st colum:
    New_RK=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #colum_SB4_p=['30','FE','CA','F2']
    colum1_mClave=matriz_clave.transpose()[0]
    # print(colum1_mClave)
    for i in range(len(New_RK)):
        New_RK[0][i]=format((int(colum_SB4[i], 16) ^ int(colum1_mClave[i], 16)^ int(colum_Rcon[i], 16)),'x')

    primera_c=np.array(New_RK)[0]
    #print("1ra columna New_ARK\n",primera_c)

    #Rcon 2sd colum:
    colum2_mClave=matriz_clave.transpose()[1]
    # print(colum2_mClave)
    for i in range(len(New_RK)):
        New_RK[1][i]=format((int(primera_c[i], 16) ^ int(colum2_mClave[i], 16)),'x')
        
    segunda_c=np.array(New_RK)[1]   
    #print("2da columna New_ARK\n",segunda_c)

    #Rcon 3rd colum:
    colum3_mClave=matriz_clave.transpose()[2]
    # print(colum3_mClave)
    for i in range(len(New_RK)):
        New_RK[2][i]=format((int(segunda_c[i], 16) ^ int(colum3_mClave[i], 16)),'x')

    tercera_c=np.array(New_RK)[2]   
    #print("3ra columna New_ARK\n",tercera_c)

    #Rcon 4th colum:
    colum4_mClave=matriz_clave.transpose()[3]
    # print(colum4_mClave)
    for i in range(len(New_RK)):
        New_RK[3][i]=format((int(tercera_c[i], 16) ^ int(colum4_mClave[i], 16)),'x')

    cuarta_c=np.array(New_RK)[3]   
    #print("4ta columna New_ARK\n",cuarta_c)

    #Nueva matriz RoundKey:
    NewM_RK=np.array(New_RK).transpose()
    return NewM_RK


def AddRoundKey_ini(usr_msg,matriz_clave):
    #m_inicial= SubBytesInvHex(SubBytesHex(usr_msg_or_matriz)) if is_for_usr_msg else usr_msg_or_matriz
    m_inicial=SubBytesInvHex(SubBytesHex(usr_msg))
    #print("Matriz Inicial\n",m_inicial)
    #print("Matriz Clave\n",matriz_clave)
    matriz_ARK=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(len(matriz_ARK)):
        for k in range(len(matriz_ARK[j])):    
            matriz_ARK[j][k] =format((int(m_inicial[j][k], 16) ^ int(matriz_clave[j][k], 16)),'x')
    #print(matriz_ARK)
    return np.array(matriz_ARK)


def AddRoundKey_matriz(m_inicial,matriz_clave):
    
    print("Matriz Inicial de Segundo ADD\n",m_inicial)
    print("Matriz Clave de Segundo ADD\n",matriz_clave)
    matriz_ARK_m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(len(matriz_ARK_m)):
        for k in range(len(matriz_ARK_m[j])):    
            matriz_ARK_m[j][k] =format((int(m_inicial[j][k], 16) ^ int(matriz_clave[j][k], 16)),'x')
    print(matriz_ARK_m)
    return (matriz_ARK_m)    

def AddRound_Key(usr_msg_or_matriz,matriz_clave,is_for_usr_msg=True):
    m_inicial=SubBytesInvHex(SubBytesHex(usr_msg_or_matriz)) if is_for_usr_msg else usr_msg_or_matriz
    print("Matriz Inicial\n",m_inicial)
    #print("Matriz Clave\n",matriz_clave)
    matriz_ARK=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(len(matriz_ARK)):
        for k in range(len(matriz_ARK[j])):    
            matriz_ARK[j][k] =format((int(m_inicial[j][k],16) ^ int(matriz_clave[j][k],16)),'x')
    #print(matriz_ARK)
    return np.array(matriz_ARK)    