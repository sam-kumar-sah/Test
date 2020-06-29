def newPassword(a,b):
    m, n= len(a), len(b)
    s=""
    if m<=n:
        for i in range(m):
            s+=a[i]
            s+=b[i]
        for i in range(m, n):
            s += b[i]

    elif n<m:
        for i in range(n):
            s+=a[i]
            s+=b[i]
        for i in range(n, m):
            s += a[i]
    return s

a=input()
b=input()
print(newPassword(a,b))
