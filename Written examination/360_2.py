import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    m,n = int(line.split(" ")[0]),int(line.split(" ")[1])
    flowers = [int(num) for num in sys.stdin.readline().strip().split()]
    Q_num = int(sys.stdin.readline().strip())
    for i in range(Q_num):
        s = sys.stdin.readline().strip()
        m,n = int(s.split(" ")[0]), int(s.split(" ")[1])
        fs = set(flowers[m-1:n])
        print(len(fs))

