from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# uso de letras y números para ayudar al usuario
tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') * 2
state = {'mark': None}
hide = [True] * 64
taps = 0  # Variable para contar el número de taps


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8) 


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200  


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    taps += 1  # Incrementar el contador de taps
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image, tiles, and taps count."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64): 
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # ajustar posición de inicio del texto para centrarlo
        goto(x + 18, y + 8)  
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Mostrar el número de taps
    up()
    goto(-180, 180)
    color('black')
    write(f"Taps: {taps}", font=('Arial', 18, 'normal'))

    # Detectar si todos los cuadros se han destapado
    if all(not h for h in hide):
        goto(-180, -180)
        write("¡Juego terminado!", font=('Arial', 18, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles) # Mezclar las letras y números
setup(420, 420, 370, 0) # Configurar dimensiones de la ventana
addshape(car) # Agregar imagen del carro
hideturtle() # Hides the turtle cursor so it doesn't appear on the screen while drawing or moving
tracer(False) # Turn off animation to manually control screen updates (for faster drawing)
onscreenclick(tap) # Bind the screen click event to the tap function
draw() # Call the draw function to start the game
done()# Finish the game

