def larS(l):
    x=len(l[0])
    for i in l[1:]:
        if(x>len(i)):
            x=len(i)
    return x

n=int(input())
l=[]
for i in range(n):
    l.append(input())
l.sort()
m=larS(l)
s=""
d={}
for i in range(m):
    for j in range(len(l)):
        try:
            d[l[j][i]]+=1
        except:
            d[l[j][i]]=1

    x=0
    c=""
    for j in d:
        if(d[j]>=x):
            x=d[j]
            c=j
    
    if(x!=n):
        break
    #print(d)
    s+=c
    d={}

print(s)
