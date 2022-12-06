import sys
s=input()
i = 0
n=4
while len(set(s[i:i+n])) != n: i+= 1
print(i+n)

n=14
while len(set(s[i:i+n])) != n: i+= 1
print(i+n)
