import sys

if __name__ == "__main__":
    while True:
        N = sys.stdin.readline().strip()
        if N == "":
            break
        N = int(N)
        maxa = [0]*10000
        maxa[0:5] = [1,1,1,2,4]
        def maxmul(n):
            if maxa[n]!=0:
                return maxa[n]
            tm=-1
            for i in range(2, n):
                tm = max(tm,(n-i)*maxmul(i))
            maxa[n] = tm
            return tm
        maxans = 0
        for i in range(N):
            maxans = max(maxans,(N-i)*maxmul(i))
        print(maxans)