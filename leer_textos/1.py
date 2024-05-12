#leer el archivo txt y agregar a una lista de listas cada parametro los cuales estan divididos en 4 espacios
file_ubication= 'c:/Users/user/Documents/python algoritmos/ejemplos de clase/leer_archivos/archivo.txt'
a= []
b=[]
c=[]
with open(file_ubication) as object:
    lines = object.readlines()
for i in lines:
    g=i.split()
    fila_numeros = [float(valor) for valor in g]
    a.append(fila_numeros)
print(a[0][0])
print(len(a))

