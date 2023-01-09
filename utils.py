#import curses 

def input_amount(message,max_lenght): 
  
    x=input(message)[:max_lenght]
    return x


if __name__ == "__main__":
    mensaje_enviado = input_amount(message='Introduce el mensaje: ',max_lenght=16) 
    print("mensaje enviado:",mensaje_enviado)