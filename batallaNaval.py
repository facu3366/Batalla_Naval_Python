from biblioteca import *

## Ejercicio 1
def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """
    Devuelve la cantidad de barcos de un tamaño dado.
    """
    contador: int = 0
    for barco in barcos:
        if len(barco) == tamaño:
            contador = contador + 1
    return contador


## Ejercicio 2
def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """
    Crea un nuevo estado de juego vacío.
    """
    dimensiones: Dimensiones = (cantidadDeFilas, cantidadDeColumnas)
    tableroUNO: Tablero = nuevoTablero(cantidadDeFilas, cantidadDeColumnas)
    tableroDOS: Tablero = nuevoTablero(cantidadDeFilas, cantidadDeColumnas)
    return (dimensiones, barcosDisponibles, [UNO], tableroUNO, tableroDOS)


def nuevoTablero(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:
    grilla_local: Grilla = grillaVacía(cantidadDeFilas, cantidadDeColumnas)
    grilla_oponente: Grilla = grillaVacía(cantidadDeFilas, cantidadDeColumnas)
    return (grilla_local, grilla_oponente)


def grillaVacía(cantidadDeFilas: int, cantidadDeColumnas: int) -> Grilla:
    grilla: Grilla = []
    for i in range(cantidadDeFilas):
        fila: list[Celda] = []
        for j in range(cantidadDeColumnas):
            fila.append(VACÍO)
        grilla.append(fila)
    return grilla


def esGrillaVacía(grilla: Grilla) -> bool:
    for fila in grilla:
        for celda in fila:
            if celda != VACÍO:
                return False
    return True
