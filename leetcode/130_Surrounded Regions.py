# class Solution:
#     def solve(self, board):
#         if not any(board): return
#         m, n, save = len(board), len(board[0]),[]
#
#         # save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
#         for i in range(m):
#             if board[i][0] == 'O':
#                 save.append((i,0))
#             if board[i][n-1] == 'O':
#                 save.append((i,n-1))
#
#         for j in range(n):
#             if board[0][j] == 'O':
#                 save.append((0,j))
#             if board[m-1][j] == 'O':
#                 save.append((m-1,j))
#
#         while len(save)>0:
#             i,j = save.pop()
#             if 0<=i and i<m and 0<=j and j<n and board[i][j] == 'O':
#                 board[i][j] = 'S'
#                 save.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
#
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'S':
#                     board[i][j] = 'O'
#                 else:
#                     board[i][j] = 'X'

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        h, w = len(board), len(board[0])

        def transform(i, j, h, w, board):
            if i < 0 or j < 0 or i >= h or j >= w or board[i][j] != 'O':
                return
            board[i][j] = 'z'
            transform(i + 1, j, h, w, board)
            transform(i - 1, j, h, w, board)
            transform(i, j + 1, h, w, board)
            transform(i, j - 1, h, w, board)

        for ix in range(h):
            transform(ix, 0, h, w, board)
            transform(ix, w - 1, h, w, board)

        for iy in range(w):
            transform(0, iy, h, w, board)
            transform(h - 1, iy, h, w, board)

        for ix in range(h):
            for iy in range(w):
                if board[ix][iy] == 'O':
                    board[ix][iy] = 'X'
                elif board[ix][iy] == 'z':
                    board[ix][iy] = 'O'

s = Solution()
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
s.solve(board)
print(board)