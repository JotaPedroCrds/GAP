from manim import *
import numpy as np

class Sunflower(Scene):
    def construct(self):
        kernel = Circle(color = ManimColor("#925F17"), radius=0.5, fill_opacity=1, ).set_z_index(1)
        circles = VDict()
        Pétalas = VDict()
        for i in range(13):
            circles["{}".format(i)] = Circle(color=BLACK, radius=1.5).move_to([np.cos(((np.pi)/6)*i), np.sin(((np.pi)/6)*i), 1])
            self.play(FadeIn(circles["{}".format(i)]))
        self.play(FadeIn(kernel))
        for i in range(13):
            if i>0:
                tamanho = 0
                for j in range(i):
                    if j>=0:
                        Pétalas["{}".format(j)] = Intersection(circles["{}".format(i-j)], circles["{}".format(i)], color=ManimColor("#E8B12D"), stroke_width=0)
                        if Pétalas["{}".format(j)].has_points():
                            tamanho =+ 1
                            Pétalas["{}".format(j)].set_opacity((tamanho)*(1/11))
                        self.play(FadeIn(Pétalas["{}".format(j)]))
            self.play(FadeOut(circles["{}".format(i)]))
