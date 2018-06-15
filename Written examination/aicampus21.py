import sys

def maxSubArray(nums):
    length = len(nums)
    cursum = nums[0]
    maxsum = nums[0]
    k = 0
    for i in list(range(1, length)):

        if nums[i] == 0:
            k += 1

        if cursum<0 or k>3:
            k=0
            cursum = nums[i]
            if nums[i]==0:
                k=1
        else:
            cursum = cursum+nums[i]

        if maxsum<cursum and k<=3:
            maxsum = cursum

    return maxsum

# if __name__ == "__main__":
#     N = sys.stdin.readline().strip()
#     line = sys.stdin.readline().strip().split(" ")
#     nums = [int(num) for num in line ]
#     ans = maxSubArray(nums)
#     print(ans)

print(maxSubArray([-5,0,-1,-1,-1,-8]))