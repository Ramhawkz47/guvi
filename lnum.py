x=input()
s=input().split()
s.sort()
l=[]
d={}
for i in range(len(s)):
    s[i]=int(s[i])
#print(s)
for i in s:
    try:
        d[i]+=1
    except:
        d[i]=1
#print(d)
for i in d:
    if(d[i]==1):
        l.append(i)

if(len(l)==0):
    l.append(-1)

for i in range(len(l)):
    if(i<len(l)-1):
        print(l[i],end=" ")
    else:
        print(l[i],end="")
