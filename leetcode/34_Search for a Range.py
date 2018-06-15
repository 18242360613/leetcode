class Solution:

    def searchleft(self, nums, target):
        l,h = 0,len(nums)-1
        while l<h:
            mid = (l+h)//2
            if nums[mid] < target:
                l = mid+1
            else:
                h = mid
        if nums[l]==target:return l
        return -1

    def searchright(self, nums, target,L):
        l,h = L,len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                l = mid+1
            else:
                h = mid-1
        return h

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:return [-1,-1]
        l=self.searchleft(nums,target)
        if l==-1:
            return [-1,-1]
        return [l,self.searchright(nums,target,l)]

s = Solution()
result = s.searchRange([5,7,7,8,8,10],7)
print(result)