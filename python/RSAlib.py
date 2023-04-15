def key(ceill=65300, pm=1000, print_=True):
    '''公，通，密'''
    from math import ceil, gcd, sqrt
    from random import randint

    #ceill = int(input('输入值上限：'))

    # 将小于33796302173076的素数加入primes列表
    primes = [2]
    up = ceil(sqrt(ceill)+pm)
    for i in range(3, up, 2):
        for j in range(3, ceil(sqrt(i)+1)):
            if i % j == 0:
                break
        else:
            primes.append(i)

    # p,q,n
    m = len(primes)
    n = 0
    upp = ceill//up#可能是随便设的
    #print(upp, primes)
    while n < ceill:#n must be greater than p*q
        p = primes[randint(upp, m-1)]
        q = primes[randint(upp, m-1)]
        n = p*q
    # fai
    fai = (p-1)*(q-1)
    # e
    for i in range(11, 100, 2):
        if gcd(fai, i) == 1:
            e = i
            break
    # d
    for l in range(fai):
        if (e*l) % fai == 1:
            d = l
            break
    if print_:
        print('公钥：')
        print(e)
        print('通钥：')
        print(n)
        print('密钥：')
        print(d)
    return e, n, d

def lock(a, e=502981, n=1091891):
    '''明文，公/密，通'''
    part = len(str(n))
    b = ''
    for i in a:
        locked = str(pow(ord(i), e, n))
        while len(locked) < part:
            locked = '0'+locked
        b += locked
    return b

def unlock(b, d=13, n=1091891):
    '''密文，密/公，通'''
    part = len(str(n))
    text = ''
    for m in range(int(len(b)/part)):
        text += chr(pow(int(b[part*m:part*(m+1)]), d, n))
    return text

#print(unlock(b=lock()))
'''
e=int(input('公钥:'))
n=int(input('通钥:'))
a=input('需要加密的文本:')
公钥：
11
通钥：
86267
密钥：
77891
公钥：
13
通钥：
1091891
密钥：
502981
公钥：
11
通钥：
3122196587
密钥：
283823531
'''
#key(12345678, 123456)
#print(unlock(lock('hello', 13, 1091891), 502981, 1091891))