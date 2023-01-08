#------------------------Programa de la función Sub Bytes----------------------------------------------
#FUENTE: https://asecuritysite.com/subjects/chapter88

from itertools import islice
import numpy as np
#-----------------------------Matriz S-Box-------------------------------------------------------------
Sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

SboxInv = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]



def str_to_bin(cadena):
        cad_bin= ''.join(format(i, '08b') for i in bytearray(cadena, encoding ='utf-8'))
        return cad_bin

def bin_to_Hexa(n):
    
    # convert binary to int
    num = int(n, 2)
    # convert int to hexadecimal
    #hex_num=hex(num)
    hex_num = format(num, 'x')
    return(hex_num)


def hex_to_bin(cadena_hex):
        n = int(cadena_hex, 16)
        cadena_bin = ''
        while n > 0:
            cadena_bin = str(n % 2) + cadena_bin
            n = n >> 1
        return cadena_bin

def bin_to_dec(n):
        return int(n, 2)   


def str_split_dec(usr_msg_bin,n):
    my_str = usr_msg_bin
    my_str_copy = my_str

    my_list = []
    n = n #definimos cada cuantos caracteres se va a dividir la cadena

    while my_str_copy:
        my_list.append(bin_to_dec(my_str_copy[:n]))
        my_str_copy = my_str_copy[n:]

    return my_list

def str_split_bin(usr_msg_bin,n):
    my_str = usr_msg_bin
    my_str_copy = my_str

    my_list = []
    n = n #definimos cada cuantos caracteres se va a dividir la cadena

    while my_str_copy:
        my_list.append(my_str_copy[:n])
        my_str_copy = my_str_copy[n:]
        
    return my_list
    

def split_list(lista):
    # list of length in which we have to split
    length_to_split = [4, 4, 4, 4]
    # Using islice
    Inputt = iter(lista)
    Output = [list(islice(Inputt, elem))
            for elem in length_to_split]
    return Output 

def find_Sbox(lista):
    for i in range(len(lista)):
        lista[i] = format(Sbox[lista[i]],'x') #Buscamo en S #Dec, y convertimos al mismo tiempo a Hexadecimal

def SubBytesHex(usr_msg):
 
    usr_msg_bin = str_to_bin(usr_msg)
    lon_msg = int(len(usr_msg) * 8)
    #esto es por si faltan ceros al principio
    if len(usr_msg_bin) < lon_msg:
        usr_msg_bin = "0" * (lon_msg - len(usr_msg_bin)) + usr_msg_bin
        
    #Verificamos si excede los 128 bits 
    if len(usr_msg_bin) > 128:
        #print("Son mas de 128 bits de mensaje!")
        matriz_subByte=str_split_bin(usr_msg_bin,128)# se agrupa el total de bits del mensaje en grupos de 128
        #print(matriz_subByte)
        for i in range(len(matriz_subByte)):
            if len(matriz_subByte[i])<= 128: 
                matriz_subByte[i] = matriz_subByte[i] +"0" * (128 - len(matriz_subByte[i]))#completamos con padding de '0' las listas de NO 128 bits
                matriz_subByte[i]=str_split_dec(matriz_subByte[i],8)#cada lista la dividimos, los 128/8 para tener los 16Bytes y al mismo tiempo pasamos a decimal
                find_Sbox(matriz_subByte[i]) #Buscamos valor asociados a la posición en decimal de lista dentro de Sbox y obtenemos nuevo equivalente en Hex de la matriz de 'usr_msg' 
                matriz_subByte[i]=split_list(matriz_subByte[i]) #Cada lista de 16 elementos se dividide en 4, para formar una matriz de 4x4
                #print("Listas SubBytes en Hex:", matriz_subByte[i])
            
        #print("Listas",matriz_subByte)
    #Si son menos de 128 bits, entonces los completamos
    elif len(usr_msg_bin) <= 128:
        #print("Son menos de 128 bits de mensaje!")
        usr_msg_bin = usr_msg_bin +"0" * (128 - len(usr_msg_bin))#completamos 
        matriz_subByte=str_split_dec(usr_msg_bin,8)
        find_Sbox(matriz_subByte)
        matriz_subByte=split_list(matriz_subByte)

    return np.array(matriz_subByte).transpose()


