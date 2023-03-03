import sys
import pygame as pg
from random import randint as rand


def write(a):
    fontt = font.render(a, True, (255, 255, 255), (0, 0, 0))
    global yrect
    rectt = fontt.get_rect()
    rectt.top = yrect
    yrect += 22
    window.blit(fontt, rectt)


def f(a, b, m):
    return g * m / abs(b - a) ** 3 * (b - a) * t


pg.init()
window = pg.display.set_mode((1200, 800))  # ,pg.RESIZABLE)
pg.display.set_caption("ThreeBody")
logo = pg.image.load("logo.png")
pg.display.set_icon(logo)
star1 = pg.image.load("blue.png")
star2 = pg.image.load("green.png")
star3 = pg.image.load("red.png")
star4 = star1
star5 = star2
star6 = star3
r1 = star1.get_rect()
r2 = star2.get_rect()
r3 = star3.get_rect()
r4 = star4.get_rect()
r5 = star5.get_rect()
r6 = star6.get_rect()
r1.center = rand(100, 1100), rand(100, 700)
r2.center = rand(100, 600), rand(100, 400)
r3.center = rand(600, 1100), rand(400, 700)
t = 0.004
g = 1.5
m1 = 1
m2 = 1
m3 = 1
v1 = 0
v2 = 0.05
v3 = -0.05
v4 = 0
v5 = 0.05
v6 = -0.05
timee = 0
p1 = r1.centerx + r1.centery * 1j
p2 = r2.centerx + r2.centery * 1j
p3 = r3.centerx + r3.centery * 1j
p4 = r1.centerx + r1.centery * 1j + 1
p5 = r2.centerx + r2.centery * 1j
p6 = r3.centerx + r3.centery * 1j
font = pg.font.Font("euclid.ttf", 20)

while True:
    for i in range(1000):
        v1 += f(p1, p2, m2) + f(p1, p3, m3)
        v2 += f(p2, p1, m1) + f(p2, p3, m3)
        v3 += f(p3, p1, m1) + f(p3, p2, m2)
        p1 += v1 * t
        p2 += v2 * t
        p3 += v3 * t
        v4 += f(p4, p5, m2) + f(p4, p6, m3)
        v5 += f(p5, p4, m1) + f(p5, p6, m3)
        v6 += f(p6, p4, m1) + f(p6, p5, m2)
        p4 += v4 * t
        p5 += v5 * t
        p6 += v6 * t
    # window.fill((0,0,0))
    yrect = 0
    write("time:" + str(abs(timee)))
    write("blue:" + str(abs(v1)))
    write("green:" + str(abs(v2)))
    write("red:" + str(abs(v3)))
    r1.center = p1.real, p1.imag
    r2.center = p2.real, p2.imag
    r3.center = p3.real, p3.imag
    window.blit(star1, r1)
    window.blit(star2, r2)
    window.blit(star3, r3)
    r4.center = p4.real, p4.imag
    r5.center = p5.real, p5.imag
    r6.center = p6.real, p6.imag
    window.blit(star4, r4)
    window.blit(star5, r5)
    window.blit(star6, r6)
    timee += 1
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
