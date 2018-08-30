import sys
if __name__ == '__main__':
    M = int(sys.stdin.readline().strip())
    x,y = [],[]
    for i in range(M):
        s = sys.stdin.readline().strip()
        m,n = int(s.split(" ")[0]), int(s.split(" ")[1])
        x.append(m)
        y.append(n)

    maxx,minx = max(x),min(x)
    maxy,miny = max(y),min(y)

    print(abs((int(maxx-minx))*(int(maxy-miny))))