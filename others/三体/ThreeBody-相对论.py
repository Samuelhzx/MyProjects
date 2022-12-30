import sys
import pygame as pg
from random import randint as rand

def place(a,b,mlist,listt):
    listplace=0
    for i in range(1,len(listt)+1):
        if abs(listt[-i]-b)<i*c*t:
            listplace=i
            break
    if listplace==0:
        return 0
    else:
        place=listt[-listplace]-a
        return g*mlist[-listplace]/abs(place)**3*place*t
    del listt[0:-listplace-1]
    del mlist[0:-listplace-1]
    
def write(a):
    fontt=font.render(a,True,(255,255,255),(0,0,0))
    global yrect
    rectt=fontt.get_rect()
    rectt.top=yrect
    yrect+=25
    window.blit(fontt,rectt)

def ga(a):
    return (1-abs(a)**2/c**2)**0.5
pg.init()
window=pg.display.set_mode((1200,800),pg.HWSURFACE)
pg.display.set_caption("ThreeBody")
logo=pg.image.load('logo.png')
pg.display.set_icon(logo)
star1 = pg.image.load('blue.png')
star2 = pg.image.load('green.png')
star3 = pg.image.load('red.png')
r1=star1.get_rect()
r2=star2.get_rect()
r3=star3.get_rect()
r1.center=rand(100,1100),rand(100,700)
r2.center=rand(100,600),rand(100,700)
r3.center=rand(600,1100),rand(100,700)

listt1=[]
listt2=[]
listt3=[]
mlist1=[]
mlist2=[]
mlist3=[]
time=0
t=1
c=1
g = 1
m1=1
m2=1
m3=1
v1=0
v2=0.05
v3=-0.05
p1=r1.centerx+r1.centery*1j
p2=r2.centerx+r2.centery*1j
p3=r3.centerx+r3.centery*1j
font=pg.font.Font('euclid.ttf',20)

while True:
    mm1=m1/ga(v1)
    mm2=m2/ga(v2)
    mm3=m3/ga(v3)
    a1=place(p1,p2,mlist2,listt2)+place(p1,p3,mlist3,listt3)
    a2=place(p2,p1,mlist1,listt1)+place(p2,p3,mlist3,listt3)
    a3=place(p3,p1,mlist1,listt1)+place(p3,p2,mlist2,listt2)
    v1+=a1*ga(v1)
    v2+=a2*ga(v2)
    v3+=a3*ga(v3)
    p1+=v1*t
    p2+=v2*t
    p3+=v3*t
    listt1.append(p1)
    listt2.append(p2)
    listt3.append(p3)
    mlist1.append(mm1)
    mlist2.append(mm2)
    mlist3.append(mm3)
    yrect=1
    write('blue:'+str(round(abs(v1)/c,5))+'c')
    write('green:'+str(round(abs(v2)/c,5))+'c')
    write('red:'+str(round(abs(v3)/c,5))+'c')
    write('time:'+str(time))
    r1.center=p1.real,p1.imag
    r2.center=p2.real,p2.imag
    r3.center=p3.real,p3.imag
    #window.fill((0,0,0))
    window.blit(star1,r1)
    window.blit(star2,r2)
    window.blit(star3,r3)
    time+=1
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()