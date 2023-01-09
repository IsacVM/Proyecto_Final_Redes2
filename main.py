from cifrado.cifrado import cifrar
from utils import input_amount 


usr_msg= input_amount(message="Ingresa mensaje: ",max_lenght=16)
data_cifrada=cifrar(usr_msg=usr_msg,clave='My_Add_Round_Key')
print("Matriz de Cifrado\n",data_cifrada)