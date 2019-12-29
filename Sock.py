from turtle import Screen, Turtle, mainloop

def main():
    space = Screen()
    space.setup(450, 450),  space.title('Sock')
    space.bgcolor('green')

    pen = Turtle(shape='circle')
    pen.shapesize(0.3), pen.width(5)
    create_sock(pen)
    pen.ht()

def create_sock(pen):
    pen.color('black', 'red'), pen.speed(9)
    pen.seth(90)
    pen.pu(), pen.goto(100, -100), pen.pd()
    pen.begin_fill()
    pen.fd(140), pen.circle(20, 60), pen.fd(140)
    pen.circle(20, 90), pen.fd(70), pen.circle(20, 90)
    pen.fd(70), pen.circle(-20, 60), pen.fd(79.74)
    pen.circle(50, 90), pen.fd(15.62), pen.circle(50, 90)
    pen.end_fill()

    pen.color('black', 'white'), pen.speed(9)
    pen.seth(60)
    pen.pu(), pen.goto(3.40, 107.32), pen.pd()
    
    pen.begin_fill()
    for i in range(2):
        pen.circle(20, 90), pen.fd(50)
        pen.circle(20, 90), pen.fd(110)
    pen.end_fill()


if __name__ == "__main__":
    main()
    mainloop()