class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict = {}
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num!=".":
                    rowkey = str(i)+'('+num+')'
                    colkey = '('+num+')'+str(j)
                    blokey = str((i//3))+'('+num+')'+str(j//3)
                    if (not rowkey in dict)and (not colkey in dict) and (not blokey in dict):
                        dict[rowkey] = 1
                        dict[colkey] = 1
                        dict[blokey] = 1
                    else:
                        return  False
        return True


s = Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

result = s.isValidSudoku(board)
print(result)
