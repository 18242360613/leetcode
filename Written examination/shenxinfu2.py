import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    order = []
    oset = set()
    for i in range(N):
        id = int(sys.stdin.readline().strip())
        if id not in oset:
            oset.add(id)
            order.append(id)

    length = min(len(order),10)
    print(length)
    for i in range(length):
        print(order[i])