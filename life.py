from turtle import Turtle


class Live(Turtle):

    def __init__(self, x_position, y_position):

        super().__init__()
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(x_position, y_position)
        self.update_live()

    def update_live(self):
        self.write(self.lives, font=("Courier", 40, "normal"))

    def del_live(self):
        self.lives -= 1
        self.clear()
        self.update_live()

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", font=("Courier", 40, "normal"))