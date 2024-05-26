import json


with open("datos.json","r") as catalogo: 
    mostrar = dict(json.load(catalogo))
    libro = int(input("digite el libro a buscar: "))
    for key in mostrar.items(): 
        print(mostrar[key]["libro"])