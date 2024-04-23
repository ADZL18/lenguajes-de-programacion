# Paso 1: Crear el diccionario de jugadores
jugadores = {
    'Jugador1': {'goles': 5, 'asistencias': 3, 'amarillas': 1, 'rojas': 0, 'partidos': 10, 'estatura': 175, 'nacionalidad': 'Argentina'},
    'Jugador2': {'goles': 3, 'asistencias': 2, 'amarillas': 2, 'rojas': 0, 'partidos': 10, 'estatura': 180, 'nacionalidad': 'Brasil'},
    'Jugador3': {'goles': 7, 'asistencias': 1, 'amarillas': 0, 'rojas': 1, 'partidos': 10, 'estatura': 170, 'nacionalidad': 'Argentina'},
    'Jugador4': {'goles': 4, 'asistencias': 4, 'amarillas': 2, 'rojas': 0, 'partidos': 10, 'estatura': 185, 'nacionalidad': 'Argentina'},
    'Jugador5': {'goles': 2, 'asistencias': 6, 'amarillas': 1, 'rojas': 0, 'partidos': 10, 'estatura': 178, 'nacionalidad': 'Brasil'},
    'Jugador6': {'goles': 6, 'asistencias': 2, 'amarillas': 0, 'rojas': 0, 'partidos': 10, 'estatura': 182, 'nacionalidad': 'Argentina'},
    'Jugador7': {'goles': 1, 'asistencias': 5, 'amarillas': 0, 'rojas': 0, 'partidos': 10, 'estatura': 177, 'nacionalidad': 'Brasil'},
    'Jugador8': {'goles': 3, 'asistencias': 3, 'amarillas': 1, 'rojas': 1, 'partidos': 10, 'estatura': 179, 'nacionalidad': 'Argentina'},
    'Jugador9': {'goles': 5, 'asistencias': 2, 'amarillas': 0, 'rojas': 0, 'partidos': 10, 'estatura': 181, 'nacionalidad': 'Brasil'},
    'Jugador10': {'goles': 2, 'asistencias': 4, 'amarillas': 1, 'rojas': 0, 'partidos': 10, 'estatura': 176, 'nacionalidad': 'Argentina'}
}

# Paso 2a: Imprimir jugadores solo por una nacionalidad
nacionalidad_deseada = 'Argentina'
print("Jugadores de la nacionalidad", nacionalidad_deseada)
for jugador, info in jugadores.items():
    if info['nacionalidad'] == nacionalidad_deseada:
        print(jugador)

# Paso 2b: Imprimir jugadores en orden alfabético
print("\nJugadores en orden alfabético:")
for jugador in sorted(jugadores.keys()):
    print(jugador)

# Paso 2c: Ordenar jugadores por la suma de asistencias y goles
print("\nJugadores ordenados por la suma de asistencias y goles:")
for jugador, info in sorted(jugadores.items(), key=lambda x: x[1]['asistencias'] + x[1]['goles'], reverse=True):
    print(jugador)
    
    
# Paso 1: Definir el diccionario de productos
productos = {
    1: {'nombre': 'Leche', 'cantidad': 20, 'precio': 2.5},
    2: {'nombre': 'Pan', 'cantidad': 30, 'precio': 1.5},
    3: {'nombre': 'Huevos', 'cantidad': 40, 'precio': 3.0},
    4: {'nombre': 'Cereal', 'cantidad': 15, 'precio': 4.0},
    5: {'nombre': 'Jugo', 'cantidad': 25, 'precio': 2.0},
    # Agrega más productos aquí
}

# Paso 2: Permitir al usuario seleccionar 3 productos para comprar
productos_comprados = []
for i in range(3):
    print("Productos disponibles:")
    for id_producto, producto in productos.items():
        print(f"ID: {id_producto}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad en almacén: {producto['cantidad']}")
    seleccion = int(input("Selecciona el ID del producto que deseas comprar: "))
    productos_comprados.append(productos[seleccion])

# Paso 3: Calcular el total a pagar
total_pagar = sum(producto['precio'] for producto in productos_comprados)
print("Total a pagar:", total_pagar)

# Paso 4: Preguntar al usuario si acepta la compra y si desea actualizar el inventario
confirmacion = input("¿Deseas comprar estos productos? (Sí/No): ")
if confirmacion.lower() == 'sí':
    for producto in productos_comprados:
        producto_id = next(key for key, value in productos.items() if value == producto)
        productos[producto_id]['cantidad'] -= 1
    print("¡Compra realizada! El inventario ha sido actualizado.")
else:
    print("Compra cancelada. El inventario no será actualizado.")



# Paso 1: Crear la lista de diccionarios de autos
autos = [
    {'marca': 'Toyota', 'motor': 'V6', 'num_ejes': 2, 'id': 1, 'modelo': 'Corolla', 'transmision': 'manual'},
    {'marca': 'Honda', 'motor': 'V4', 'num_ejes': 2, 'id': 2, 'modelo': 'Civic', 'transmision': 'manual'},
    {'marca': 'Ford', 'motor': 'V8', 'num_ejes': 2, 'id': 3, 'modelo': 'Mustang', 'transmision': 'manual'},
    {'marca': 'Chevrolet', 'motor': 'V6', 'num_ejes': 2, 'id': 4, 'modelo': 'Camaro', 'transmision': 'manual'},
    {'marca': 'Nissan', 'motor': 'V6', 'num_ejes': 2, 'id': 5, 'modelo': 'Altima', 'transmision': 'manual'}
]

# Paso 2: Permitir al usuario seleccionar un auto por su modelo para comprar
print("Autos disponibles para comprar:")
for auto in autos:
    print(f"ID: {auto['id']}, Marca: {auto['marca']}, Modelo: {auto['modelo']}")

modelo_seleccionado = input("Selecciona el modelo del auto que deseas comprar: ")

# Eliminar el auto seleccionado de la lista
auto_comprado = None
for auto in autos:
    if auto['modelo'].lower() == modelo_seleccionado.lower():
        auto_comprado = auto
        autos.remove(auto)
        break

if auto_comprado:
    print(f"Has comprado el {auto_comprado['marca']} {auto_comprado['modelo']}.")
else:
    print("No se encontró ningún auto con ese modelo.")

# Paso 3: Mostrar la lista de autos actualizada
print("Lista de autos actualizada después de la compra:")
for auto in autos:
    print(auto)

# Paso 4: Preguntar al usuario si desea actualizar el tipo de transmisión del auto comprado
if auto_comprado:
    nueva_transmision = input("¿Deseas actualizar la transmisión del auto a automática? (Sí/No): ")
    if nueva_transmision.lower() == 'sí':
        auto_comprado['transmision'] = 'automática'
        print(f"La transmisión del {auto_comprado['marca']} {auto_comprado['modelo']} ha sido actualizada a automática.")
    else:
        print("No se realizaron cambios en la transmisión del auto.")
