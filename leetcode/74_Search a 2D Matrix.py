class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l,h,mid = 0,len(matrix),0
        if h==0 or len(matrix[0])==0:return False

        while l<h:
            mid = (l+h)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                break
            elif matrix[mid][0]> target:
                h = mid
            else:
                l= mid+1

        if not(matrix[mid][0]<=target and matrix[mid][-1]>=target): return False

        l,h = 0,len(matrix[mid])
        while l<h:
            t = (l+h)//2
            if matrix[mid][t]==target:
                break
            elif matrix[mid][t]>target:
                h = t
            else:
                l = t+1

        if matrix[mid][t]==target:
            return True
        return False

s = Solution()
ans = s.searchMatrix([[1]],3)
print(ans)