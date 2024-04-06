from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Create a square
        square = Square()  
        
        # Display the square
        self.play(Create(square))
        
        # Wait for a moment
        self.wait(1)  
        
        # Transform the square into a circle
        self.play(Transform(square, Circle()))  
        
        # Wait for a moment
        self.wait(1)  
