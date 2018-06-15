class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        sums=[]
        for i in range(length-2):
            low,high =i+1,length-1
            sumt = 0 - nums[i]
            if (i==0) or (i > 0 and nums[i]!=nums[i-1]):
                while low < high:
                    if nums[low]+nums[high]==sumt:
                        sums.append([nums[i],nums[low],nums[high]])
                        while (low < high) and (nums[low]==nums[low+1]):
                            low+=1
                        while (low < high) and (nums[high]==nums[high-1]):
                            high-=1
                        low+=1
                        high-=1
                    elif nums[low]+nums[high] < sumt:
                            low+=1
                    else:
                            high-=1
        return sums