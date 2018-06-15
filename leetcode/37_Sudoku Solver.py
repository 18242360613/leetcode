class Solution:

    def isValidSudoku(self, board):
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

    def dictremove(self,dictlist,i,j,c):
        rowind, cloind, bloind = i, 9 + j, 18 + (3 * (i // 3) + (j // 3))
        dictlist[rowind].remove(c)
        dictlist[cloind].remove(c)
        dictlist[bloind].remove(c)

    def dictadd(self,dictlist,i,j,c):
        rowind, cloind, bloind = i, 9 + j, 18 + (3 * (i // 3) + (j // 3))
        dictlist[rowind].add(c)
        dictlist[cloind].add(c)
        dictlist[bloind].add(c)

    def solve(self,k,length,board,pos,dictlist):
        if k==length:
            self.t+=1
            if self.isValidSudoku(board):
                return True
            else:
                return False
        else:
            i,j = pos[k][0],pos[k][1]
            rowind, cloind, bloind = i, 9 + j, 18 + (3 * (i // 3) + (j // 3))
            keyset = dictlist[rowind] & dictlist[cloind] & dictlist[bloind]
            if len(keyset)>0:
                for c in keyset:
                    self.dictremove(dictlist,i,j,c)
                    board[i][j] = c
                    if self.solve(k+1,length,board,pos,dictlist):
                        return True
                    board[i][j] = '.'
                    self.dictadd(dictlist, i, j, c)
            else:
                return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dictlist = [set(['1','2','3','4','5','6','7','8','9']) for i in range(27)]
        pos=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    self.dictremove(dictlist, i, j, board[i][j])
                else:
                    pos.append((i,j))

        self.solve(0,len(pos),board,pos,dictlist)
        return board

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

result = s.solveSudoku(board)
print(result)
print(s.t)
