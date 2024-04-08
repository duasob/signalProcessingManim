from manim import *

class Formula(Scene):
    def construct(self):
        #convolution

        formula = MathTex(r"y[n] = x[n] * h[n]").scale(1.5)
        self.play(Write(formula))
        self.wait(1)
        formulaN = MathTex(r"y[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k]").scale(1.5)
        self.play(Transform(formula, formulaN))
        formulaN = MathTex(r"y[n] = x[n] * h[n]").scale(1.5)
        self.wait(1)
        self.play(Transform(formula, formulaN))
        self.wait(1)
        x = MathTex(r"x[n] = z^{n}").scale(1.5).shift(UP).next_to(formula, UP)
        self.play(Write(x))
        self.wait(1)
        

        formulaN = MathTex(r"y[n] = z^{n} * h[n]").scale(1.5)
        self.play(Transform(formula, formulaN))
        self.play(FadeOut(x))
        formulaN = MathTex(r"y[n] = \sum_{k=-\infty}^{\infty} z^{n-k} h[k]").scale(1.5)
        self.play(Transform(formula, formulaN))
        self.wait(1)
        formulaN = MathTex(r"y[n] = z^{n}\sum_{k=-\infty}^{\infty} z^{-k} h[k]").scale(1.5)
        self.play(Transform(formula, formulaN))
        self.wait(1)
        formulaN = MathTex(r"y[n] = z^{n}H(z)").scale(1.5)
        self.play(Transform(formula, formulaN))
        self.wait(1)
        formulaN = MathTex(r"y[n] = x[n]H(z)").scale(1.5)
        self.play(Transform(formula, formulaN))
        self.wait(2)
