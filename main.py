import turtle
import time
import random

game_over = False
score = 0
HEIGHT, WIDTH = 500, 500
mick = turtle.Turtle()
scoreboard = mick.clone()
scoreboard.penup()
mick.penup()
style = ('Courier', 30)
finish_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(HEIGHT, WIDTH)
screen.bgcolor("light blue")
screen.title("deneme")

def turtle_click(x, y):
    global score
    score += 1
    scoreboard.clear()
    scoreboard.write(f"score:{score} ", move=False, font=style, align="left")
    turtle_spawner()


def finish_time(time):
    global game_over
    finish_turtle.hideturtle()
    finish_turtle.penup()
    finish_turtle.setpos(-50, 300)
    finish_turtle.clear()
    if time > 0:
        finish_turtle.clear()
        finish_turtle.write(arg=f"time: {time}", move=False, font=style, align="left")
        screen.ontimer(lambda: finish_time(time -1), 1000)
    else:
        game_over = True
        finish_turtle.clear()
        finish_turtle.hideturtle()
        mick.hideturtle()
        finish_turtle.write(arg=f"game finished", move=False, font=style, align="left")


#kaplumbağa
mick.shape("turtle")
mick.shapesize(3,3)
mick.color("green")
mick.onclick(turtle_click)
score = 0

#def scoreboard_score():




def scoreboardMain():
    scoreboard.hideturtle()
    scoreboard.setpos(-50, 360)
    scoreboard.write(f"score:{score} ", move=False, font=style, align="left")

def turtle_spawner():
    if not game_over:
        mick.setpos(random.randint(-300,300), random.randint(-300,300))
        screen.ontimer(turtle_spawner, 3000)





turtle.tracer(0)
turtle_spawner()
scoreboardMain()
finish_time(10)
turtle.tracer(1)
turtle.mainloop()