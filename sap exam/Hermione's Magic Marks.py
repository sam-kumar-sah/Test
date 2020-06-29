#Hermione's Magic Marks

def swap(s):
    a='PEPEEPE'
    c,d=0,0
    for i in range(len(a)):
        if a[i]==s[i]:
            c+=1
        else:
            d+=1
    return (len(a)-d)

def pop(a,k):
    n=k
    while(n):
        a*=k
        n-=1
    return a

t=int(input())
for i in range(t):
    a,k,h=map(int,input().split())
    s=input()

    ans=pop(a,k)
    p=len(str(ans))
    q=len(str(h))
    if p==q:
        print(-1)
    elif p>=q:
        print(0)
    elif p<=q:
        pre=swap(s)
        pp=(h//ans)-1
        print(pre)
