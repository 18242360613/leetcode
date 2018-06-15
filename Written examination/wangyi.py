import sys

if __name__ == "__main__":

    while True:
        N = sys.stdin.readline().strip()
        if N == "":
            break
        N = int(N)
        clocks = []
        for i in range(N):
            s = sys.stdin.readline().strip().split(" ")
            h,m= int(s[0]),int(s[1])
            clocks.append([h,m])
        clocks.sort(reverse=True)
        needtime = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip().split(" ")
        rh,rm = int(s[0]),int(s[1])
        lasth,lastm = 0,0
        if rm >= needtime:
            lasth, lastm = rh,rm-needtime
        elif rm+60 >= needtime:
            lasth, lastm = rh-1, rm - needtime+60
        else:
            lasth, lastm = rh - 2, rm - needtime + 120

        i = 0
        while i<N:
            if clocks[i]<=[lasth,lastm]:
                break
            i+=1
        print("%d %d"%(clocks[i][0],clocks[i][1]))