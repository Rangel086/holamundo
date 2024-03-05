"""
Elementos del juego
0-personaje
1-cajas
2-metas
3-paredes
4-piso
5-personaje metas
6-caja meta
"""

class Soko:

    mapa = []  # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de juego
        self.mapa = [
            [3, 3, 3, 3, 3],
            [3, 4, 4, 4, 3],
            [3, 4, 0, 4, 3],
            [3, 4, 4, 4, 3],
            [3, 3, 3, 3, 3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimir_mapa(self):
        for filas in self.mapa:
            print(filas)

    def movimiento1(self):
        # Donde estaba el persona pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        # Actualiza la posicion del personaje
        self.personaje_columna += 1

    def derecha(self):
        # Movimiento 1: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento1()

    def arriba(self):
        # Movimiento 2: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila - 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimiento2()

    def abajo(self):
        # Movimiento 3: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila + 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimiento3()

    def movimiento2(self):
        # Donde estaba el persona pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        # Actualiza la posicion del personaje
        self.personaje_fila -= 1

    def movimiento3(self):
        # Donde estaba el persona pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        # Actualiza la posicion del personaje
        self.personaje_fila += 1

    def jugar(self):
        while True:
            # Imprime el mapa
            self.imprimir_mapa()
            # Pide al usuario el movimiento
            movimiento
