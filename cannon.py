from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Aumentar la velocidad del proyectil (más rápida)
        speed.x = (x + 200) / 15  # Reducir el divisor para mayor velocidad
        speed.y = (y + 200) / 15


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Aumentar la velocidad de los objetivos (más rápida)
        target.x -= 1  # Incrementar la velocidad de movimiento de los objetivos

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # Check if the target has not collided
        if abs(target - ball) > 13:
            # Reposition the target inside bounds (to loop)
            if not inside(target):
                target.x = 200
                target.y = randrange(-150, 150)
            # Add it to the target list
            targets.append(target)

    draw()

    """
    Delete so the game does not end
    for target in targets:
        if not inside(target):
            return
    """

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
