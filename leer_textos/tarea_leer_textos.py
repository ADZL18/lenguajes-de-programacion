#leer el archivo txt y agregar a una lista de listas cada parametro 
file_ubication= 'c:/Users/user/Documents/python algoritmos/ejemplos de clase/leer_archivos/archivo.txt'
lista_de_listas= []

with open(file_ubication) as object:
    lines = object.readlines()
for i in lines:
    lista_de_listas.append(i.split())
#print(lista_de_listas)
print("la primera lista es:", lista_de_listas[0])
print("la ultima lista es:", lista_de_listas[2470])

