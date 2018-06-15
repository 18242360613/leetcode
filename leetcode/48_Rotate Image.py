class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n =len(matrix)
        for i in range(n//2):
            for j in range(n-n//2):
                matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i],matrix[i][j]=\
                matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i]

s = Solution()
ans = s.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(ans)