from manim import *
<<<<<<< HEAD


class zhouduichen(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        shuiyin = Text('黄子轩制作', font='Simsun', fill_opacity=1).shift(UP)
        self.play(Create(axes), Write(shuiyin))
        half = VMobject()

        half.set_points_as_corners([[-1, 3, 0], [-1, 2, 0], [-4, 1, 0], [-2, 1, 0],
                                   [-3, 0, 0], [-2, -2, 0], [-1, 0, 0], [-1, -3, 0], [0, -3, 0], [-1, 3, 0]])
        half.shift(LEFT)

        start = UP*3  # +LEFT
        end = DOWN*3  # +LEFT
        line = Line3D(start, end, color=YELLOW)
        dui = Text('对称轴', font='Simsun').next_to(line, UP)
        text1 = Text("11.5.翻折与轴对称图形", font='Simsun').scale(0.8)
        text2 = Text("先画一个任意平面图形", font='Simsun').scale(0.5)
        text3 = Text("再指定一条对称轴", font='Simsun').scale(0.5)
        text4 = Text("于是我们画出了一组轴对称图形", font='Simsun').scale(0.5)
        g = VGroup(text1, text2, text3, text4)
=======
class zhouduichen(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        shuiyin=Text('黄子轩制作',font='Simsun',fill_opacity=1).shift(UP)
        self.play(Create(axes),Write(shuiyin))
        half=VMobject()

        half.set_points_as_corners([[-1,3,0],[-1,2,0],[-4,1,0],[-2,1,0],[-3,0,0],[-2,-2,0],[-1,0,0],[-1,-3,0],[0,-3,0],[-1,3,0]])
        half.shift(LEFT)
        
        
        start=UP*3#+LEFT
        end=DOWN*3#+LEFT
        line=Line3D(start,end,color=YELLOW)
        dui=Text('对称轴',font='Simsun').next_to(line,UP)
        text1 = Text("11.5.翻折与轴对称图形",font='Simsun').scale(0.8)
        text2 = Text("先画一个任意平面图形",font='Simsun').scale(0.5)
        text3 = Text("再指定一条对称轴",font='Simsun').scale(0.5)
        text4 = Text("于是我们画出了一组轴对称图形",font='Simsun').scale(0.5)
        g=VGroup(text1,text2,text3,text4)
        
>>>>>>> origin/main

        g.arrange(DOWN).to_corner(UL)
        for i in range(2):
            self.add_fixed_in_frame_mobjects(g[i])
            g[i].to_edge(RIGHT)
            self.play(Write(g[i]))
<<<<<<< HEAD
        # self.play(Write(g[0]))
        # self.play(Write(g[1]))
        self.play(Create(half), run_time=3)
        self.play(half.animate.set_fill(BLUE, 1).set_opacity(0.5), run_time=3)
=======
        #self.play(Write(g[0]))
        #self.play(Write(g[1]))
        self.play(Create(half),run_time=3)
        self.play(half.animate.set_fill(BLUE,1).set_opacity(0.5),run_time=3)
>>>>>>> origin/main

        self.add_fixed_in_frame_mobjects(g[2])
        g[2].to_edge(RIGHT)
        self.play(Write(g[2]))

<<<<<<< HEAD
        self.play(Create(line), Create(dui))
        self.move_camera(phi=70 * DEGREES, theta=-75 * DEGREES, run_time=3)

        self.begin_ambient_camera_rotation(rate=-0.1)
        half2 = half.copy()
        self.play(Rotating(half2, axis=UP, about_point=start, radians=PI))
=======
        self.play(Create(line),Create(dui))
        self.move_camera(phi=70 * DEGREES, theta=-75 * DEGREES,run_time=3)
        
        self.begin_ambient_camera_rotation(rate=-0.1)
        half2=half.copy()
        self.play(Rotating(half2,axis=UP,about_point=start,radians=PI))
>>>>>>> origin/main
        self.add_fixed_in_frame_mobjects(g[3])
        g[3].to_edge(RIGHT)
        self.play(Write(g[3]))
        self.wait(2)
        self.stop_ambient_camera_rotation()
<<<<<<< HEAD
        self.move_camera(phi=0, theta=-PI/2, run_time=4)
=======
        self.move_camera(phi=0, theta=-PI/2,run_time=4)
>>>>>>> origin/main
        self.wait(2)
