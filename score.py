from turtle import Turtle


class Score(Turtle):

    def __init__(self, x_position, y_position):

        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(x_position, y_position)
        self.update_score()

    def update_score(self):
        self.write(self.score, font=("Courier", 40, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

