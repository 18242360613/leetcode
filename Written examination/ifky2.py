import time
import sys
start=time.clock()
i=input('please enter  an integer:')
r=list()
r.append(2)
for a in range(3,i):
    b=False
    for b in r:
        if a%b==0:
            b=False
            break
        else:
            b=True
    if b==True:
        r.append(a)


print(r)
t=(time.clock()-start)
print(t)

