import random  # importamos los modulos ramdom y json para elegir un token y guardarlo en json
import json

#todos los caracteres especiales para crear un token
letras = list("abcdefghijklmnopkrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numeros = list("1,2,3,4,5,6,7,8,9,0")
caracteres = list("@-,*!/")

# unimos las 3 listas y definimos una longitud de caracteres para el token
union = letras + numeros + caracteres
longitud_token = 16

# generamos un token aleatorio hasta el rango de la longitud
token = ''.join(random.choice(union) for _ in range(longitud_token))

#escribimos el token en un json para la hora de usarse
with open("token.txt","w") as archivo:
    archivo.writelines(token)





