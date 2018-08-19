import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    nums = [int(num) for num in  sys.stdin.readline().strip().split(" ")]
    maxdp = [[0]*len(nums) for i in range(len(nums)) ]
    mindp = [[0] * len(nums) for i in range(len(nums))]
    ans = 0

    for i in range(len(nums)):
        for j in list(range(i,len(nums))):
            if i==j:
                maxdp[i][j] = nums[i]
                mindp[i][j] = nums[i]
            else:
                maxdp[i][j] = max(nums[j],maxdp[i][j])
                mindp[i][j] = min(nums[j],mindp[i][j])

    for i in range(len(nums)):
        for j in list(range(i+1,len(nums))):
            ans = ans+(maxdp[i][j]-mindp[i][j])

    print(ans)
