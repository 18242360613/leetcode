class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return matrix
        h, w = len(matrix), len(matrix[0])
        mask = [[10000] * w for i in range(h)]
        for i in range(h):
            for j in range(w):
                if matrix[i][j] != 0:
                    mask[i][j] = min(mask[i][j], mask[i - 1][j] + 1, mask[i][j - 1] + 1)
                else:
                    mask[i][j] = 0
        for i in range(h - 1, -1, -1):
            for j in range(w - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i < h - 1:
                        mask[i][j] = min(mask[i][j], mask[i + 1][j] + 1)
                    if j < w - 1:
                        mask[i][j] = min(mask[i][j], mask[i][j + 1] + 1)
        return mask

s = Solution()
print(s.updateMatrix([[1,1],[1,0]]))