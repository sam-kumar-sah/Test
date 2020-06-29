i/p: 5
o/p:
	*****
	~~~~~~*
	~~~~~~~*
	~~~~~~~~*
	~~~~~~~~~*
	~~~~~~~~~~*
	~~~~~~~~~*
	~~~~~~~~*
	~~~~~~~*
	******
	
#solution:

nn=int(input())
n=(nn-1)//2

print('*'*nn)
for i in range(n):
    for j in range(n):
        nn=nn+1
        print('~'*nn+'*')
print('~'*(nn+1)+'*')
p=nn
for i in range(n,-1,-1):
    for j in range(i):
        print('~'*p+'*')
        p = p - 1
print('*'*p)
