from src.assests.portada import *
from src.interfaz.gestion_libros import gestion_libros
from src.logearse.registro import registro
from src.logearse.login import login

    
def main():    
    registro()
    login()
    while True: 
        gestion_libros()
        break
main()