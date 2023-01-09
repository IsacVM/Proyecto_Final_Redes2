################################################################################
#  l    i   s   t   a        h  e   x   a
################################################################################

def str_int(lista):
    list_aux=[]
    for i in range(0,8):
        if lista[i]==0:
            list_aux.append('0')
        else:
            list_aux.append('1')

    juntar=''.join(list_aux)
    auxx=conversor_binario_a_hexadecimal(juntar)
    return auxx

def conversor_binario_a_hexadecimal(juntar):
    bnum = int(juntar)

    h = 0
    m = 1
    chk = 1
    i = 0
    hnum = []
    while bnum!=0:
        rem = bnum%10
        h = h + (rem*m)
        if chk%4==0:
            if h<10:
                hnum.insert(i, chr(h+48))
            else:
                hnum.insert(i, chr(h+55))
            m = 1
            h = 0
            chk = 1
            i = i+1
        else:
            m = m*2
            chk = chk+1
        bnum = int(bnum/10)

    if chk!=1:
        hnum.insert(i, chr(h+48))
    if chk==1:
        i = i-1

    #("\nEquivalent Hexadecimal Value = ", end="")
    while i>=0:
        #print(end=hnum[i])
        i = i-1
        #print(hnum[i])
    #print()
    #(hnum)
   
    hnum.reverse()
    #(hnum)
    juntarr=''.join(hnum)
    #(juntarr, type(juntarr))
    return juntarr



################################################################################
# m  u   l   t       p   o   l   i   n   o   m   i   o   s
################################################################################

def multiplicar_polinomios(lista1, lista2):
    if lista1==[0,0,0,0,0,0,0,1]:
        #print("Se multiplicara por 1")
        return lista2

    if lista1==[0,0,0,0,0,0,1,0]:
        #print("Se multiplicara por 2")
        #print((lista2))
        lista2.append(0)
        
        #print(len(lista2))
        #print((lista2))
        #print((lista2[0]))
        if len(lista2)==9 and lista2[0]==1:
            lista2.pop(0)
            x8=[0,0,0,1,1,0,1,1]
            #print(len(x8))
            #print((x8))
            resultado=[]
            #print("----")
            #print((x8))
            #print((lista2))
            for i in range(0, len(lista2)):
                if lista2[i]==x8[i]:###############################
                    resultado.append(0)
                else:
                    resultado.append(1)

            
            return resultado
        else:
            if len(lista2)==9 and lista2[0]==0:
                lista2.pop(0)
            return lista2

    if lista1==[0,0,0,0,0,0,1,1]:
        #print("Se multiplicara por 3")
        temporal=[]
        for i in lista2:
            temporal.append(i)
        #lista2.pop(0)
        lista2.append(0)
        #print(temporal)
        #print(lista2)
        
        ####son 8 bits, al subir de nuvel 1 se generan 9 y se borra el primero
        if len(lista2)==9 and lista2[0]==0:
            lista2.pop(0)
            resultado=[]
            #print("-----------")
            #print(temporal)
            #print(lista2)
            for i in range(0, len(lista2)):
                if lista2[i]==temporal[i]:
                    resultado.append(0)
                else:
                    resultado.append(1)
            #print(resultado)
            return resultado



        ##if es 9 significa que hay z8
        if len(lista2)==9 and lista2[0]==1:
            lista2.pop(0)
            x8=[0,0,0,1,1,0,1,1]    
            resultado=[]
            #print("---")
            #print(x8)
            #print(lista2)
            #print(temporal)
            for i in range(0, len(lista2)):
                if (x8[i]==lista2[i]):###############################
                    resultado.append(0)
                else:
                    resultado.append(1)
            #print("x8 con la primera", x8)
            #print("lista2", lista2)
            #print("resultado1", resultado)
            #print("temporal", temporal)
            #print("---")

            resultado2=[]

            for i in range(0, len(lista2)):
                if (resultado[i]==temporal[i]):###############################
                    resultado2.append(0)
                else:
                    resultado2.append(1)
            #print("---")
            #print("resultado 2", resultado2)
            #print("---")
            return resultado2

