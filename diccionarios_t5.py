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
diccionario= vars(ft)
print(diccionario)
print("------------------------------------------------------------------------")


#7 Escribe un programa en Python para eliminar duplicados del diccionario.
def eliminar_duplicados(diccionario):
    diccionario_sin_duplicados = {clave: valor for clave, valor in diccionario.items()}
    return diccionario_sin_duplicados

motos = {
    'Yamaha': 'MT-07', 'Honda': 'CBR600RR', 'Kawasaki': 'Ninja 300','Yamaha': 'YZF-R1','Honda': 'CBR1000RR', 'Suzuki': 'GSX-R750','Kawasaki': 'Ninja ZX-6R'}
nuevo_dicccionario= eliminar_duplicados(motos)
print(nuevo_dicccionario)
print("------------------------------------------------------------------------")


#8 Escribe un programa en Python para verificar si un diccionario está vacío o no.
def esta_vacio(diccionario):
    if len(diccionario)==0:
        return True
    else:
        return False
    #ejemplo
motocicletas = {
    'Yamaha': 'MT-07', 'Honda': 'CBR600RR', 'Kawasaki': 'Ninja 300','Yamaha': 'YZF-R1','Honda': 'CBR1000RR', 'Suzuki': 'GSX-R750',
    'Kawasaki': 'Ninja ZX-6R'}
carros= {}
print(esta_vacio(motocicletas))
print(esta_vacio(carros))
print("------------------------------------------------------------------------")


 #9 Escribe un programa en Python para extraer una lista de valores de una lista dada de diccionarios.
def extraer_valores(lista_diccionarios):
    lista_de_valores = [valor for diccionario in lista_diccionarios for valor in diccionario.values()]
    return lista_de_valores

Diccionario_original= [{'Matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]
print(extraer_valores(Diccionario_original))
print("------------------------------------------------------------------------")


#10 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Ciencias [92, 94, 88] 
def extaer_asigantura_ciencias(lista_de_diccionarios):
    asignatura_ciencias = [diccionario['ciencia'] for diccionario in lista_de_diccionarios if 'ciencia' in diccionario]
    return asignatura_ciencias

Diccionario_original= [{'Matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]
print(extaer_asigantura_ciencias(Diccionario_original))
print("------------------------------------------------------------------------")


#11 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Matemáticas [90, 89, 92]
def extaer_asigantura_matematicas(lista_de_diccionarios):
    asignatura_matematicas = [diccionario['Matematicas'] for diccionario in lista_de_diccionarios if 'Matematicas' in diccionario]
    return asignatura_matematicas

Diccionario_original= [{'Matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]
print(extaer_asigantura_matematicas(Diccionario_original))
print("------------------------------------------------------------------------")


#12 Escribe un programa en Python para encontrar la longitud de un diccionario de valores.
def longitud_diccionario(diccionario):
    longitud = len(diccionario.values())
    return longitud

edad = {"pedro": 20, "lorena": 18, "valeria": 19}
longitud = longitud_diccionario(edad)
print(longitud)
print("------------------------------------------------------------------------")


#13 Escribe un programa en Python para obtener la profundidad de un diccionario.
def profundidad_diccionario(diccionario):
    profundidades = [profundidad_diccionario(valor) for valor in diccionario.values() if isinstance(valor, dict)]
    return 1 + max(profundidades, default=0)

Diccionario_original= {'semestre1': {'Matematicas': 90, 'ciencia': 92}, 'semestre2': {'Matematicas': 89, 'ciencia': 94}, 'semestre3': {'Matematicas': 92, 'ciencia': 88}}
profundidad = profundidad_diccionario(Diccionario_original)
print(profundidad)
print("------------------------------------------------------------------------")