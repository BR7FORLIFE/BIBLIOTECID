from portada import *
import time
import json

def login(): 
    time.sleep(2)
    clear_screen()
    title()
    print("INICIA SESION-----------------------------")
    print("USUARIO")
    usuario = input("----->: ")
    print("CONTRASEÑA")
    contraseña = input("----->:")
    diccionario_autenticacion = {"users": usuario,"password: ":contraseña}
    with open("data.json","r") as autenticar: 
        comprobar = json.load(autenticar)
        print(comprobar)
        if diccionario_autenticacion.values() == comprobar: 
            print("\nINICIANDO SESION!")
            time.sleep(2)
            clear_screen()
        else:
            print("no lo detecta")    
    
    