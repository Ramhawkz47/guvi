n= int(input())
l=input()
l=l.split()

for i in range(len(l)):
  l[i]=int(l[i])

l.sort()
x=0
m=[]
for i in l:
  if(i==x):
    m.append(x)
  x=i
for i in m:
  print(i,end=" ")
