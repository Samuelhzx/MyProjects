from math import *
from sympy import Ei
import numpy as np
import matplotlib.pyplot as plt


def O(x):
    num = np.linspace(x, x + 10, 1000)
    summ = 0
    for i in num:
        summ += 1 / i / (i * i - 1) / log(i)
    return summ / 100


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
        a = 6 - a
    return primes


def zeta(s):  # zeta_function_from_Havil_2003
    """
    |             1        ∞      1       n              n
    |  ζ(s) = --------- *  Σ   ------- *  Σ   (-1)^k * (   ) * (k+1)^(-s)
    |         1-2^(1-s)   n=0  2^(n+1)   k=0             k
    """
    E = 1e-10
    res = 0 + 0j
    n = -1
    while True:
        n += 1
        kk = 0 + 0j

        comb = 1
        for k in range(n + 1):

            kk += comb * (k + 1) ** -s
            comb *= (k - n) / (k + 1)

        kk *= 2 ** -(n + 1)
        res += kk

        if abs(kk) < E:
            # print(n)
            break
    return res / (1 - 2 ** (1 - s))


def zeta2(s, t):  # slow
    def euler(n):
        return cos(log(n)*s)+1j*sin(log(n)*s)
    result = 0
    a = 1
    for n in range(1, 4000):
        result += a/euler(n)/n**t
        a = -a
    result = result/(1-2/2**t/euler(2))
    return result


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


def zeros():
    x = np.linspace(14, 50, 100000)
    zero = [0]
    for i in x:
        if abs(zeta(0.5 + 1j * i)) < 0.001:
            if i - zero[-1] > 0.01:
                zero.append(i)
                print(i)
    del zero[0]
    return zero


primes = f(10000)


def int_factorization(a):  # 分解质因数
    zhi = []
    while a != 1:
        for i in primes:
            if a % i == 0:
                a = a / i
                zhi.append(i)
            if i > a:
                break
    return zhi


def u(n):
    if n == 1:
        return 1
    for i in primes:
        if i * i > n:
            break
        elif n % (i * i) == 0:
            return 0
    zhi = int_factorization(n)
    return (-1) ** len(zhi)


def readzeros():
    with open("zero_points_from_@vivek3141.txt", "r") as zeros:
        zero = zeros.readlines()
        for i in range(len(zero)):
            zero[i] = float(zero[i])
    return zero


def PI(x):
    result = Ei(np.log(x)) - log(2) + O(x)
    zeros = readzeros() ####################################################################
    for i in zeros:
        result -= Ei(log(x) * (0.5 + i * 1j)) + Ei(log(x) * (0.5 - i * 1j))
    return result# + O(x)


def pi_(x):#数学上的最后一步
    prim = 0
    for n in range(1, max(4, ceil(log2(x)))):
        prim += u(n) / n * PI(x ** (1 / n))
    return prim


def Ei2(x):
    step = int(10000*abs(x))
    EI_ZERO_PPOINT = 0.372507410781367
    num = np.linspace(EI_ZERO_PPOINT, x, step)
    summ = 0
    for i in num:
        summ += e**i/i
    return summ*(x - EI_ZERO_PPOINT)/step
print(Ei2(3+5*1j))

def Ei3(x):
    def ln(x):
        return log(abs(x))+atan2(x.imag, x.real)*1j
    val = 0.577+ln(x)
    for k in range(1, 120):
        val += x**k/(k*factorial(k))
    return val


def li(x):
    num = np.linspace(2, x, 1000)
    summ = 0
    for i in num:
        summ += 1/log(i)
    return summ*(x-2)/1000+1.045


def calc_riemann_fitting(top=20, times=50):
    x = np.linspace(2, top, times) #####################################################
    y = []
    z = []
    lin = 0
    for i in x:
        while primes[lin] < i:
            lin += 1
        y.append(lin)
        z.append(pi_(i))
        print(z[-1])
    return x, y, z


def plotting(x, y, z):
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()


def display_calc_riemann_fitting():
    plotting(*calc_riemann_fitting())


def read(name, encoding='utf-8'):
    with open(name,"r",encoding=encoding) as us:
        return us.readlines()
    



#if __name__ == "__main__":
#    display_calc_riemann_fitting()