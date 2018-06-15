import sys
import math

def funct(x):
    divisor = 2
    result = []
    while x!= 1:
        if x % divisor == 0:
            x = x / divisor
            result.append(divisor)
            divisor = 2
        else :
            divisor =divisor + 1
    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        M = int(sys.stdin.readline().strip())
        factor = funct(M)
        success = False
        if factor[0]!=2:
            print("No")
        else:
            fac = 1
            for j in list(range(1,len(factor))):
                if factor[j]%2 ==1:
                    fac = fac*factor[j]
            print("%d %d"%(fac,M//fac))