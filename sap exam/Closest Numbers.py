#17. Closest Numbers
'''
i/p: 4
     4 2 1 3
o/p: 1 2
     2 3
     3 4
'''
def closestNumbers(numbers):
    l=numbers
    n=len(l)
    def sam(l,n):
        a=[]
        for i in range(len(l)):
            x = l[i]
            for j in range(i + 1, n):
                y = (abs(x - l[j]))
                a.append(y)
        return min(a)
    ans=sam(l,n)

    b=[]
    for i in range(len(l)):
       x=l[i]
       for j in range(i+1,n):
           y=(abs(x-l[j]))
           if y==ans:
               if x<l[j]:
                   b.append((x,l[j]))
               else:
                   b.append((l[j],x))
    b.sort()
    for i in b:
        print(*i,end='\n')

if __name__=='__main__':
    n = int(input())
    numbers= list(map(int, input().split()[:n]))
    closestNumbers(numbers)