def de_string_int(lista_s):
    lista=[]
    for i in lista_s:
        if i=='0':
            lista.append(0)
        else:
            lista.append(1)
    return lista

def conversor_hexadecimal_a_binario(hexadecimal):
    lista_hex=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    binario=[]
    for i in hexadecimal:
        if i in lista_hex:
            indice=lista_hex.index(i)
            num_binar=(bin(indice).lstrip("0b"))
            longi=(abs(len(num_binar)-4))
            n='0'*longi
            n_cadena=n + num_binar
            binario.append(n_cadena)
    binario_final=str(("").join(binario))
    #("Numero en binario:",binario_final)
    #(len(binario_final))
    #pasando a una lista
    lista=list(binario_final)
    #(lista)
    if len(lista)<8:
        #("Completando con ceros a la izquierda")
        numero_de_ceros=8-len(lista)
        ceros=[]
        for i in range(0,numero_de_ceros):
            ceros.append('0')
        lista= ceros+lista
    lista1=de_string_int(lista)
    return lista1


def funcion_xor(lista1,lista2):
    resultado=[]
    for i in range(0,8):
        if ((lista1[i]==0 and lista2[i]==0) or (lista1[i]==1 and lista2[i]==1)):
            resultado.append(0)
        else:
            resultado.append(1)
    return resultado



################################################################################
#  M    i   x               c   o   l   u  m    n   s
################################################################################

