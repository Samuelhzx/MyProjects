'''
九头蛇游戏，一个可以用来创造大数的小游戏
总体思路是删除指定括号，然后按规则补上
好久以前写的，没几个注释，我自己都快看不懂了。。。
不过能跑就行
玩法：输入数字，表示删去从左往右第几个括号
'''

<<<<<<< HEAD
from random import randint


def list_to_str(listt):  # list转换成str
    final = None
    for j in listt:
        if final == None:
            final = j
        else:
            final += j
    return final


def delete(string, times):
    a = 1
    num = 0
    for i in range(len(zifu)):
        if zifu[i] == '(':
            a = 1
        else:
            if a == 1:  # is a smallest 括号
                num += 1
                if num == string:
                    new = list(zifu)

                    def sec(x, ii):
                        b = 0  # b用来判断括号
                        while b != x:
                            ii -= x
                            if new[ii] == '(':
                                b += 1
                            else:
                                b -= 1
                        return ii
                    iii = i-1
                    start = sec(1, iii)
                    iii = i
                    end = sec(-1, iii)-2
                    del new[i-1:i+1]
                    if start != 0:
                        secon = new[start:end+1]
                        # print(start,end)
                        # print(secon)
                        for k in range(times):
                            for m in range(1, len(secon)+1):
                                new.insert(end+1+k*len(secon), secon[-m])

                    return list_to_str(new)
            a = -1


def ceng(zifuu):  # 检测括号的层数
    cou = 0
    for n in zifuu:
        if n == '(':
            cou += 1
        else:
            cou -= 1
        if cou == 3:
            return False
    return True


times = 1

zifu = []
while ceng(zifu) and (len(zifu) > 10 or len(zifu) < 6):  # 这里是随机生成一个开始
    zifu = list(zifu)
    zifu.insert(randint(0, len(zifu)), '()')
    zifu = list_to_str(zifu)
zifu = '('+zifu+')'

while zifu != '()':  # 主程序
    print(zifu)
    string = int(input())
    zifu = delete(string, times)
    times += 1
print('()\nYou Win!')
=======
def list_to_str(listt):#list转换成str
    final=None
    for j in listt:
        if final==None:
            final=j
        else:
            final+=j
    return final
def delete(string,times):
    a=1
    num=0
    for i in range(len(zifu)):
        if zifu[i]=='(':
            a=1
        else:
            if a==1:#is a smallest 括号
                num+=1
                if num==string:
                    new=list(zifu)

                    def sec(x,ii):
                        b=0#b用来判断括号
                        while b!=x:
                            ii-=x
                            if new[ii]=='(':
                                b+=1
                            else:
                                b-=1
                        return ii
                    iii=i-1
                    start=sec(1,iii)
                    iii=i
                    end=sec(-1,iii)-2
                    del new[i-1:i+1]
                    if start!=0:
                        secon=new[start:end+1]
                        #print(start,end)
                        #print(secon)
                        for k in range(times):
                            for m in range(1,len(secon)+1):
                                new.insert(end+1+k*len(secon),secon[-m])
                        
                    return list_to_str(new)
            a=-1
def ceng(zifuu):#检测括号的层数
    cou=0
    for n in zifuu:
        if n=='(':
            cou+=1
        else:
            cou-=1
        if cou==3:
            return False
    return True
times=1
from random import randint

zifu=[]
while ceng(zifu) and (len(zifu)>10 or len(zifu)<6):#这里是随机生成一个开始
    zifu=list(zifu)
    zifu.insert(randint(0,len(zifu)),'()')
    zifu=list_to_str(zifu)
zifu='('+zifu+')'

while zifu!='()':#主程序
    print(zifu)
    string=int(input())
    zifu=delete(string,times)
    times+=1
print('()\nYou Win!')
>>>>>>> origin/main
