x=input()
s=input().split()
s.sort()
s=s[::-1]
n=""
for i in s:
    n+=i

print(int(n))
