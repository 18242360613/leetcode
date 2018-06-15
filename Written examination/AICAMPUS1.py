import sys

def getzeronums(x):
    if x==0:
        return 1
    num=0
    while x>0:
        if x%10==0:
            num+=1
        else:
            break
        x=x//10
    return num

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N, M = int(line.split(" ")[0]), int(line.split(" ")[1])
    dp= [[1000000]*M for i in range(N)]
    way = [[[]]*M for i in range(N)]
    value =[[-1]*M for i in range(N)]
    nums = []

    for i in range(N):
        s = sys.stdin.readline().strip().split(" ")
        num = []
        for c in s:
            num.append(int(c,16))
        nums.append(num)

    for i in range(N):
        for j in range(M):
            if i==0 and j ==0:
                value[i][j] = nums[i][j]
                dp[i][j] = getzeronums(value[i][j])
                way[i][j] = ''
            else:
                if i == 0:
                    value[i][j] = value[i][j-1]*nums[i][j]
                    dp[i][j] = getzeronums(value[i][j])
                    way[i][j] = way[i][j-1]+">"
                elif j==0:
                    value[i][j] = value[i-1][j]*nums[i][j]
                    dp[i][j] = getzeronums(value[i][j])
                    way[i][j] = way[i-1][j]+"V"
                else:
                    a = value[i-1][j]*nums[i][j]#row
                    b = value[i][j-1]*nums[i][j]#column prior
                    if getzeronums(a)>getzeronums(b):
                        way[i][j] = way[i][j-1]+">"
                        dp[i][j] = getzeronums(b)
                        value[i][j] = b
                    elif getzeronums(a)<getzeronums(b):
                        way[i][j] = way[i-1][j]+"V"
                        dp[i][j] = getzeronums(a)
                        value[i][j] = a
                    else:
                        way[i][j] = min(way[i - 1][j] + "V",way[i][j-1]+">")
                        dp[i][j] = getzeronums(a)
                        value[i][j] = a

    print(dp[N-1][M-1])
    print(way[N-1][M-1])