import collections
class Solution:
    def majorityElement(self, nums):
        return collections.Counter(nums).most_common(1)[0][0]

S = Solution()
ans = S.majorityElement([2,2,1,1,1,2,2])
print(ans)