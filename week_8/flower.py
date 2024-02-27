import turtle

screen = turtle.Screen()
screen.bgcolor('white')
flower = turtle.Turtle()
flower.shape("classic")
flower.color("blue")

for _ in range(45) :
    flower.forward(100)
    flower.right(45)
    flower.forward(100)
    flower.right(135)
    flower.forward(100)
    flower.right(45)
    flower.forward(100)
    flower.right(170)

flower.hideturtle()

turtle.done()


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad .shape("turtle")
    brad.color("red")
    brad.speed(10)

    for a in range (36):
        brad.circle(100)
        brad.right(10)
    window.mainloop()
draw_flower    

    
