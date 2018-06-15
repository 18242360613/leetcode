class Solution:
    def threeSum(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        sums=[]
        for i in range(length-2):
            low,high =i+1,length-1
            sumt = target - nums[i]
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
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        sums=[]
        for i in range(length-3):
            if (i==0) or (i > 0 and nums[i]!=nums[i-1]):
                tmpsum = self.threeSum(nums[i+1:],target - nums[i])
                for ts in tmpsum:
                    sums.append([nums[i]]+ts)
        return sums
                    
        
        
        