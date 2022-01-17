from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color{colors}: ")
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
