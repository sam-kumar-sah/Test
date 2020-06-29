#deleting substring

def maxMoves(s,t):
    c=0
    for i in s:
        if i in t:
            c+=1
    print(c//len(t))

if __name__=='__main__':
    s=input()
    t=input()
    maxMoves(s, t)
