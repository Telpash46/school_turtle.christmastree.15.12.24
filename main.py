import random
import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(400, 0)

n = 60
t.speed(1000)
t.pensize(5)
t.color("brown")
t.left(90)
t.forward(3*n)
t.backward(n*4.8)
t.pensize(1)
t.color("dark green")

def tree(d, s):
    if d <= 0: return
    t.forward(s)
    tree(d - 1, s*.8)
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)

def add_ball(x, y, color, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def add_star(x, y, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.end_fill()
    t.penup()


def blink_star_center(x, y):
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
    while True:
        t.penup()
        t.goto(x, y - 15)  # Опускаемся немного ниже центра звезды
        t.pendown()
        t.color(random.choice(colors))
        t.begin_fill()
        t.setheading(0)  # Устанавливаем начальное направление (вниз)

        t.forward(20)

        t.setheading(-70)
        t.forward(25)

        t.setheading(-140)
        t.forward(20)

        t.setheading(-210)
        t.forward(25)

        t.setheading(-280)
        t.forward(25)
        t.end_fill()
        turtle.hideturtle()


tree(20, n)
add_star(-50, 225, 'orange')

def generate_data():

    if len(allowed_x) > 0:
        coords_index = random.randint(0, len(allowed_x) - 1)
        size = random.randint(10, 15)
        data_to_return = {
            'ok': True,
            'x': allowed_x[coords_index],
            'y': allowed_y[coords_index],
            'color': colors[coords_index],
            'size': size
        }
        allowed_x.pop(coords_index)
        allowed_y.pop(coords_index)
        colors.pop(coords_index)
        return data_to_return
    else:
        return {
            'ok': False,
            'x': None,
            'y': None,
            'color': None,
            'size': None
        }
allowed_x = [-10, -30, -20, 40, 30, -10, 25, -60, 70, 30]
allowed_y = [50, 5, -50, 20, -30, 90, 110, -80, -90, -80]
colors = ["red", "blue", "yellow", "purple", "pink", "orange", "gold", "silver", "brown", "green"]

for _ in range(10):
    data = generate_data()
    if data.get('ok'):
        add_ball(data.get('x'), data.get('y'), data.get('color'), data.get('size'))
        print("added ball")
blink_star_center(-10, 240)

screen.update()
turtle.done()