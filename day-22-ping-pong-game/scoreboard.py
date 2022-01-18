from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 38, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 240)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()
