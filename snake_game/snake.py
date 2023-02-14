import turtle as t
from config import *


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)        
         
         
    def add_segment(self, position):
        turtle = t.Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)
            
         
    def extend(self):
        self.add_segment(self.segments[-1].position())
         
            
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
       
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
       
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        