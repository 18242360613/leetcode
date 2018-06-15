#coding=utf-8
import sys

if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().strip()
        if line=="":
            break
        n1,n2,m = int(line.split(" ")[0]),int(line.split(" ")[1]),int(line.split(" ")[2])
        nc = [int(a) for a in sys.stdin.readline().strip().split(" ")]
        sc = [int(a) for a in sys.stdin.readline().strip().split(" ")]
        coin = []
        for c in nc:
            i = 0
            while (c*2**i)<= m:
                coin.append(c*2**i)
                i=i+1

        for c in sc:
            coin.append(c)

        coin.sort()
        length = len(coin)
        dp = [0]*(m+1)
        dp[0] = 1
        for i in range(length):
            for j in list(range(m,coin[i]-1,-1)):
                dp[j] += dp[j - coin[i]];
        print(dp[m])