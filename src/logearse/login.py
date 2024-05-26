from src.assests.portada import * # accedemos tanto como el tiulo como el limpiado de pantalla
import time
import json


def login(): 
    time.sleep(2)
    clear_screen()
    title()
    
    #interfaz
    print("INICIA SESION-----------------------------")
    print("USUARIO")
    usuario = input("----->: ")
    print("CONTRASEÑA")
    contraseña = input("----->:")
    
    #guardamos las variables en un dicionario
    diccionario_autenticacion = {"users": usuario,"password: ":contraseña}
    
    #abrimos el archivo donde se almacenara tanto el usuario como la contraseña y comprobamos si concuerdo con el registro
    # de usuario
    with open("data.json","r") as autenticar: 
        comprobar = json.load(autenticar).values()
        values = list(comprobar)
        values_autenticacion = list(diccionario_autenticacion.values())
        if values_autenticacion == values: 
            print("\nLOGEADO EXITOSAMENTE!")     
        else: 
            print("USUARIO O CONTRASEÑA SON INCORRECTOS!")
            
        time.sleep(2)        
        
        
    
    