import curses 

def input_amount(message,max_lenght): 
    try: 
        stdscr = curses.initscr() 
        stdscr.clear() 
        stdscr.addstr(message) 
        amt = stdscr.getstr(1,0,max_lenght) # or use getkey() as showed above.
    except: 
        raise 
    finally: 
        curses.endwin() # to restore the terminal to its original operating mode.
    return amt.decode()


if __name__ == "__main__":
    mensaje_enviado = input_amount(message='Introduce el mensaje: ',max_lenght=16) 
    print("mensaje enviado:",mensaje_enviado)