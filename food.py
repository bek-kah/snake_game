from turtle import Turtle
import turtle
import random
turtle.colormode(255)


class Food(Turtle):

    def __init__(self, random_color):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.refresh(random_color)
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed('fastest')

    def refresh(self, random_color):
        self.color(random_color)
        random_x = random.randint(-280, 280)
        randon_y = random.randint(-280, 240)
        self.goto(random_x, randon_y)
