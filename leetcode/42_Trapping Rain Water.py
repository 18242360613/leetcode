class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        maxleft,maxright = [0]*len(height),[0]*len(height)
        if len(height)==0: return 0
        maxleft[0],maxright[-1] = height[0],height[-1]

        for i in list(range(1,len(height))):
            maxleft[i] = max(maxleft[i-1],height[i])
        for i in list(range(len(height)-2,-1,-1)):
            maxright[i] = max(maxright[i+1],height[i])

        for i in range(len(height)):
            ans = ans + min(maxleft[i],maxright[i])-height[i]

        return ans

s = Solution()
ans = s.trap([])
print(ans)