def mix_column(m_ejemplo):
    m_f=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m_definida=[['02','03' ,'01' ,'01'],['01' ,'02' ,'03' ,'01'],[ '01', '01', '02','03'],[ '03', '01', '01','02']]
    for fila in range(4):

        for columna in range(4):

             #("Para todos los renglones con primera columna columna 0")
            if columna==0:
                #("----------Para la columna 0---------")
                a=m_ejemplo[0][0]
                b=m_ejemplo[1][0]
                c=m_ejemplo[2][0]
                d=m_ejemplo[3][0]

                if fila==0:
                    #("Primer renglon columna 0")
                    #print(m_definida[0][0],a)
                    b1=conversor_hexadecimal_a_binario(m_definida[0][0])
                    b2=conversor_hexadecimal_a_binario(a)
                    mult_polinoms1=multiplicar_polinomios(b1, b2)

                    b11=conversor_hexadecimal_a_binario(m_definida[0][1])
                    b22=conversor_hexadecimal_a_binario(b)
                    mult_polinoms11=multiplicar_polinomios(b11, b22)
                   
                    b111=conversor_hexadecimal_a_binario(m_definida[0][2])
                    b222=conversor_hexadecimal_a_binario(c)
                    mult_polinoms111=multiplicar_polinomios(b111, b222)

                    b1111=conversor_hexadecimal_a_binario(m_definida[0][3])
                    b2222=conversor_hexadecimal_a_binario(d)
                    mult_polinoms1111=multiplicar_polinomios(b1111, b2222)

                    list_xor=funcion_xor(mult_polinoms1,mult_polinoms11)
                    list_xor2=funcion_xor(mult_polinoms111,mult_polinoms1111)
                    list_xor3=funcion_xor(list_xor,list_xor2)
                    n_list_xor3=[]
                    for i in range(0,8):
                        if list_xor3[i]==1:
                            n_list_xor3.append('1')
                        else:
                            n_list_xor3.append('0')
                    

                    s00=list_xor3
             

                if fila==1:
                    #("segundo renglon columna 0")
                    #(m_definida[1][0],a)
                    a1=conversor_hexadecimal_a_binario(m_definida[1][0])
                    a2=conversor_hexadecimal_a_binario(a)
                    mult_p=multiplicar_polinomios(a1, a2)

                    #(m_definida[1][1],b)
                    a11=conversor_hexadecimal_a_binario(m_definida[1][1])
                    a22=conversor_hexadecimal_a_binario(b)
                    mult_p1=multiplicar_polinomios(a11, a22)

                    #(m_definida[1][2],c)
                    a111=conversor_hexadecimal_a_binario(m_definida[1][2])
                    a222=conversor_hexadecimal_a_binario(c)
                    mult_p2=multiplicar_polinomios(a111, a222)

                    #(m_definida[1][3],d)
                    a1111=conversor_hexadecimal_a_binario(m_definida[1][3])
                    a2222=conversor_hexadecimal_a_binario(d)
                    mult_p3=multiplicar_polinomios(a1111, a2222)

                    list_1=funcion_xor(mult_p,mult_p1)
                    list_11=funcion_xor(mult_p2,mult_p3)
                    list_111=funcion_xor(list_1,list_11)

                    s01=list_111
                 
                if fila==2:
                    #("tercer renglon columna 0")
                    #(m_definida[2][0],a)
                    q1=conversor_hexadecimal_a_binario(m_definida[2][0])
                    q2=conversor_hexadecimal_a_binario(a)
                    mult_q=multiplicar_polinomios(q1, q2)

                    #(m_definida[2][1],b)
                    q11=conversor_hexadecimal_a_binario(m_definida[2][1])
                    q22=conversor_hexadecimal_a_binario(b)
                    mult_qq=multiplicar_polinomios(q11, q22)

                    #(m_definida[2][2],c)
                    q111=conversor_hexadecimal_a_binario(m_definida[2][2])
                    q222=conversor_hexadecimal_a_binario(c)
                    mult_qqq=multiplicar_polinomios(q111, q222)

                    #(m_definida[2][3],d)
                    q1111=conversor_hexadecimal_a_binario(m_definida[2][3])
                    q2222=conversor_hexadecimal_a_binario(d)
                    mult_qqqq=multiplicar_polinomios(q1111, q2222)


                    qa1=funcion_xor(mult_q,mult_qq)
                    qa2=funcion_xor(mult_qqq,mult_qqqq)
                    qa3=funcion_xor(qa1,qa2)
                    
                    s02=qa3
                  

                if fila==3:
                    #("cuarto renglon columna 0")
                    #(m_definida[3][0],a)
                    pu1=conversor_hexadecimal_a_binario(m_definida[3][0])
                    pu2=conversor_hexadecimal_a_binario(a)
                    pu_q=multiplicar_polinomios(pu1, pu2)

                    #(m_definida[3][1],b)
                    pu11=conversor_hexadecimal_a_binario(m_definida[3][1])
                    pu22=conversor_hexadecimal_a_binario(b)
                    pu_qq=multiplicar_polinomios(pu11, pu22)

                    #(m_definida[3][2],c)
                    pu111=conversor_hexadecimal_a_binario(m_definida[3][2])
                    pu222=conversor_hexadecimal_a_binario(c)
                    pu_qqq=multiplicar_polinomios(pu111, pu222)

                    #(m_definida[3][3],d)
                    pu1111=conversor_hexadecimal_a_binario(m_definida[3][3])
                    pu2222=conversor_hexadecimal_a_binario(d)
                    pu_qqqq=multiplicar_polinomios(pu1111, pu2222)

                    pua=funcion_xor(pu_q,pu_qq)
                    puaa=funcion_xor(pu_qqq,pu_qqqq)
                    puaaa=funcion_xor(pua,puaa)

                    s03=puaaa
                    


             #print("Para todos los renglones con columna 1")
            if columna==1:
                #("----------Para la columna 1---------")
                aa=m_ejemplo[0][1]
                bb=m_ejemplo[1][1]
                cc=m_ejemplo[2][1]
                dd=m_ejemplo[3][1]
                if fila==0:
                    #("Primer renglon columna 1")
                    #(m_definida[0][0],aa)
                    jr1=conversor_hexadecimal_a_binario(m_definida[0][0])
                    kp1=conversor_hexadecimal_a_binario(aa)
                    j_k=multiplicar_polinomios(jr1, kp1)

                    #(m_definida[0][1],bb)
                    jr11=conversor_hexadecimal_a_binario(m_definida[0][1])
                    kp11=conversor_hexadecimal_a_binario(bb)
                    j_k1=multiplicar_polinomios(jr11, kp11)

                    #(m_definida[0][2],cc)
                    jr111=conversor_hexadecimal_a_binario(m_definida[0][2])
                    kp111=conversor_hexadecimal_a_binario(cc)
                    j_k11=multiplicar_polinomios(jr111, kp111)

                    #(m_definida[0][3],dd)
                    jr1111=conversor_hexadecimal_a_binario(m_definida[0][3])
                    kp1111=conversor_hexadecimal_a_binario(dd)
                    j_k111=multiplicar_polinomios(jr1111, kp1111)

                    j_xor=funcion_xor(j_k,j_k1)
                    j_xor2=funcion_xor(j_k11,j_k111)
                    j_xor3=funcion_xor(j_xor,j_xor2)

                    s10=j_xor3
                    
    
                if fila==1:
                    #("segundo renglon columna 1")
                    #(m_definida[1][0],aa)
                    src1=conversor_hexadecimal_a_binario(m_definida[1][0])
                    src2=conversor_hexadecimal_a_binario(aa)
                    src_p=multiplicar_polinomios(src1, src2)

                    #(m_definida[1][1],bb)
                    src11=conversor_hexadecimal_a_binario(m_definida[1][1])
                    src22=conversor_hexadecimal_a_binario(bb)
                    src_pp=multiplicar_polinomios(src11,src22 )

                    #(m_definida[1][2],cc)
                    src111=conversor_hexadecimal_a_binario(m_definida[1][2])
                    src222=conversor_hexadecimal_a_binario(cc)
                    src_ppp=multiplicar_polinomios(src111,src222 )
                

                    #(m_definida[1][3],dd)
                    src1111=conversor_hexadecimal_a_binario(m_definida[1][3])
                    src2222=conversor_hexadecimal_a_binario(dd)
                    src_pppp=multiplicar_polinomios(src1111,src2222 )

                    src_xor=funcion_xor(src_p,src_pp)
               
                    src_xor2=funcion_xor(src_ppp,src_pppp)
                   
                    src_xor3=funcion_xor(src_xor,src_xor2)
                    s11=src_xor3
                    
            

                if fila==2:
                    #("tercer renglon columna 1")
                    #(m_definida[2][0],aa)
                    sk1=conversor_hexadecimal_a_binario(m_definida[2][0])
                    sk2=conversor_hexadecimal_a_binario(aa)
                    sk_p=multiplicar_polinomios(sk1, sk2)

                
                    #(m_definida[2][1],bb)
                
                    sk11=conversor_hexadecimal_a_binario(m_definida[2][1])
                    sk22=conversor_hexadecimal_a_binario(bb)
                    sk_pp=multiplicar_polinomios(sk11, sk22)

                    #(m_definida[2][2],cc)
                    sk111=conversor_hexadecimal_a_binario(m_definida[2][2])
                    sk222=conversor_hexadecimal_a_binario(cc)
                    sk_ppp=multiplicar_polinomios(sk111, sk222)

                    #(m_definida[2][3],dd)
                    sk1111=conversor_hexadecimal_a_binario(m_definida[2][3])
                    sk2222=conversor_hexadecimal_a_binario(dd)
                    sk_pppp=multiplicar_polinomios(sk1111, sk2222)

                    sk_xor=funcion_xor(sk_p,sk_pp)
                    sk_xor2=funcion_xor(sk_ppp,sk_pppp)
                    sk_xor3=funcion_xor(sk_xor,sk_xor2)
                    s12=sk_xor3

                if fila==3:
                    #("cuarto renglon columna 1")
                    #(m_definida[3][0],aa)
                    sw1=conversor_hexadecimal_a_binario(m_definida[3][0])
                    sw2=conversor_hexadecimal_a_binario(aa)
                    sw_p=multiplicar_polinomios(sw1, sw2)

                    #(m_definida[3][1],bb)
            
                    sw11=conversor_hexadecimal_a_binario(m_definida[3][1])
                    sw22=conversor_hexadecimal_a_binario(bb)
                    sw_pp=multiplicar_polinomios(sw11, sw22)

                    #(m_definida[3][2],cc)

                    sw111=conversor_hexadecimal_a_binario(m_definida[3][2])
                    sw222=conversor_hexadecimal_a_binario(cc)
                    sw_ppp=multiplicar_polinomios(sw111, sw222)

                    #(m_definida[3][3],dd)
            
                    sw1111=conversor_hexadecimal_a_binario(m_definida[3][3])
                    sw2222=conversor_hexadecimal_a_binario(dd)
                    sw_pppp=multiplicar_polinomios(sw1111, sw2222)

                    sw_xor=funcion_xor(sw_p,sw_pp)
                    sw_xor2=funcion_xor(sw_ppp,sw_pppp)
                    sw_xor3=funcion_xor(sw_xor,sw_xor2)
                    s13=sw_xor3


             #("Para todos los renglones con  columna 2")
            if columna==2:
                #("----------Para la columna 2---------")
                aaa=m_ejemplo[0][2]
                bbb=m_ejemplo[1][2]
                ccc=m_ejemplo[2][2]
                ddd=m_ejemplo[3][2]
                if fila==0:
                    #("Primer renglon columna 2")
                    #(m_definida[0][0],aaa)

                    pc1=conversor_hexadecimal_a_binario(m_definida[0][0])
                    pc2=conversor_hexadecimal_a_binario(aaa)
                    pc_p=multiplicar_polinomios(pc1, pc2)

                    #(m_definida[0][1],bbb)
                    pc11=conversor_hexadecimal_a_binario(m_definida[0][1])
                    pc22=conversor_hexadecimal_a_binario(bbb)
                    pc_pp=multiplicar_polinomios(pc11, pc22)

                    #(m_definida[0][2],ccc)
                    pc111=conversor_hexadecimal_a_binario(m_definida[0][2])
                    pc222=conversor_hexadecimal_a_binario(ccc)
                    pc_ppp=multiplicar_polinomios(pc111, pc222)

                    #(m_definida[0][3],ddd)
                    pc1111=conversor_hexadecimal_a_binario(m_definida[0][3])
                    pc2222=conversor_hexadecimal_a_binario(ddd)
                    pc_pppp=multiplicar_polinomios(pc1111, pc2222)
                
                    pc_xor=funcion_xor(pc_p,pc_pp)
                    pc_xor2=funcion_xor(pc_ppp,pc_pppp)
                    pc_xor3=funcion_xor(pc_xor,pc_xor2)
                    s20=pc_xor3

                if fila==1:
                    #("segundo renglon columna 2")
                    #(m_definida[1][0],aaa)
                    pcw1=conversor_hexadecimal_a_binario(m_definida[1][0])
                    pcw2=conversor_hexadecimal_a_binario(aaa)
                    pcw_p=multiplicar_polinomios(pcw1, pcw2)

                    #(m_definida[1][1],bbb)
                    pcw11=conversor_hexadecimal_a_binario(m_definida[1][1])
                    pcw22=conversor_hexadecimal_a_binario(bbb)
                    pcw_pp=multiplicar_polinomios(pcw11, pcw22)
        
                    #(m_definida[1][2],ccc)
                    pcw111=conversor_hexadecimal_a_binario(m_definida[1][2])
                    pcw222=conversor_hexadecimal_a_binario(ccc)
                    pcw_ppp=multiplicar_polinomios(pcw111, pcw222)

                    #(m_definida[1][3],ddd)
                    pcw1111=conversor_hexadecimal_a_binario(m_definida[1][3])
                    pcw2222=conversor_hexadecimal_a_binario(ddd)
                    pcw_pppp=multiplicar_polinomios(pcw1111, pcw2222)

                    pcw_xor=funcion_xor(pcw_p,pcw_pp)
                    pcw_xor2=funcion_xor(pcw_ppp,pcw_pppp)
                    pcw_xor3=funcion_xor(pcw_xor,pcw_xor2)
                    s21=pcw_xor3


                if fila==2:
                    #("tercer renglon columna 2")
                    #(m_definida[2][0],aaa)
                    ppt1=conversor_hexadecimal_a_binario(m_definida[2][0])
                    ppt2=conversor_hexadecimal_a_binario(aaa)
                    ppt_p=multiplicar_polinomios(ppt1, ppt2)

                    #(m_definida[2][1],bbb)
                    ppt11=conversor_hexadecimal_a_binario(m_definida[2][1])
                    ppt22=conversor_hexadecimal_a_binario(bbb)
                    ppt_pp=multiplicar_polinomios(ppt11, ppt22)

                    #(m_definida[2][2],ccc)
                    ppt111=conversor_hexadecimal_a_binario(m_definida[2][2])
                    ppt222=conversor_hexadecimal_a_binario(ccc)
                    ppt_ppp=multiplicar_polinomios(ppt111, ppt222)

                    #(m_definida[2][3],ddd)
                    ppt1111=conversor_hexadecimal_a_binario(m_definida[2][3])
                    ppt2222=conversor_hexadecimal_a_binario(ddd)
                    ppt_pppp=multiplicar_polinomios(ppt1111, ppt2222)

                    ppt_xor=funcion_xor(ppt_p,ppt_pp)
                    ppt_xor2=funcion_xor(ppt_ppp,ppt_pppp)
                    ppt_xor3=funcion_xor(ppt_xor,ppt_xor2)
                    s22=ppt_xor3

                if fila==3:
                    #("cuarto renglon columna 2")
                    #(m_definida[3][0],aaa)
                    pz1=conversor_hexadecimal_a_binario(m_definida[3][0])
                    pz2=conversor_hexadecimal_a_binario(aaa)
                    pz_p=multiplicar_polinomios(pz1, pz2)

                    #(m_definida[3][1],bbb)
                    pz11=conversor_hexadecimal_a_binario(m_definida[3][1])
                    pz22=conversor_hexadecimal_a_binario(bbb)
                    pz_pp=multiplicar_polinomios(pz11, pz22)

                    #(m_definida[3][2],ccc)
                    pz111=conversor_hexadecimal_a_binario(m_definida[3][2])
                    pz222=conversor_hexadecimal_a_binario(ccc)
                    pz_ppp=multiplicar_polinomios(pz111, pz222)

                    #(m_definida[3][3],ddd)
                    pz1111=conversor_hexadecimal_a_binario(m_definida[3][3])
                    pz2222=conversor_hexadecimal_a_binario(ddd)
                    pz_pppp=multiplicar_polinomios(pz1111, pz2222)

                    pz_xor=funcion_xor(pz_p,pz_pp)
                    pz_xor2=funcion_xor(pz_ppp,pz_pppp)
                    pz_xor3=funcion_xor(pz_xor,pz_xor2)
                    s23=pz_xor3



             #("Para todos los renglones con  columna 3")
            if columna==3:
                #("----------Para la columna 3---------")
                aaaa=m_ejemplo[0][3]
                bbbb=m_ejemplo[1][3]
                cccc=m_ejemplo[2][3]
                dddd=m_ejemplo[3][3]
                if fila==0:
                    #("Primer renglon columna 3")
                    #(m_definida[0][0],aaaa)
                    pe1=conversor_hexadecimal_a_binario(m_definida[0][0])
                    pe2=conversor_hexadecimal_a_binario(aaaa)
                    pe_p=multiplicar_polinomios(pe1, pe2)

                    #(m_definida[0][1],bbbb)
                    pe11=conversor_hexadecimal_a_binario(m_definida[0][1])
                    pe22=conversor_hexadecimal_a_binario(bbbb)
                    pe_pp=multiplicar_polinomios(pe11, pe22)

                    #(m_definida[0][2],cccc)
                    pe111=conversor_hexadecimal_a_binario(m_definida[0][2])
                    pe222=conversor_hexadecimal_a_binario(cccc)
                    pe_ppp=multiplicar_polinomios(pe111, pe222)

                    #(m_definida[0][3],dddd)
                    pe1111=conversor_hexadecimal_a_binario(m_definida[0][3])
                    pe2222=conversor_hexadecimal_a_binario(dddd)
                    pe_pppp=multiplicar_polinomios(pe1111, pe2222)

                    pe_xor=funcion_xor(pe_p,pe_pp)
                    pe_xor2=funcion_xor(pe_ppp,pe_pppp)
                    pe_xor3=funcion_xor(pe_xor,pe_xor2)
                    s30=pe_xor3

                if fila==1:
                    #("segundo renglon columna 3")
                    #(m_definida[1][0],aaaa)
                    px1=conversor_hexadecimal_a_binario(m_definida[1][0])
                    px2=conversor_hexadecimal_a_binario(aaaa)
                    px_p=multiplicar_polinomios(px1, px2)

                    #(m_definida[1][1],bbbb)
                    px11=conversor_hexadecimal_a_binario(m_definida[1][1])
                    px22=conversor_hexadecimal_a_binario(bbbb)
                    px_pp=multiplicar_polinomios(px11, px22)

                    #(m_definida[1][2],cccc)
                    px111=conversor_hexadecimal_a_binario(m_definida[1][2])
                    px222=conversor_hexadecimal_a_binario(cccc)
                    px_ppp=multiplicar_polinomios(px111, px222)

                    #(m_definida[1][3],dddd)
                    px1111=conversor_hexadecimal_a_binario(m_definida[1][3])
                    px2222=conversor_hexadecimal_a_binario(dddd)
                    px_pppp=multiplicar_polinomios(px1111, px2222)


                    px_xor=funcion_xor(px_p,px_pp)
                    px_xor2=funcion_xor(px_ppp,px_pppp)
                    px_xor3=funcion_xor(px_xor,px_xor2)
                    s31=px_xor3



                if fila==2:
                    #("tercer renglon columna 3")
                    #(m_definida[2][0],aaaa)
                    pg1=conversor_hexadecimal_a_binario(m_definida[2][0])
                    pg2=conversor_hexadecimal_a_binario(aaaa)
                    pg_p=multiplicar_polinomios(pg1, pg2)

                    #(m_definida[2][1],bbbb)
                    pg11=conversor_hexadecimal_a_binario(m_definida[2][1])
                    pg22=conversor_hexadecimal_a_binario(bbbb)
                    pg_pp=multiplicar_polinomios(pg11, pg22)

                    #(m_definida[2][2],cccc)
                    pg111=conversor_hexadecimal_a_binario(m_definida[2][2])
                    pg222=conversor_hexadecimal_a_binario(cccc)
                    pg_ppp=multiplicar_polinomios(pg111, pg222)

                    #(m_definida[2][3],dddd)
                    pg1111=conversor_hexadecimal_a_binario(m_definida[2][3])
                    pg2222=conversor_hexadecimal_a_binario(dddd)
                    pg_pppp=multiplicar_polinomios(pg1111, pg2222)

                    pg_xor=funcion_xor(pg_p,pg_pp)
                    pg_xor2=funcion_xor(pg_ppp,pg_pppp)
                    pg_xor3=funcion_xor(pg_xor,pg_xor2)
                    s32=pg_xor3

                if fila==3:
                    #("cuarto renglon columna 3")
                    #(m_definida[3][0],aaaa)
                    phs1=conversor_hexadecimal_a_binario(m_definida[3][0])
                    phs2=conversor_hexadecimal_a_binario(aaaa)
                    phs_p=multiplicar_polinomios(phs1, phs2)

                    #(m_definida[3][1],bbbb)
                    phs11=conversor_hexadecimal_a_binario(m_definida[3][1])
                    phs22=conversor_hexadecimal_a_binario(bbbb)
                    phs_pp=multiplicar_polinomios(phs11, phs22)

                    #(m_definida[3][2],cccc)
                    phs111=conversor_hexadecimal_a_binario(m_definida[3][2])
                    phs222=conversor_hexadecimal_a_binario(cccc)
                    phs_ppp=multiplicar_polinomios(phs111, phs222)

                    #(m_definida[3][3],dddd)
                    phs1111=conversor_hexadecimal_a_binario(m_definida[3][3])
                    phs2222=conversor_hexadecimal_a_binario(dddd)
                    phs_pppp=multiplicar_polinomios(phs1111, phs2222)

                    phs_xor=funcion_xor(phs_p,phs_pp)
                    phs_xor2=funcion_xor(phs_ppp,phs_pppp)
                    phs_xor3=funcion_xor(phs_xor,phs_xor2)
                    s33=phs_xor3
            
    #("-----PRIMERa columna------")
    #("S00",s00)
    aux= str_int(s00)
    
    m_f[0][0]=aux
    
    #("S01",s01)
    aux= str_int(s01)
    m_f[1][0]=aux
    
    #("S02",s02)
    aux= str_int(s02)
    m_f[2][0]=aux

    #("S03",s03)
    aux= str_int(s03)
    m_f[3][0]=aux

    #("-----Segundo columna -------")
    #("S10",s10)
    aux= str_int(s10)
    m_f[0][1]=aux

    #("S11",s11)
    aux= str_int(s11)
    m_f[1][1]=aux

    #("S12",s12)
    aux= str_int(s12)
    m_f[2][1]=aux

    #("S13",s13)
    aux= str_int(s13)
    m_f[3][1]=aux

    #("-----Tercer columna -------")
    #("S20",s20)
    aux= str_int(s20)
    m_f[0][2]=aux

    #("S21",s21)
    aux= str_int(s21)
    m_f[1][2]=aux

    #("S22",s22)
    aux= str_int(s22)
    m_f[2][2]=aux

    #("S23",s23)
    aux= str_int(s23)
    m_f[3][2]=aux


    #("-----Cuarta columna -------")
    #("S30",s30)
    aux= str_int(s30)
    m_f[0][3]=aux

    #("S31",s31)
    aux= str_int(s31)
    m_f[1][3]=aux

    #("S32",s32)
    aux= str_int(s32)
    m_f[2][3]=aux

    #"S33",s33)
    aux= str_int(s33)
    m_f[3][3]=aux

    #aux= str_int(s33)
    #print("hexa",aux)

    # print("#### MATRIZ RESULTADO ####")
    # for i in m_f:
    #     print(i)

    return m_f
    

if __name__ == "__main__":
    ##para 1
    lista1=[0,0,0,0,0,0,0,1]
    lista2=[0,1,0,0,0,1,1,0]

    #para2
    # lista1=[0,0,0,0,0,0,1,0]
    # lista2=[1,1,1,1,0,0,1,0]

    #para 3
    # lista1=[0,0,0,0,0,0,1,1]
    # lista2=[0,1,0,0,1,1,0,0]

    # resultado=multiplicar_polinomios(lista1, lista2)
    # print(resultado)

    #Matriz ejemplo que llega de shift row
    m_ejemplo=[['87','F2' ,'4D' ,'97'],['6E' ,'4C' ,'90' ,'EC'],[ '46', 'E7', '4A','C3'],[ 'A6', '8C', 'D8','95']]
    mix_column(m_ejemplo)