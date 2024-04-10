from manim import *
import numpy as np

class EulerFormula3DScene(ThreeDScene):
    def construct(self):
        # Create 3D Axes
        axes = ThreeDAxes(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            z_range=[-2, 10, 1],  # Extended z-range to accommodate spiral
            axis_config={"color": WHITE},
        )

        # Add axes to the scene
        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Display Euler's formula
        euler_formula = MathTex("z = e^{i\\theta}", font_size=36).to_corner(UL)
        self.add_fixed_in_frame_mobjects(euler_formula)  # Keeps text fixed in frame
        
        # Euler's formula in 3D, incorporating 't' as the z-axis to create a spiral
        def e_to_i_theta_3d(t):
            return np.array((np.cos(t), np.sin(t), t))  # 't' also maps to the z-axis
        
        # Create the 3D parametric curve
        curve = ParametricFunction(
            e_to_i_theta_3d,
            t_range = np.array([0, 4*PI]),  # Extended to see more of the spiral
            color = BLUE
        )
        
        # Play creation animations
        self.play(Create(curve))
        self.wait(1)  # Hold the view for a second
        
        # Animate the movement of the camera to fully appreciate the 3D structure
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=3)
        self.wait(1)  # Hold the final view for a second
