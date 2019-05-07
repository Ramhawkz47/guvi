x=input()
s=input().split()
l=[]
for i in range(len(s)):
    if((i==int(s[i]))):
        l.append(i)
if(len(l)==0):
    l.append(-1)

for i in range(len(l)):
    if(i<len(l)-1):
        print(l[i],end=" ")
    else:
        print(l[i],end="")
