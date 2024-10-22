"""Snake, classic arcade game.

Exercises:
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *
from freegames import square, vector

# Define food and snake's initial position
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)  # Direction of movement
colors = ['purple', 'blue', 'yellow', 'pink', 'orange']  # Color options

def change(x, y):
    """Change snake direction based on user input.

    Args:
        x (int): X-coordinate direction (horizontal).
        y (int): Y-coordinate direction (vertical).
    """
    aim.x = x
    aim.y = y

def inside(head):
    """Check if the snake's head is inside the game boundaries.

    Args:
        head (vector): Position of the snake's head.

    Returns:
        bool: True if the head is within the boundary, otherwise False.
    """
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food randomly in one of four directions, ensuring it stays inside the window."""
    directions = [(10, 0), (-10, 0), (0, 10), (0, -10)]  # Possible movement directions
    dx, dy = choice(directions)  # Randomly choose a direction

    # Update food's position
    food.x += dx
    food.y += dy

    # Check if food stays inside boundaries, if not, revert the movement
    if not inside(food):
        food.x -= dx
        food.y -= dy

def move():
    """Move the snake forward by one segment, handle collisions and food consumption."""
    head = snake[-1].copy()  # Copy the current head
    head.move(aim)  # Move the head based on the aim

    # Check if the snake runs into walls or itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Draw red square at the collision point
        update()
        return

    snake.append(head)  # Add the new head to the snake's body

    # Check if the snake eats the food
    if head == food:
        print('Snake length:', len(snake))  # Display the length of the snake
        food.x = randrange(-15, 15) * 10  # Generate a new random position for the food
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  # Remove the last segment of the snake (movement)

    move_food()  # Move the food each time the snake moves

    clear()  # Clear the previous frame

    # Draw the snake
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Draw the food
    square(food.x, food.y, 9, food_color)
    update()  # Update the screen
    ontimer(move, 100)  # Schedule the next move (can adjust timing for speed)

# Set up the game screen
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Randomly choose colors for the snake and food, ensuring they are different
snake_color = choice(colors)
food_color = choice(colors)
while food_color == snake_color: # Checks that they are not the same
    food_color = choice(colors) 

# Map arrow keys to change direction
onkey(lambda: change(10, 0), 'Right')  # Move right
onkey(lambda: change(-10, 0), 'Left')  # Move left
onkey(lambda: change(0, 10), 'Up')  # Move up
onkey(lambda: change(0, -10), 'Down')  # Move down

# Start the game loop
move()
done()
