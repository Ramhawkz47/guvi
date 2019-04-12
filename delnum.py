def deln(n,k):
    if((n==0)or(k==0)):
        return n
    #print(n)
    #print(k)
    a=deln(n//10,k)*10+n%10
    b=deln(n//10,k-1)
    #print(a)
    #print(b)
    if a<b:
        return a
    else:
        return b

s=input()
s=s.split(" ")
print(deln(int(s[0]),int(s[1])))
