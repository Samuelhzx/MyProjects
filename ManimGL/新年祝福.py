'''
虽然manimpango里显示有Smiley Sans，但是不知为什么渲染出来就不是了
'''

from manimlib import *
from random import uniform as uni


class blessings(Scene):

    def construct(self):
        g = VGroup()

        def yanhua(height, x, path_h, colorp, colorf, rad, blessings, shift, scale=1, len=None):
            if len is None:
                len = rad - 0.1

            def get_path():
                getpath = Line(start=[x, -4, 0], end=[x, -4-path_h, 0])
                getpath.set_color_by_gradient(colorp, '#000000')
                return getpath

            path = get_path()
            self.add(path)
            text = Text(blessings, font='Smiley Sans', color=YELLOW,
                        run_time=2).shift(shift).scale(scale)
            g.add(text)
            self.play(path.animate.shift(UP*(4+height)),
                      rate_func=linear, run_time=2.5)
            self.play(ApplyMethod(path.set_opacity, 0, run_time=1.5),
                      Flash(path.get_start(), colorf, run_time=2,
                            flash_radius=rad, line_length=len),
                      Write(text))
        yanhua(2, 0, 3, BLUE, YELLOW, 1, '新年到了', UP*2, 2)
        yanhua(uni(-1, 3), uni(-5, 5), uni(1, 3), random_color(),
               random_color(), uni(0.3, 1.5), '祝大家', UP*1, 1.5)
        yanhua(uni(-1, 3), uni(-5, 5), uni(1, 3), random_color(),
               random_color(), uni(0.3, 1.5), '新年快乐', UP*0, 1.5)
        yanhua(uni(-1, 3), uni(-5, 5), uni(1, 3), random_color(),
               random_color(), uni(0.3, 1.5), '前兔无量', UP*-1, 1.5)
        yanhua(uni(-1, 3), uni(-5, 5), uni(1, 3), random_color(),
               random_color(), uni(0.3, 1.5), '奋发兔强', UP*-2, 1.5)
        byebye = Text('bye bye', font='Smiley Sans',
                      color=YELLOW, run_time=2).shift(UP).scale(3)
        hihi = Text('hi hi', font='Smiley Sans', color=YELLOW,
                    run_time=2).shift(UP).scale(3)
        _2022 = Tex('202', '2').shift(DOWN).scale(3)
        _2023 = Tex('202', '3').shift(DOWN).scale(3)
        self.play(FadeOut(g))
        self.play(FadeIn(byebye))
        self.play(FadeIn(_2022, lag_ratio=0.5))
        self.wait()
        self.play(Transform(byebye, hihi))
        self.play(TransformMatchingTex(_2022, _2023))
        self.wait(2)
