import sys

if __name__ == "__main__":
    while True:
        N = sys.stdin.readline().strip()
        if N == "":
            break
        N = int(N)
        dp = [0]*(N+1)
        dp[1],dp[2],dp[3],dp[4],dp[5] = 0,0,1,1,2
        for i in list(xrange(6,N+1)):
            dp[i] =dp[int((i+1)/2)]+1
        print dp[N]