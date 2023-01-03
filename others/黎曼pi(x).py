from math import *
from sympy import Ei
import numpy as np
import matplotlib.pyplot as plt
print('程序预备中……')

'''
如果没有sympy的话这几个也能用，不过慢
def Ei2(x):
    num=np.linspace(0.3725,x,100*int(abs(x)))
    summ=0
    for i in num:
        summ+=e**i/i
    return summ*(x-0.3725)/100/int(abs(x))

def Ei3(x):
    def ln(x):
        return log(abs(x))+atan2(x.imag,x.real)*1j
    val=0.577+ln(x)
    for k in range(1,120):
        val+=x**k/(k*factorial(k))
    return val

def li(x):
    num=np.linspace(2,x,1000)
    summ=0
    for i in num:
        summ+=1/log(i)
    return summ*(x-2)/1000+1.045

def zero_points(up):
    def zeta(s,t):
        def euler(n):
            return cos(log(n)*s)+1j*sin(log(n)*s)
        result=0
        a=1
        for n in range(1,4000):
            result+=a/euler(n)/n**t
            a=-a
        result=result/(1-2/2**t/euler(2))
        return result
    x=np.linspace(100,up,30*(up-14))
    zero=[0]
    for i in x:
        if abs(zeta(i))<0.03:
            if i-zero[-1]>0.3:
                zero.append(i)
                print(i)
    del zero[0]
    return zero

'''


def O(x):
    num = np.linspace(x, x+10, 1000)
    summ = 0
    for i in num:
        summ += 1/i/(i*i-1)/log(i)
    return summ/100


def f(b):  # 计算素数，由于计算量不大，就不用米勒拉宾算法了
    a = 2
    i = 23
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    while len(primes) < b:
        n = 1
        pn = 0
        while pn**2 < i:
            pn = primes[n]
            if i % pn == 0:
                break
            n += 1
        if pn**2 > i:
            primes.append(i)
        i += a
        a = 6-a
    return primes


def zeta(s):                  # zeta_function_from_Havil_2003
    '''
    |             1        ∞      1       n              n
    |  ζ(s) = --------- *  Σ   ------- *  Σ   (-1)^k * (   ) * (k+1)^(-s)
    |         1-2^(1-s)   n=0  2^(n+1)   k=0             k
    '''
    E = 1e-10
    res = 0+0j
    n = -1
    while True:
        n += 1
        kk = 0+0j

        comb = 1
        for k in range(n+1):

            kk += comb * (k+1) ** -s
            comb *= (k-n) / (k+1)

        kk *= 2 ** - (n+1)
        res += kk

        if abs(kk) < E:
            # print(n)
            break
    return res / (1 - 2 ** (1-s))


def zeros():
    x = np.linspace(14, 50, 100000)
    zero = [0]
    for i in x:
        if abs(zeta(0.5+1j*i)) < 0.001:
            if i-zero[-1] > 0.01:
                zero.append(i)
                print(i)
    del zero[0]
    return zero


def fenjie(a):  # 分解质因数
    zhi = []
    while a != 1:
        for i in primes:
            if a % i == 0:
                a = a/i
                zhi.append(i)
            if i > a:
                break
    return zhi


def u(n):
    if n == 1:
        return 1
    for i in primes:
        if i*i > n:
            break
        elif n % (i*i) == 0:
            return 0
    zhi = fenjie(n)
    return (-1)**len(zhi)


def PI(x):
    result = Ei(np.log(x))-log(2)+O(x)

    for i in zero:
        k = float(i)
        result -= Ei(log(x)*(0.5+k*1j))+Ei(log(x)*(0.5-k*1j))
    return result+O(x)


def pi(x):
    prim = 0
    for n in range(1, floor(10)):
        prim += u(n)/n*PI(x**(1/n))
    return prim


print('程序准备就绪')
primes = f(10000)

zero = zeros()
'''[14.1,21,25,30.4,32.94,37.57,40.91,48.01,49.78,52.98,56.44,59.35,
60.81,65.11,67.08,69.55,75.69,77.15,84.72,87.42,92.49,94.63,95.86,98.83]
#zero_points(1000)'''
'''
zeros= open("zerosb.txt","r")
zero = zeros.readlines()
zeros.close()
'''
x = np.linspace(2, 15, 29)
y = []
z = []
lin = 0
for i in x:
    while primes[lin] < i:
        lin += 1
    y.append(lin)
    z.append(pi(i))
plt.plot(x, y)
plt.plot(x, z)
plt.show()
