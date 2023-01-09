import numpy as np


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
