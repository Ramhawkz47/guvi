def remo(l,n):
    l.sort()
    x=0
    m=[]
    for i in l:
        if(i==x):
            m.append(x)

        x=i
    if((len(m)==n)or(n==2)):
        return(m)
    else:
        #print(m)
        return(remo(m,len(m)))

n= int(input())
l=input()
l=l.split()

for i in range(len(l)):
  l[i]=int(l[i])

m=remo(l,n)
f=0
for i in m:
  if(len(m)>(f+1)):
    print(i,end=" ")
  else:
    print(i,end="")
