#1 Escribe un programa en Python para multiplicar todos los elementos de un diccionario.
def multiplicar_dicc(diccionario):
    contador=1
    for i in diccionario.values():
        contador*=i
    return contador

edad = {
    "pedro": 20, "lorena": 18, "valeria": 19 }
print(multiplicar_dicc(edad))
print("------------------------------------------------------------------------")


#2 Escribe un programa en Python para eliminar una clave de un diccionario.
def eliminar_key(diccionario, key):
    del diccionario[key]
    return diccionario

edad = {
    "pedro": 20, "lorena": 18, "valeria": 19 }
eliminar_key(edad,"pedro")
print(edad)
print("------------------------------------------------------------------------")


#3 Escribe un programa en Python para convertir dos listas en un diccionario.
def diccionario(a,b):
    diccionario = {}
    for i in range(len(a)):
        diccionario[a[i]] = b[i]
    return diccionario

ropa = ["camisa", "calcetines", "short", "zapatos", "ropa interior"]
colores = ["rojo", "azul", "verde", "amarillo", "morado"]
print(diccionario(ropa, colores))
print("------------------------------------------------------------------------")


#4 Escribe un programa en Python para ordenar un diccionario dado por clave.
def ordenar_diccionario(diccionario):
    a= sorted(diccionario)
    return a
edad = {
    "lorena": 18, "valeria": 19, "pedro": 20, "angel": 12} 
diccionario_ordenado= ordenar_diccionario(edad)
print(diccionario_ordenado)
print("------------------------------------------------------------------------")


#5 Escribe un programa en Python para obtener los valores máximo y mínimo de un diccionario.
def valor_minimo(diccionario):
    a=[]
    for i in diccionario.values():
        a.append(i)
    b=min(a)
    return b
def valor_max(diccionario):
    a=[]
    for i in diccionario.values():
        a.append(i)
    b=max(a)
    return b
edad = {
    "lorena": 18, "valeria": 19, "pedro": 20, "angel": 12} 
print("el valor maximo del diccionario es:", valor_minimo(edad),"el valor minimo del diccionario es:",valor_max(edad))
print("------------------------------------------------------------------------")


#6 Escribe un programa en Python para obtener un diccionario a partir de los campos de un objeto.
class Moto:
    def __init__ (self, marca, modelo, motor, precio):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.precio = precio   
ft= Moto("italika", "ft150", "150cc", "21000")
diccionario_ft= ft.__dict__
print(diccionario_ft)
print("------------------------------------------------------------------------")


#7 Escribe un programa en Python para eliminar duplicados del diccionario.
def eliminar_llaves_duplicadas(diccionario):
   sin_llaves_duplicadas= set(diccionario.key())
   diccionario_sin_llaves_duplicadas = {key: diccionario[key] for key in sin_llaves_duplicadas}
   return diccionario_sin_llaves_duplicadas
motos = {
    'Yamaha': 'MT-07', 'Honda': 'CBR600RR', 'Kawasaki': 'Ninja 300','Yamaha': 'YZF-R1','Honda': 'CBR1000RR', 'Suzuki': 'GSX-R750','Kawasaki': 'Ninja ZX-6R'}
nuevo_dicccionario= eliminar_llaves_duplicadas(motos)
print(nuevo_dicccionario)