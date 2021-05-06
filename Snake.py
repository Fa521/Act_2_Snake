from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Se crean 2 numeros aleatorias de 1 a 5
color_snake_num = randrange(1,6)
color_food_num = randrange(1,6)

def color_snake(color_snake_num):
    """
    [Con un switch statement se regresa el color de la serpiente dependiendo del numero aleatorio]
    parameter color_snake_num: [numero aleatorio que decide el color]
    """
    switcher={
        1:'maroon',
        2:'violet',
        3:'magenta',
        4:'navy',
        5:'black'}
    return switcher.get(color_snake_num,"")

def color_food(color_food_num):
    """
    [Con un switch statement se regresa el color de la comida dependiendo del numero aleatorio]
    parameter color_food_num: [numero aleatorio que decide el color]
    """
    switcher={
        1:'yellow',
        2:'gold',
        3:'gray',
        4:'blue',
        5:'lightgreen'}
    return switcher.get(color_food_num,"")

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        # Se llama a la funcion para obtener el string del color
        square(body.x, body.y, 9, color_snake(color_snake_num))

    # Se llama a la funcion para obtener el string del color
    square(food.x, food.y, 9, color_food(color_food_num))
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
