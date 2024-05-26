import os
import platform  #importamos las librerias necesarias para el limpiado de pantalla


# definimos un titulo
def title(): 
    print("""
          
    |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
    | B | I | B | L | I | O | T | E | C | I | D |
    |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
          Sistema de Gestión de Biblioteca
    """)

# creamos la funcion de limpiado de pantalla esperando a ser llamada 
def clear_screen():
     if os.name =="nt": 
         os.system("cls")
     else: 
         os.system("clear")    
    