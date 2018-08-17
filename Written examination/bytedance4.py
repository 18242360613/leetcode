import sys

class Line:
    def __init__(self,start,end):
        self.start = start
        self.end = end

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip().split(" ")
    lines = []
    for i in range(N):
        s = int(line[2*i])
        e = int(line[2*i+1])
        if s > e:
            e = M+e
        lines.append(Line(s,e))
    lines.sort(key=lambda x:x.end)
    res,last = 0,-1
    for i in range(N):
        if lines[i].start >= last and lines[i].end<=M:
            res+=1
            last = lines[i].end

    print(res)