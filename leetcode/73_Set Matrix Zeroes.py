class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row,col = len(matrix),len(matrix[0])
        fr,fc = False,False

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    if i==0: fr = True
                    if j==0: fc = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j] = 0

        if fr:
            for j in range(col):
                matrix[0][j] = 0

        if fc:
            for i in range(row):
                matrix[i][0] = 0

S = Solution()
matrix = [[1,0,3]]
S.setZeroes(matrix)
print(matrix)