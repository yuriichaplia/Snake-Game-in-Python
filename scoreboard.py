from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x = 0, y = 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
