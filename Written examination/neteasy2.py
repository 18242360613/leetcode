import sys
class Solution:
    def nextPermutation(self, nums):
        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i<0:
            nums.reverse()
        else:
            j=i+1
            while j<len(nums) and nums[j]>nums[i]:
                j+=1
            j-=1
            nums[i],nums[j] = nums[j],nums[i]
            nums[i+1:] = sorted(nums[i+1:])

if __name__ == '__main__':
    line = sys.stdin.readline().strip().split(" ")
    n,m,k = int(line[0]),int(line[1]),int(line[2])
    nums = []
    for i in range(n):
        nums.append('a')

    for i in range(m):
        nums.append('z')

    listans = [nums]
    s = Solution()
    ans = set()
    i = 0
    while i < k-1:
        s.nextPermutation(nums)
        value = "".join(nums.copy())
        if value in ans:
            break
        ans.add(value)
        i+=1

    if i==(k-1):
        print("".join(nums))
    else:
        print(-1)
