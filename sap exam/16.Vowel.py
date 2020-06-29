#16. Vowel

def sam_kumar(sl,nl):
    l,ans=[],[]
    v='aeiou'
    for i in range(len(sl)):
        s=sl[i]
        if s[0] in v and s[len(s)-1] in v:
            l.append(1)
        else:
            l.append(0)
    for i in range(len(nl)):
        n=nl[i]
        a,b=int(n[0]),int(n[2])
        c=0
        for i in range(a-1,b):
            if l[i]==1:
                c+=1
        ans.append(c)
    return ans

n=int(input())
sl,nl=[],[]
for i in range(n):
    s=input()
    sl.append(s)
q=int(input())
for i in range(q):
    s=input()
    nl.append(s)
#print(sl)
#print(nl)
print(sam_kumar(sl,nl))


'''
Example-1:
i/p:
    5
    aab
    a
    bcd
    awe
    bbbbbu
    2
    2-3
    4-5
o/p: [1, 1]

Example -2:
i/p:
    5
    aba
    bcb
    ece
    aa
    e
    3
    1-3
    2-5
    2-2

o/p: [2, 3, 0]

'''
