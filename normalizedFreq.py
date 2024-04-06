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
        axes = create_axes([0, 10, np.pi/4], [-1, 1, 0.2])
        self.add(axes)
        self.wait(1)
        sine_graph = create_sine(axes)
        self.play(Create(sine_graph))

        fs = 2
        f = 1
        sample_points = sample(axes, np.sin, [0, 10], 10*fs)
        self.play(Create(sample_points))
        
        fs_value_text = MathTex(f"f_s = {fs}").move_to(axes.y_axis.get_top() + UP * 0.5)
        f_value_text = MathTex(f"f = {f}").move_to(axes.y_axis.get_top() + UP * 0.5 + RIGHT * 2)
        omeaga_value_text = MathTex(f"\Omega = 2 \pi ({f/fs})").move_to(axes.y_axis.get_top() + UP * 0.5 + RIGHT * 5)
        letters = VGroup(fs_value_text, f_value_text, omeaga_value_text)
        self.play(Create(letters))

        self.wait(1)
        sine_1 = VGroup(sine_graph, sample_points, letters)
        f = 2
        sine_2 = create_sine(axes, f, BLUE)
        sample_points2 = sample(axes, np.sin, [0, 10], 10*fs, f)
        fs_value_text2 = MathTex(f"f_s = {fs}").move_to(axes.y_axis.get_top() + UP * 0.5)
        f_value_text2 = MathTex(f"f = {f}").move_to(axes.y_axis.get_top() + UP * 0.5 + RIGHT * 2)
        omeaga_value_text2 = MathTex(f"\Omega = 2 \pi ({f/fs})").move_to(axes.y_axis.get_top() + UP * 0.5 + RIGHT * 5)
        letters2 = VGroup(fs_value_text2, f_value_text2, omeaga_value_text2)

        sine_2 = VGroup(sine_2, sample_points2, letters2)
        self.play(Transform(sine_1, sine_2))

        self.wait(1)

        fs = 4
        sine_3 = create_sine(axes, f, BLUE)
        sample_points3 = sample(axes, np.sin, [0, 10], 10*fs, f)
        fs_value_text3 = MathTex(f"f_s = {fs}").move_to(axes.y_axis.get_top() + UP * 0.5)
        f_value_text3 = MathTex(f"f = {f}").move_to(axes.y_axis.get_top() + UP * 0.5 + RIGHT * 2)
        omeaga_value_text3 = MathTex(f"\Omega = 2 \pi ({f/fs})").move_to(axes.y_axis.get_top() + UP * 0.5 + RIGHT * 5)
        letters3 = VGroup(fs_value_text3, f_value_text3, omeaga_value_text3)

        sine_3 = VGroup(sine_3, sample_points3, letters3)
        self.play(Transform(sine_1, sine_3))

        self.wait(3)