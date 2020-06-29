#3.Prime Fibonacci

#solution-1:
def fibb(a,b,n):
    l=[]
    l.append(a)
    l.append(b)
    for i in range(n-2):
        c=a+b
        l.append(c)
        a,b=b,c
    return l[-1]

import sympy
a,b=map(int,input().split())
l=list(sympy.primerange(a,b))
comb=[int(str(i)+str(j)) for i in l for j in l if i!=j and sympy.isprime(int(str(i)+str(j)))]
c=list(set(comb))
x,y=min(c),max(c)
ct=len(c)
print(fibb(x,y,ct))

#solution-2:
import math
def fib(a,b,n):
    l=[]
    l.append(a)
    l.append(b)
    for i in range(n-2):
        c=a+b
        a,b=b,c
        l.append(c)
    return l[-1]

def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

a,b=map(int,input().split())
d=[]
for i in range(a,b+1):
    if prime(i):
        d.append(i)
print('d=',d)

comb=[int(str(i)+str(j)) for i in d for j in d if i!=j and prime(int(str(i)+str(j)))]
c=list(set(comb))
a,b=min(c),max(c)
ct=len(c)
print(a,b,ct)
print('ans=',fib(a,b,ct))
