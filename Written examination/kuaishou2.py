import sys

if __name__ == "__main__":

    while True:
        N = sys.stdin.readline().strip()
        if N == "":
            break
        N = int(N)
        R = 1000000003
        f0,f1,f2,f3,f4 = 1,1,1,1,1
        if N<=4:
            print(1)
        else:
            for i in range(5,N+1):
                tmp = ((2018*f4)%R+(2017*f3)%R+(2016*f2)%R+(2015*f1)%R+(2014*f0)%R)%R
                f4,f3,f2,f1,f0 = tmp,f4,f3,f2,f1
            print(f4)