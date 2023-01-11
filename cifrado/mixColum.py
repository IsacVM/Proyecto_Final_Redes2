from copy import copy

#import numpy as np

def galoisMult(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256


def mixColumn(column):
    temp = copy(column)
    column[0] = galoisMult(temp[0],2) ^ galoisMult(temp[3],1) ^ \
                galoisMult(temp[2],1) ^ galoisMult(temp[1],3)
    column[1] = galoisMult(temp[1],2) ^ galoisMult(temp[0],1) ^ \
                galoisMult(temp[3],1) ^ galoisMult(temp[2],3)
    column[2] = galoisMult(temp[2],2) ^ galoisMult(temp[1],1) ^ \
                galoisMult(temp[0],1) ^ galoisMult(temp[3],3)
    column[3] = galoisMult(temp[3],2) ^ galoisMult(temp[2],1) ^ \
		    galoisMult(temp[1],1) ^ galoisMult(temp[0],3)



def mixColumnInv(column):
    temp = copy(column)
    column[0] = galoisMult(temp[0],14) ^ galoisMult(temp[3],9) ^ \
                galoisMult(temp[2],13) ^ galoisMult(temp[1],11)
    column[1] = galoisMult(temp[1],14) ^ galoisMult(temp[0],9) ^ \
                galoisMult(temp[3],13) ^ galoisMult(temp[2],11)
    column[2] = galoisMult(temp[2],14) ^ galoisMult(temp[1],9) ^ \
                galoisMult(temp[0],13) ^ galoisMult(temp[3],11)
    column[3] = galoisMult(temp[3],14) ^ galoisMult(temp[2],9) ^ \
		    galoisMult(temp[1],13) ^ galoisMult(temp[0],11)



#m_shift=[['52','21','02','FE'],['45','33','D7','9F'],['F1','AB','9F','8F'],['76','AA','F9','2B']]

#lista=[]
#for i in m_shift:
#    lista=lista+list(i)

#PASAMOS A dec vector g
#for i in range(len(lista)): 
    lista[i]=int(lista[i],16)

#print ("Antes del Mix en decimal m_shift\n ",lista)    

 
#mixColumn(m_shift)
#m_shift=np.array(m_shift)
#print('Mixed:\n',m_shift)

#mixColumnInv(g_inv)
#print ('Inverse mixed\n', g_inv)