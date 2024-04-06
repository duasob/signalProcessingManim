from manim import *
import numpy as np

def create_axes():
    x_range = [0, 10, np.pi/4]
    axes = Axes(
        x_range=x_range,  # Adding a step size for clarity
        y_range=[-1, 1, 0.2],  # Adding a step size for clarity
        axis_config={"color": WHITE},  # This is correct
    )
    return axes
        
def create_sine(axes):
    # Define the sine function
    sine = lambda x: np.sin(x)
    # Plot the sine function on the defined axes
    sine_graph = axes.plot(sine, color=RED)
    return sine_graph

def create_square_wave(axes):
    square_wave_start = axes.c2p(0, 1)  # Convert from axes coordinates to scene points
    square_wave_end = axes.c2p(np.pi, 1)

    square_wave = Line(square_wave_start, square_wave_end, color=BLUE)
    end_line_start = axes.c2p(np.pi, 0)
    end_line_end = axes.c2p(np.pi, 1)
    end_line = Line(end_line_start, end_line_end, color=BLUE)

    # Horizontal line at y=0 for x > pi/2 to represent value of 0
    zero_line_start = axes.c2p(np.pi, 0)
    zero_line_end = axes.c2p(10, 0)  # Adjust according to your x_range
    zero_line = Line(zero_line_start, zero_line_end, color=BLUE, stroke_width=2)
    # Animate drawing of the zero value line


    square_wave = VGroup(square_wave, end_line, zero_line)
    return square_wave

class ConvolutionScene(Scene):
    def construct(self):
        axes = create_axes()
        self.add(axes)
        self.wait(1)
        sine_graph = create_sine(axes)
        self.play(Create(sine_graph))
        
        sine_graph = VGroup(axes, sine_graph)
        self.play(sine_graph.animate.scale(0.5))
        self.play(sine_graph.animate.to_corner(UR))
        
        axes2 = create_axes()
        self.add(axes2)
        square_wave_graph = create_square_wave(axes2)
        square_wave_graph = VGroup(axes2, square_wave_graph)
        self.play(Create(square_wave_graph))
        self.play(square_wave_graph.animate.scale(0.5))
        self.play(square_wave_graph.animate.to_corner(UL))

        square_wave_graph_copy = square_wave_graph.copy()
        square_wave_graph_copy.scale([-1, 1, 1], about_point=square_wave_graph_copy.get_center())
        self.play(Transform(square_wave_graph, square_wave_graph_copy))

        self.wait(1)





class DiscreteSquareWave(Scene):
    def construct(self):
        # Define the axes
        

        # Define the sine function
        sine = lambda x: np.sin(x)
        # Plot the sine function on the defined axes
        sine_graph = axes.plot(sine, color=RED)

        
        
        self.add(axes)
        self.wait(0.5)
        self.play(Create(sine_graph))
        self.wait(0.5)  # Wait for 1 second at the end of the animation

        N = np.pi/4  # Sampling every 1 unit along the x-axis
        x_samples = np.arange(0, 10, N)  # Adjust the range as necessary
        lines_and_dots = VGroup()
        for x in x_samples:
            start_point = axes.c2p(x, 0)  # Start at the x-axis
            end_point = axes.c2p(x, sine(x))  # End at the sampled point on the sine wave
            line = Line(start_point, end_point, color=YELLOW)
            dot = Dot(end_point, color=YELLOW)
            lines_and_dots.add(line, dot)  # Add both the line and dot to the group

        # Animate the appearance of lines and dots
        self.play(LaggedStart(*[Create(obj) for obj in lines_and_dots], lag_ratio=0.1))
        self.wait(1)



class DiscreteSine(Scene):
    def construct(self):
        # Define the axes
        x_range = [0, 10, np.pi/4]
        axes = Axes(
            x_range=x_range,  # Adding a step size for clarity
            y_range=[-1, 1, 0.2],  # Adding a step size for clarity
            axis_config={"color": WHITE},  # This is correct
        )

        # Define the sine function
        sine = lambda x: np.sin(x)
        # Plot the sine function on the defined axes
        sine_graph = axes.plot(sine, color=RED)

        
        
        self.add(axes)
        self.wait(0.5)
        self.play(Create(sine_graph))
        self.wait(0.5)  # Wait for 1 second at the end of the animation

        N = np.pi/4  # Sampling every 1 unit along the x-axis
        x_samples = np.arange(0, 10, N)  # Adjust the range as necessary
        lines_and_dots = VGroup()
        for x in x_samples:
            start_point = axes.c2p(x, 0)  # Start at the x-axis
            end_point = axes.c2p(x, sine(x))  # End at the sampled point on the sine wave
            line = Line(start_point, end_point, color=YELLOW)
            dot = Dot(end_point, color=YELLOW)
            lines_and_dots.add(line, dot)  # Add both the line and dot to the group

        # Animate the appearance of lines and dots
        self.play(LaggedStart(*[Create(obj) for obj in lines_and_dots], lag_ratio=0.1))
        self.wait(0.5)
        self.play(FadeOut(sine_graph))
        self.wait(0.5)
        graph = VGroup(axes, lines_and_dots)
        self.play(graph.animate.shift(RIGHT * 2))
        
        