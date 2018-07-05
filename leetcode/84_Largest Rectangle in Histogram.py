class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        maxarea,i,length,stack = 0,0,len(heights),[]
        while i<length:
            h = heights[i]
            if len(stack)==0 or h >= heights[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                tp = stack.pop()
                if len(stack)==0:
                    w = i
                else:
                    w = i-1-stack[-1]
                maxarea = max(maxarea,heights[tp]*w)
        return maxarea

s = Solution()
maxarea = s.largestRectangleArea([2,1,5,6,2,3])
print(maxarea)