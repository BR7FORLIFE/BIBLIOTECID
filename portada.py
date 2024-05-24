import os
import platform

def title(): 
    print("""
          
    |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
    | B | I | B | L | I | O | T | E | C | I | D |
    |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
          Sistema de Gestión de Biblioteca
    """)


def clear_screen():
     if os.name =="nt": 
         os.system("cls")
     else: 
         os.system("clear")    
    