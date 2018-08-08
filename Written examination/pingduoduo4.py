import sys

def lengthOfLIS(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

if __name__ == '__main__':
    N = sys.stdin.readline().strip()
    nums = [int(num) for num in sys.stdin.readline().strip().split(' ')]
    ans = lengthOfLIS(nums)
    print(min(ans,len(nums)-ans))