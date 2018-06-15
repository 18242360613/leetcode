import sys

if __name__ == "__main__":
    while True:
        N = sys.stdin.readline().strip()
        if N == "":
            break
        N = int(N)
        light ={}
        for i in xrange(N):
            line = sys.stdin.readline().strip().split(" ")
            for j in line[1:]:
                light[int(j)] = int(line[0])
        print len(light.keys())