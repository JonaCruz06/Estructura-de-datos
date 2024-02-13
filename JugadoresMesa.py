import os
# Limpia la pantalla de la consola.
os.system('cls' if os.name == 'nt' else 'clear')
class JuegoMesa:
    def __init__(self, num_jugadores):
        # Inicializa la clase con el número de jugadores y crea una lista de nombres de jugadores.
        self.num_jugadores = num_jugadores
        # Se crea una lista de jugadores con nombres genéricos.
        self.jugadores = [f"Jugador {i + 1}" for i in range(num_jugadores)]
        # Inicializa el índice del turno actual en 0.
        self.turno_actual = 0

    def siguiente_turno(self):
        # Método para avanzar al siguiente turno en la cola circular.
        self.turno_actual = (self.turno_actual + 1) % self.num_jugadores
        # Devuelve el nombre del jugador que tiene el turno actualmente.
        return self.jugadores[self.turno_actual]

# Juego de mesa
# Crea una instancia de la clase JuegoMesa con 5 jugadores.
juego = JuegoMesa(5)

# Bucle que continúa hasta que el usuario escribe 'listo'.
while True:
    # Muestra un mensaje y espera a que el usuario presione Enter para avanzar al siguiente jugador o listo para salir del juego.
    input("Presiona Enter para avanzar al siguiente turno (o escribe 'listo' para salir): ")
    # Lee la entrada del usuario.
    if input().lower() == 'listo':
        # Si el usuario escribe 'listo', rompe el bucle y termina el juego.
        break
    turno_actual = juego.siguiente_turno()
    # Muestra el nombre del jugador que tiene el turno actualmente.
    print("Es el turno de {turno_actual}")

# Muestra el mensaje final cuando el juego ha terminado.
print("El juego ha terminado. ¡Listo para jugar!")
