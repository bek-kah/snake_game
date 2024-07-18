import random
import turtle
from turtle import Turtle
SIZES = [1, 1.05, 1.1, 1.15, 1.2]
turtle.colormode(255)

STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]


class Snake:
    def __init__(self, random_color):
        self.segments = []
        self.create_snake(random_color)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def reset(self, random_color):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake(random_color)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self, random_color):
        for position in STARTING_POSITIONS:
            self.add_segment(position, random_color)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def coords(self):
        return round(self.head.xcor()), round(self.head.ycor())

    def tail_coords(self):
        return round(self.tail.xcor()), round(self.tail.ycor())

    def add_segment(self, position, random_color):
        new_segment = Turtle()
        rand_color = (random_color)
        new_segment.color(rand_color)
        new_segment.shape('square')
        rand = random.choice(SIZES)
        new_segment.shapesize(rand, rand)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self, random_color):
        self.add_segment(self.segments[-1].position(), random_color)

    def reset_snake(self):
        self.segments = []
        self.create_snake()

