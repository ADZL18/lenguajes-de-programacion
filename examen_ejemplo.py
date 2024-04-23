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
