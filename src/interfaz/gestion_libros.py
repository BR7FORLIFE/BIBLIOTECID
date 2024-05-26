from  src.assests.portada import * #importamos la ruta donde se encuentra el titulo y el limpiado de pantalla
import json # importamos para manejar archivos json
from src.assests.autenticacion_master import * #importamos la ruta para acceder al token generado
import time #importamos time para el sleep o la espera
  
# definimos una funcion el cual verificaremos el token generado para el autor del proyecto
def gestion_libros():
    while True:  
        clear_screen() # limpiamos pantalla
        title() # llamamos al titulo
    
        # abrimos el json el cual tenemos el login del usuario tanto el usuario como la contraseña
        with open("data.json","r") as usuario:
            usuario = json.load(usuario)
            user = list(usuario.values())
        print(f"""
            -----------------------------
            | GESTION DE LIBROS (CATALOGO)|
             -----------------------------
                      
             BIENVENIDO | {user[0]} |
             
            1. CONTINUAR COMO USUARIO
            2. CONTINUAR COMO DESARROLLADOR
            3. SALIR            
            """)
    
        opcion = int(input("Digite una opcion de las presentes: "))
        if opcion == 1: 
            #mostramos los catalogos de libros definidos en catalogos .json
            clear_screen()
            title()
            print("CATALOGOS DE LIBROS------->")
            with open("catalogo.json","r") as catalogo: 
                mostrar = dict(json.load(catalogo))
                for key in mostrar: 
                    print(mostrar[key]["titulo"])
                # BUSCAMOS EN EL JSON EL LIBRO SEGUN LA ELECCION DEL USUARIO
                escoger_libro = int(input("DIGITE EL LIBRO EL CUAL QUIERE SABER MAS INFORMACION: "))
                
                
            
            break
        elif opcion == 2:
            #defimos una variable el cual comprobara si el token generado corresponde con el que digite el usuario
            # si es asi es porque es el creador de la app caso contrario no tendra acceso a funcionalidades
            permiso = input("DIGITE SU TOKEN PARA TENER ACCESO DE MODIFICACION: ")
    
            # comprobamos el token con lo digitado en la variable
            if permiso == token:
                print("ACCESO CONSEDIDO!")
                time.sleep(3)
                clear_screen()
                title()
            else:
                 print("EL TOKEN ES INCORECTO!")
            break
        else: 
            break     
    
        
            
    
    
    
    
    


   


    
    
    