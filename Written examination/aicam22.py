import sys

if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    N,M = int(line.split(" ")[0]),int(line.split(" ")[1])
    nums=[]
    for i in range(N):
        t = int(sys.stdin.readline().strip())
        nums.append(t/M)

    ans = 0
    for i in range(N):
        for j in list(range(i+1,N)):
            ans=ans+int(abs(nums[i]-nums[j]))
    print(ans)