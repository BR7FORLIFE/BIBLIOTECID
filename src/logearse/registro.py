import json
from src.assests.portada import *
def registro(): 
    clear_screen()
    title()
    while True:
        print("REGISTRO DE USUARIO ")
        print("USUARIO------------------------->")
        usuario = input("DIGITE UN NOMBRE PARA SU USUARIO: ")
        contraseña = input("DIGITE UNA CONTRASEÑA: ")
        diccionario_usuario = {"user: ": usuario,"password: ":contraseña}
        with open("data.json","w") as registro: 
            registro_usuario = json.dump(diccionario_usuario,registro,indent=4)
        print("Registro exitoso--------------------!")    
        break