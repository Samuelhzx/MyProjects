from random import randint

def one():
    roundd=1
    pick=0
    while pick!=1:
        roundd+=1
        pick=randint(1,roundd)
    return roundd

def a():
    num=0
    for i in range(10000):
        num+=one()
    print(num/10000)
a()