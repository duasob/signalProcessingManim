from manim import *
import numpy as np

class EulerFormula3DScene(ThreeDScene):
    def construct(self):
        # Create 3D Axes
        axes = ThreeDAxes(

        )

        # Add axes to the scene
        self.add(axes)
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        def e_to_i_theta(t):
            return np.array((np.cos(t), np.sin(t), 0))
        
        # Create the parametric curve using the function
        curve = ParametricFunction(
            e_to_i_theta,
            t_range = np.array([0, 2*PI]),
            color = BLUE
        )
        
        self.play(Create(curve))
        self.wait(1)
        # Display Euler's formula
        euler_formula = MathTex("z = e^{i\\theta}", font_size=50).to_corner(UL)
        self.play(Write(euler_formula))
        self.add_fixed_in_frame_mobjects(euler_formula)  # Keeps text fixed in frame
        
        self.move_camera(phi=75 * DEGREES, theta= 45* DEGREES, run_time=3)
        # Euler's formula in 3D, incorporating 't' as the z-axis to create a spiral
        def e_to_i_theta_3d(t):
            return np.array((np.cos(t), np.sin(t), t/5))  # 't' also maps to the z-axis
        
        # Create the 3D parametric curve
        curve3D = ParametricFunction(
            e_to_i_theta_3d,
            t_range = np.array([0, 4*PI]),  # Extended to see more of the spiral
            color = BLUE
        )
        
        # Play creation animations
        self.play(Transform(curve, curve3D))
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=5)
        self.wait(5)
        # Animate the movement of the camera to fully appreciate the 3D structure
        
        self.wait(1)  # Hold the final view for a second
