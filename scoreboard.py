from turtle import Turtle
SCORE = 0
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0 , 260)
        self.write(f"Score : {SCORE}" , False , align="center" , font=("Arial" , 20))


    def add_point(self):
        global SCORE
        self.clear()
        SCORE += 1
        self.write(f"Score : {SCORE}", False, align="center", font=("Arial", 20))

    def game_over(self):
        global SCORE
        self.clear()
        self.goto(0 , 0)
        self.write(f"Game over! Total score: {SCORE}" , False, align="center", font=("Arial", 20))