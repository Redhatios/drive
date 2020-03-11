from itertools import permutations
import re
x = input()
x1 = set(x)
x1 = list(x1)
s=""
xz=[]
l=[]
for i in x2:
    s += i
final = permutations(s,len(x2))
z = (list(final))
count=0
for i in z:
    s=""
    for j in i:
        s+=j
        count+=1
        if(count!=len(x2)):
            s+='[a-z]*'  
    #print(s)
    count = 0
    g=re.findall(s,x)
    if(g !=[]):
        l.append(g)
print(l)
for i in l:
    for j in i:
        xz.append(len(j))
print(min(xz))
    
