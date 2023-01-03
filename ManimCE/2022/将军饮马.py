from manim import *
import math


class yinma(Scene):
    def construct(self):
        def chin(a):
            txt = Tex(a, tex_template=TexTemplateLibrary.ctex)
            return txt

        def crossing(line1, line2):
            a = line1.start
            b = line1.end
            c = line2.start
            d = line2.end
            p = math.tan(math.atan2((b[1]-a[1]), (b[0]-a[0])))
            f = a[1]-a[0]*p
            g = math.tan(math.atan2((d[1]-c[1]), (d[0]-c[0])))
            h = c[1]-c[0]*g
            x = (h-f)/(p-g)
            # print(p,f,g,h)
            lis = np.array([x, f+p*x, 0])
            return lis
        hzx = chin('黄子轩制作').to_corner(UR)
        self.play(Write(hzx))
        p = ValueTracker(-1)
        bx = ValueTracker(2.5)
        by = ValueTracker(2)
        dota = always_redraw(lambda: Dot(LEFT*3+UP*3))
        dotp = always_redraw(lambda: Dot([p.get_value(), 0, 0], color=RED))
        dotb = always_redraw(lambda: Dot(
            RIGHT*bx.get_value()+UP*by.get_value(), color=BLUE))
        dotb2 = always_redraw(lambda: Dot(
            RIGHT*bx.get_value()+DOWN*by.get_value(), color=GREEN))
        l = Line(LEFT*5, RIGHT*5)
        self.play(Create(l))
        self.play(Create(dota), Create(dotb), Create(dotp), Create(dotb2))
        ap = always_redraw(lambda: Line(dota.get_center(),
                           dotp.get_center(), color=YELLOW))
        bp = always_redraw(lambda: Line(dotb.get_center(), dotp.get_center()))
        b2p = always_redraw(lambda: Line(
            dotb2.get_center(), dotp.get_center()))
        self.play(Create(ap), Create(bp), Create(b2p))

        a = always_redraw(lambda: Tex('A').next_to(dota, UP))
        b = always_redraw(lambda: Tex('B', color=BLUE).next_to(dotb, UP))
        b2 = always_redraw(lambda: Tex("B'", color=GREEN).next_to(dotb2, UP))
        tp = always_redraw(lambda: Tex('P', color=RED).next_to(dotp, UP))
        self.play(Write(a), Write(b), Write(b2), Write(tp), run_time=2)
        self.wait()
        t1 = chin("因为PB=PB'")
        t2 = chin("所以AP+PB=AP+PB'")

        t3 = chin("因为两点之间线段最短")
        t4 = chin("所以当P在AB'的连线上时AP+PB'取最小值")
        t5 = chin("即AP+PB取最小值")
        g = Group(t1, t2, t3, t4, t5).arrange(DOWN).to_corner()
        for i in range(5):
            g[i].to_edge()
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait()
        self.play(bx.animate.increment_value(1), run_time=2)
        self.play(bx.animate.increment_value(-2),
                  by.animate.increment_value(1), run_time=2)
        self.play(bx.animate.increment_value(1),
                  by.animate.increment_value(-1), run_time=2)
        self.play(p.animate.increment_value(3), run_time=2)
        self.play(p.animate.increment_value(-6), run_time=2)
        self.wait()
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        line = Line(dota, dotb2).set_opacity(0.3)
        self.play(FadeIn(line), run_time=2)
        self.play(p.animate.set_value(crossing(l, line)[0]), run_time=2)
        self.play(FadeOut(line), run_time=2)
