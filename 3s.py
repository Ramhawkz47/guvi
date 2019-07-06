x,y=input().split()
m=len(x)
n=len(y)
if ((n<m)or(n==m)):
    i=0
    while i<m and x[i]==y[i]:
        i+=1
    print(((n+i)**2)-(i+1))
else:
    i=0
    while i<n and x[i]==y[i]:
        i+=1
    a=x[i:]
    b=y[i:]
    l=list(a)
    #print(l)
    j=0
    for c in b:
        if c in l:
            j+=1
            l.remove(c)
    print(((m+i+j)*2)+(m+i))