def SubBytesInvHex(matriz_subB):
    matriz_InvS=matriz_subB

    for i in range(len(matriz_InvS)):
        for j in range (len( matriz_InvS[i])):    
            matriz_InvS[i][j] = format(SboxInv[int(matriz_InvS[i][j],base=16)],'x') #convertimos al mismo tiempo a Hexadecimal

    return matriz_InvS

def AddRoundKey(usr_msg):
    m_inicial=SubBytesInvHex(SubBytesHex(usr_msg))
    #Procedemos con la matriz de nuestra 'clave'
    clave='My_Add_Round_Key'
    clave_bin = str_to_bin(clave)
    matriz_clave=str_split_dec(clave_bin,8)
    for i in range(len(matriz_clave)):
        matriz_clave[i]= format(matriz_clave[i], 'x')
    
    matriz_clave=np.array(split_list(matriz_clave)).transpose()
    print("Matriz Inicial\n",m_inicial)
    print("Matriz Clave\n",matriz_clave)
    matriz_ARK=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(len(matriz_ARK)):
        for k in range(len(matriz_ARK[j])):    
            matriz_ARK[j][k] =format((int(m_inicial[j][k], 16) ^ int(matriz_clave[j][k], 16)),'x')

    return np.array(matriz_ARK)


def shift_rows(m_SB,matriz_n):
    for fila in range(4):
        a=m_SB[fila][0]
        b=m_SB[fila][1]
        c=m_SB[fila][2]
        d=m_SB[fila][3]
        if fila==0:
                matriz_n[fila][0]=a
                matriz_n[fila][1]=b
                matriz_n[fila][2]=c
                matriz_n[fila][3]=d
        else:
            if fila==1:
                matriz_n[fila][0]=b
                matriz_n[fila][1]=c
                matriz_n[fila][2]=d
                matriz_n[fila][3]=a
        if fila==2:
                matriz_n[fila][0]=c
                matriz_n[fila][1]=d
                matriz_n[fila][2]=a
                matriz_n[fila][3]=b
        else:
            if fila==3:
                matriz_n[fila][0]=d
                matriz_n[fila][1]=a
                matriz_n[fila][2]=b
                matriz_n[fila][3]=c

    return np.array(matriz_n)

def shift_rows_inverse(matriz_shift,matriz_n_i):
    for fila in range(4):
        a=matriz_shift[fila][0]
        b=matriz_shift[fila][1]
        c=matriz_shift[fila][2]
        d=matriz_shift[fila][3]
        if fila==0:
                matriz_n_i[fila][0]=a
                matriz_n_i[fila][1]=b
                matriz_n_i[fila][2]=c
                matriz_n_i[fila][3]=d
        else:
            if fila==1:
                matriz_n_i[fila][0]=d
                matriz_n_i[fila][1]=a
                matriz_n_i[fila][2]=b
                matriz_n_i[fila][3]=c
        if fila==2:
                matriz_n_i[fila][0]=c
                matriz_n_i[fila][1]=d
                matriz_n_i[fila][2]=a
                matriz_n_i[fila][3]=b
        else:
            if fila==3:
                matriz_n_i[fila][0]=b
                matriz_n_i[fila][1]=c
                matriz_n_i[fila][2]=d
                matriz_n_i[fila][3]=a

    return np.array(matriz_n_i)

usr_msg= input("Ingresa mensaje: ")
#--------------AddRoundKey --------------------------------
m_addRK=AddRoundKey(usr_msg)
print("Primer Matriz AddRoundKey\n",m_addRK)
#--------------SubBytes --------------------------------
matriz_SB=SubBytesHex(usr_msg)
print("Matriz SubBytes\n",matriz_SB)
#matriz_InvSB=SubBytesInvHex(matriz_SB)
#print(matriz_InvSB)

#--------------Shift Rows --------------------------------
matriz_n=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matriz_n_i=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

matriz_shift=shift_rows(matriz_SB,matriz_n)
matriz_shift_inverse=shift_rows_inverse(matriz_shift,matriz_n_i)

print ("Matriz Shift-Rows\n",matriz_shift)

print ("Matriz Shift-Rows-Inverse\n",matriz_shift_inverse)