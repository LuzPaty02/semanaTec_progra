# Free Games Library games enhancement project

This is a repository that contains the enhanced functions for 5 free games files. [Link to the library.](https://grantjenks.com/docs/freegames/)
## Free Python Games Quickstart

Free Python Games is a collection of Python games that are fun and easy to run. Follow this guide to get started!

## Installation

Installing Free Python Games is simple using `pip`:

```bash
$ python3 -m pip install freegames
```
Make sure to install the following libraries 

Turtle

```bash
$ python3 -m pip install turtle
```
Tkinter
```bash

$ python3 -m pip install tkinter
```


## Games modified
### Paint 
Game that draws lines and shapes on the screen. Click to mark the start of a shape and click again to mark its end. Different shapes and colors can be selected using the keyboard.
- Added onkey color yellow
- draw circle functionality
-  completed rectangle and triangle functions

  
### Snake
classic arcade game. Use the arrow keys to navigate and eat the green food. Each time the food is consumed, the snake grows one segment longer. Avoid eating yourself or going out of bounds!
- Move food randomly
- change element colors each run


### Pacman
classic arcade game. Use the arrow keys to navigate and eat all the white food. Watch out for red ghosts that roam the maze.
- make ghosts smarter
- modify maze
- speed ghosts
  
### Cannon
projectile motion. Click the screen to fire your cannnonball. The cannonball pops blue balloons in its path. Pop all the balloons before they can cross the screen.
- cannon speed
- infinite running

### Memory
puzzle game of number pairs. Click a tile to reveal a number. Match two numbers and the tiles will disappear to reveal an image.
- added tap counter
- detect discovered taps
- center digit in square
- add letters to the data

## Running each game

Paint 
```bash
$ python3 python paint.py
```

Snake 
```bash
$ python3 python snake.py
```

Pacman 
```bash
$ python3 python pacman.py
```

Memory
```bash
$ python3 python memory.py
```

Cannon
```bash
$ python3 python cannon.py
```

