def f(a,b,c):
    x=y=0
    for i in range(c):
        x = x+a+y
    y = y+b
    return x
print f(-5,2,10)