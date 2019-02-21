import math

class Solution:
    def maximumGap(self, nums: 'List[int]') -> 'int':

        if len(nums)==0 or len(nums)==1:
            return 0

        length = len(nums)
        maxval,minval = max(nums),min(nums)
        gap = math.ceil((maxval-minval)/(length-1))
        if gap ==0:
            return 0

        minbucket,maxbucket = [float("inf")]*(length),[float("-inf")]*(length)

        for val in nums:
            # if val == maxval or  val == minval:
            #     continue

            index = (val - minval)//gap
            minbucket[index] = min(minbucket[index],val)
            maxbucket[index] = max(maxbucket[index],val)

        maxgap,pre = 0,minval
        for i in range(len(minbucket)):
            if minbucket[i] == float("inf") or maxbucket[i]==float("-inf"):
                continue

            maxgap = max(maxgap,minbucket[i]-pre)
            pre = maxbucket[i]

        # maxgap = max(maxgap,maxval-pre)

        return maxgap

s = Solution()
print(s.maximumGap([1,10]))