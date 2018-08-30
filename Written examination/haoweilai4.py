import sys
if __name__ == '__main__':
    line = sys.stdin.readline().strip().split()
    n,m = int(line[0]),int(line[1])
    scores = [int(s) for s in sys.stdin.readline().strip().split()]
    avgs = sum(scores)/n
    totalacore,t,p = 0,1,m/n
    while t*avgs > 0.001:
        totalacore += t*avgs
        t = t * p
    print("%.2f" % totalacore )