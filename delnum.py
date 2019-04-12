s=input()
s=s.split(" ")
#print(s)
if(int(s[1])==0):
    print(int(s[0]))
else:
    x=s[0][int(s[1]):]
    print(x)
