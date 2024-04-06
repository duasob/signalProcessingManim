from manim import *
import numpy as np

class ConvolutionScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4], y_range=[-2, 2],
            axis_config={"color": BLUE},
        )

        # Define the first function
        f = lambda x: np.exp(-x**2)
        f_graph = axes.plot(f, color=RED, label='f(t)')

        # Define the second function, which we'll treat as the kernel for convolution
        g = lambda x: np.exp(-(x-2)**2)
        g_graph = axes.plot(g, color=GREEN, label='g(t)')

        # Add axes and function plots to the scene
        self.add(axes, f_graph, g_graph)

        # Display the labels
        f_label = axes.get_graph_label(f_graph, label='f(t)')
        g_label = axes.get_graph_label(g_graph, label='g(t)', x_val=3)
        self.play(Create(f_label), Create(g_label))

        # Convolution result (for visualization, this is a simplified representation)
        convolution = lambda x: np.sqrt(np.pi) * np.exp(-x**2 / 4) * np.cos(5*x)
        convolution_graph = axes.plot(convolution, color=PURPLE, label='(f*g)(t)')
        convolution_label = axes.get_graph_label(convolution_graph, label='(f*g)(t)', x_val=-3)

        self.wait(1)

        # Transition to convolution graph
        self.play(Transform(f_graph, convolution_graph), Transform(g_graph, convolution_graph),
                  FadeOut(f_label), FadeOut(g_label), Create(convolution_label))

        self.wait(2)

class Axis(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10],
            y_range=[-5, 5],
            axis_config={"color": WHITE},
        )

        self.add(axes)
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
        self.wait(1)
        