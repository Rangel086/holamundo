""""
    elementos del juego 
    0-personaje
    1-cajas
    2-metas
    3-paredes
    4-piso
    5-personaje metas
    6-caja meta 
"""
class Sokoban:
    PARED = 3
    PISO = 4
    PERSONAJE = 0
    CAJA = 1

    def __init__(self):
        # Define el mapa de juego
        self.mapa = [
            [self.PARED] * 10,
            [self.PARED] + [self.PISO] * 8 + [self.PARED],
            [self.PARED] + [self.PISO] * 8 + [self.PARED],
            [self.PARED] + [self.PISO] * 4 +  [self.CAJA] + [self.PISO] * 3  + [self.PARED],
            [self.PARED] + [self.PISO] * 4 + [self.PERSONAJE] + [self.PISO] * 3 + [self.PARED],
            [self.PARED] + [self.PISO] * 8 + [self.PARED],
            [self.PARED] + [self.PISO] * 8 + [self.PARED],
            [self.PARED] + [self.PISO] * 8 + [self.PARED],
            [self.PARED] + [self.PISO] * 8 + [self.PARED],
            [self.PARED] * 10
        ]

        # Definimos la posición inicial del personaje y de la caja
        self.personaje_columna = 5
        self.personaje_fila = 4
        self.caja_columna = 5
        self.caja_fila = 3

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def mover_derecha(self):
        if self.mapa[self.personaje_fila][self.personaje_columna + 1] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = self.PERSONAJE
            self.personaje_columna += 1
        elif self.mapa[self.personaje_fila][self.personaje_columna + 1] == self.CAJA and self.mapa[self.personaje_fila][self.personaje_columna + 2] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = self.PERSONAJE
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = self.CAJA
            self.personaje_columna += 1
            self.caja_columna += 1

    def mover_izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna - 1] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = self.PERSONAJE
            self.personaje_columna -= 1
        elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == self.CAJA and self.mapa[self.personaje_fila][self.personaje_columna - 2] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = self.PERSONAJE
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = self.CAJA
            self.personaje_columna -= 1
            self.caja_columna -= 1

    def mover_arriba(self):
        if self.mapa[self.personaje_fila - 1][self.personaje_columna] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = self.PERSONAJE
            self.personaje_fila -= 1
        elif self.mapa[self.personaje_fila - 1][self.personaje_columna] == self.CAJA and self.mapa[self.personaje_fila - 2][self.personaje_columna] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = self.PERSONAJE
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = self.CAJA
            self.personaje_fila -= 1
            self.caja_fila -= 1

    def mover_abajo(self):
        if self.mapa[self.personaje_fila + 1][self.personaje_columna] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = self.PERSONAJE
            self.personaje_fila += 1
        elif self.mapa[self.personaje_fila + 1][self.personaje_columna] == self.CAJA and self.mapa[self.personaje_fila + 2][self.personaje_columna] == self.PISO:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = self.PERSONAJE
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = self.CAJA
            self.personaje_fila += 1
            self.caja_fila += 1

    def jugar(self):
        while True:
            self.imprimirMapa()
            movimiento = input("Selecciona el movimiento (d: derecha, a: izquierda, w: arriba, s: abajo, exit: para salir del juego): ")
            if movimiento == 'd':
                self.mover_derecha()
            elif movimiento == 'a':
                self.mover_izquierda()
            elif movimiento == 'w':
                self.mover_arriba()
            elif movimiento == 's':
                self.mover_abajo()
            elif movimiento == 'exit':
                exit()

# Crea una instancia del juego y comienza a jugar
sokoban = Sokoban()
sokoban.jugar()
