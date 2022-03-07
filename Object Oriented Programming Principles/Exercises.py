## Polygon
 
# Goal: “Create class and sub-class objects which represent different geometrical shapes, such as Rectangles and Squares”
 
from abc import ABC, abstractmethod

class Shapes(ABC):
    Sides = True
    Corners = 0

    def Edges(self):
        return "Yes"

    def Quadlateral(self):
        self.Corners += 4

    @abstractmethod
    def Spherical(self):
        pass

    Lines = False

class Square(Shapes):

    def Quadlateral(self):
        self.Corners +=4

    def Spherical(self):
        return "No"

class Circle(Shapes):
    Sides = 1
    Corners = False

    def Spherical(self):
        return "It can be"

    def Edges(self):
        return "Just One"




## Lottery Ball
 
# Goal: “Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls 
# of each color that are in the hat. Give the object the ability to pick a random number of balls from the hat, 
# which will then be used to compute the probability of picking a certain distribution of balls over a large number 
# of experiments”