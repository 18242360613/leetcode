class Solution:
    def solve(self,boards,board,cur,n,col,dir45,dir135):
        if cur==n:
            boards.append([''.join(row) for row in board])
            return

        for j in range(n):
            if col[j]==0 and dir45[cur+j]==0 and dir135[j-cur+n-1]==0:
                col[j], dir45[cur + j], dir135[j - cur + n - 1] = 1,1,1
                board[cur][j] = 'Q'
                self.solve(boards,board,cur+1,n,col,dir45,dir135)
                col[j], dir45[cur + j], dir135[j - cur + n - 1] = 0, 0, 0
                board[cur][j] = '.'


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        boards = []
        board = [["."]*n for i in range(n)]
        col,dir45,dir135 = [0]*(2*n),[0]*(2*n),[0]*(2*n)
        self.solve(boards,board,0,n,col,dir45,dir135)
        return boards

S = Solution()
ans = S.solveNQueens(4)
print(ans)