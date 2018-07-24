class Solution:
    def search(self, nums, target):
        l, h = 0, len(nums)
        while l < h:
            mid = (l + h) // 2
            if nums[mid] == target: return True

            if (nums[mid]==nums[l]) and (nums[mid]==nums[h-1]):
                l,h = l+1,h-1
            else:
                if nums[mid] >= nums[l]:
                    if nums[mid] > target and target >= nums[l]:
                        h = mid
                    else:
                        l = mid + 1
                else:
                    if nums[h - 1] >= target and target > nums[mid]:
                        l = mid + 1
                    else:
                        h = mid
        return False

s = Solution()
ans = s.search([1,3,1,1],3)
print(ans)


