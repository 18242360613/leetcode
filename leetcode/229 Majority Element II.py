class Solution:
    def majorityElement(self, nums):
        if nums is None:
            return []
        count1,count2,candidate1,candidate2 = 0,0,0,1
        for num in nums:
            if candidate1 == num:
                count1 +=1
            elif candidate2 == num:
                count2 +=1
            elif count1 ==0:
                count1 = 1
                candidate1 = num
            elif count2 == 0:
                count2=1
                candidate2 = num
            else:
                count1 = count1 - 1
                count2 = count2 - 1

        return [ num for num in [candidate1,candidate2] if nums.count(num)> len(nums)//3]

    def majorityElement2(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]


S = Solution()
print(S.majorityElement([1,2,2,3,2,1,1,3]))