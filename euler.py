from manim import *
import numpy as np

class EulerFormulaScene(ThreeDScene):
    def construct(self):
        # Create 3D Axes
        axes = ThreeDAxes(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            z_range=[-2, 2, 0.5],
            axis_config={"color": WHITE},
        )

        # Add axes to the scene
        self.add(axes)
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        euler_formula = MathTex("z = e^{i\\theta}", font_size=36).to_corner(UL)
        
        
        def e_to_i_theta(t):
            return np.array((np.cos(t), np.sin(t), 0))
        
        # Create the parametric curve using the function
        curve = ParametricFunction(
            e_to_i_theta,
            t_range = np.array([0, 2*PI]),
            color = BLUE
        )
        
        self.play(Create(curve))
        self.play(Write(euler_formula))

        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=3)
