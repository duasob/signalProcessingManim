from manim import *
import numpy as np


def create_axes(x_range, y_range):
    axes = Axes(
        x_range=x_range,  # Adding a step size for clarity
        y_range=y_range,  # Adding a step size for clarity
        axis_config={"color": WHITE},  # This is correct
    )
    return axes

def create_sine(axes, freq=1, color=RED):
    x = np.linspace(0, 10, 1000)
    y = np.sin(freq * x)
    points = [axes.coords_to_point(x, y) for x, y in zip(x, y)]
    return VMobject().set_points_as_corners(points).set_color(color)

def sample(axes, func,  x_range, n, f=1):
    x = np.linspace(x_range[0], x_range[1], n)
    y = func(x * f)
    points = [axes.coords_to_point(x, y) for x, y in zip(x, y)]
    return VGroup(*[Dot(point) for point in points])


class Animate(Scene):
    def construct(self):
        axis = create_axes([0, np.pi*2+1, np.pi/4], [-1, 1, 0.2])
        self.add(axis)
        sine_f1 = create_sine(axis, 1)
        N = 10
        N_label = MathTex(f"N = {N}").move_to(axis.y_axis.get_top() + UP * 0.5)
        sine_f1_label = MathTex("f = 1").next_to(N_label).set_color(RED)
        sine_f1 = VGroup(sine_f1, sine_f1_label)
        self.play(Create(sine_f1))


        sample_f1 = sample(axis, np.sin, [0, np.pi*2], N, 1)
        sample_f1 = VGroup(sample_f1, N_label)
        self.play(Create(sample_f1))

        self.wait(1)
        #Create aliased sine wave
        sine_f2 = create_sine(axis, 10, BLUE)
        sine_f2_label = MathTex("f = 10").next_to(sine_f1_label).set_color(BLUE)
        sine_f2 = VGroup(sine_f2, sine_f2_label)
        #how do I slow don the play speed of the animation?
        
        self.play(Create(sine_f2), run_time=2)

        self.wait(2)
        
        # Show that the N samples of the aliased sine wave are the same as the original sine wave
        N = 8
        sample_f2 = sample(axis, np.sin, [0, np.pi*2], N, 1)
        N_label = MathTex(f"N = {N}").move_to(axis.y_axis.get_top() + UP * 0.5)
        sample_f2 = VGroup(sample_f2, N_label)
        self.play(Transform(sample_f1, sample_f2), run_time=2)
        self.wait(2)

        sine_3 = create_sine(axis, 8 , BLUE)
        sine_3_label = MathTex("f = 8").next_to(sine_f1_label).set_color(BLUE)
        sine_3 = VGroup(sine_3, sine_3_label)
        self.play(Transform(sine_f2, sine_3), run_time=2)
        
        self.wait(2)

