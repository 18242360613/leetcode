import sys

if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    N,M = int(line.split(" ")[0]),int(line.split(" ")[1])
    model = set()
    for i in range(N):
        m = sys.stdin.readline().strip()
        model.add(m)

    for i in range(M):
        m = sys.stdin.readline().strip()
        if m not in model:
            print("YES")
            model.add(m)
        else:
            print("NO")
