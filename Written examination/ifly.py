import sys

def dfs(idx,cur,n,total,ts,sugs):
    global mind
    global mins
    if cur==n//2 and abs(ts - total)<mind:
        mind = abs(ts - total)
        mins = total
        return

    if idx==n:return
    dfs(idx+1,cur+1,n,total+sugs[idx],ts,sugs)
    dfs(idx+1,cur,n,total,ts,sugs)

mins = 0
mind = 100000000
while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    N = int(line.split(" ")[0])
    sugs = [int(s) for s in line.split(" ")[1:]]
    mins,mind = 0,10000000
    dfs(0, 0, N, 0, sum(sugs) / 2, sugs)

    print("%d %d"%(min(sum(sugs)-mins,mins),max(sum(sugs)-mins,mins)))