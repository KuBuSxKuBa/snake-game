from turtle import Turtle
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0 , 260)
        self.update_scoreboard()


    # def add_point(self):
    #     self.clear()
    #     self.score += 1
    #     self.write(f"Score : {self.score}", False, align="center", font=("Arial", 20))
    #
    # # def game_over(self):
    #     # global SCORE
    #     # self.clear()
    #     # self.goto(0 , 0)
    #     # self.write(f"Game over! Total score: {SCORE}" , False, align="center", font=("Arial", 20))
    #
    # def reset(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.score = 0
    #     self.clear()
    #     self.write(f"Score : {self.score} High score : {self.high_score}", False, align="center", font=("Arial", 20))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_highscore(self):
        print(self.high_score)
        with open("highscore.txt", "w") as file:
            file.write(self.high_score)
