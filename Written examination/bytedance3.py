import sys

if __name__ == '__main__':
    pscore,tscore = [],[]
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        line = sys.stdin.readline().strip()
        pscore.append(int(line[0]))
        tscore.append(int(line[1]))
