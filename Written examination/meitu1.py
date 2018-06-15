import sys
from itertools import permutations
while True:
    line = sys.stdin.readline().strip().split(" ")
    if line=="":
        break
    N = int(line[0])
    K = int(line[1])
    a = len(list(permutations([i for i in range(N)], K)))
    print a%772235