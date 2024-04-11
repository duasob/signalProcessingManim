from manim import *
import numpy as np

class EulerFormula3DScene(ThreeDScene):
    def construct(self):
        # Create 3D Axes
        axes = ThreeDAxes(

        )

        # Add axes to the scene
        self.add(axes)
        self.set_camera_orientation(phi=0 * DEGREES, theta=90 * DEGREES)

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
        self.add_fixed_in_frame_mobjects(euler_formula)  # Keeps text fixed in frame
        
        self.move_camera(phi=45 * DEGREES, theta= 45* DEGREES, run_time=3)
        # Euler's formula in 3D, incorporating 't' as the z-axis to create a spiral
        def e_to_i_theta_3d(t):
            return np.array((np.cos(t), np.sin(t), t/5))  # 't' also maps to the z-axis
        
        # Create the 3D parametric curve
        curve3D = ParametricFunction(
            e_to_i_theta_3d,
            t_range = np.array([0, 8*PI]),  # Extended to see more of the spiral
            color = BLUE
        )
        
        # Play creation animations
        self.play(Transform(curve, curve3D))
        self.move_camera(phi=15 * DEGREES, theta=-45* DEGREES, run_time=5)
        # Animate the movement of the camera to fully appreciate the 3D structure
        
        self.wait(1)  # Hold the final view for a second




class EulerFormula3DXScene(ThreeDScene):
    def construct(self):
        # Create 3D Axes
        axes = ThreeDAxes()

        # Add axes to the scene
        self.add(axes)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES)

        def e_to_i_theta(t):
            return np.array((0,np.cos(t) , np.sin(t)))
        
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
        self.add_fixed_in_frame_mobjects(euler_formula)  # Keeps text fixed in frame
        
                
        self.move_camera(phi=45 * DEGREES, theta=-45* DEGREES, run_time=2)
        
        # Euler's formula in 3D, but 't' now maps to the x-axis to create a spiral from left to right
        def e_to_i_theta_3dx(t):
            return np.array((t/5,np.cos(t) ,np.sin(t)))  # 't' maps to the x-axis
        
        # Create the 3D parametric curve for the modified spiral
        curve3D = ParametricFunction(
            e_to_i_theta_3dx,
            t_range = np.array([0, 8*PI]),  # Extended to see more of the spiral
            color = BLUE
        )
        
        # Play creation animations

        
        
        self.play(Transform(curve, curve3D))
        self.move_camera(phi=70 * DEGREES, theta=-30* DEGREES, run_time=2)

        self.play(FadeOut(euler_formula))
        euler_formula = MathTex("z = cos(\\theta) + isin(\\theta)", font_size=50).to_corner(UL)
        self.add_fixed_in_frame_mobjects(euler_formula)
        copy_curve = curve.copy()

        def cosine(t):
            return np.array((t/5,np.cos(t),0))
        
        cosine_curve = ParametricFunction(
            cosine,
            t_range = np.array([0, 8*PI]),  # Extended to see more of the spiral
            color = BLUE
        )

        def sine(t):
            return np.array((t/5,0,np.sin(t)))  # 't' maps to the x-axis
        
        sine_curve = ParametricFunction(
            sine,
            t_range = np.array([0, 8*PI]),  # Extended to see more of the spiral
            color = BLUE
        )

        curves = VGroup(cosine_curve, sine_curve)
        #self.play(Transform(curve, curves))
        self.play(Transform(curve, cosine_curve))
        self.move_camera(phi=0 * DEGREES, theta= -90* DEGREES, run_time=2)
        
        self.wait(1)
        self.move_camera(phi=45 * DEGREES, theta=-45* DEGREES, run_time=2)
        self.play(Transform(curve, copy_curve))


        self.play(Transform(curve, sine_curve))
        self.move_camera(phi=90 * DEGREES, theta= -90* DEGREES, run_time=2)
        
        
        

        self.wait(1)  # Hold the final view for a second

class EulerFormula3DXSceneNW(ThreeDScene):
    def construct(self):
        # Create 3D Axes
        axes = ThreeDAxes()

        # Add axes to the scene
        self.add(axes)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES)

        def e_to_i_theta(t):
            return np.array((0,np.cos(t) , np.sin(t)))
        
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
        self.add_fixed_in_frame_mobjects(euler_formula)  # Keeps text fixed in frame
        
                
        
        
        # Euler's formula in 3D, but 't' now maps to the x-axis to create a spiral from left to right
        def e_to_i_theta_3dx(t):
            return np.array((t/5,np.cos(t) ,np.sin(t)))  # 't' maps to the x-axis
        
        # Create the 3D parametric curve for the modified spiral
        curve3D = ParametricFunction(
            e_to_i_theta_3dx,
            t_range = np.array([0, 8*PI]),  # Extended to see more of the spiral
            color = BLUE
        )
        
        # Play creation animations

        
        
        amin1 = AnimationGroup(
            self.move_camera(phi=45 * DEGREES, theta=-45* DEGREES,run_time=2),
            self.play(Transform(curve, curve3D)),
            lag_ratio=0
        )

        self.play(amin1)

        self.play(FadeOut(euler_formula))
        euler_formula = MathTex("z = cos(\\theta) + isin(\\theta)", font_size=50).to_corner(UL)
        self.add_fixed_in_frame_mobjects(euler_formula)
        copy_curve = curve.copy()

        def cosine(t):
            return np.array((t/5,np.cos(t),0))
        
        cosine_curve = ParametricFunction(
            cosine,
            t_range = np.array([0, 8*PI]),  # Extended to see more of the spiral
            color = BLUE
        )

        def sine(t):
            return np.array((t/5,0,np.sin(t)))  # 't' maps to the x-axis
        
        sine_curve = ParametricFunction(
            sine,
            t_range = np.array([0, 8*PI]),  # Extended to see more of the spiral
            color = BLUE
        )

        curves = VGroup(cosine_curve, sine_curve)
        #self.play(Transform(curve, curves))
        anim2 = AnimateGroup(
            Transform(curve, cosine_curve),
            self.move_camera(phi=0 * DEGREES, theta= -90* DEGREES),
            run_time=2
        )
        
        self.play(anim2)
        self.wait(1)
        
        anim3 = AnimateGroup(
            self.move_camera(phi=45 * DEGREES, theta=-45* DEGREES),
            Transform(curve, copy_curve),
            run_time=2
        )
        self.play(anim3)

        anim4 = AnimateGroup(
           Transform(curve, sine_curve),
            self.move_camera(phi=90 * DEGREES, theta= -90* DEGREES),
            run_time=2
        )
        
        
        
        

        self.wait(1)  # Hold the final view for a second
