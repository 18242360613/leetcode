class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:return []
        ans = []
        rowbegin,rowend,colbegin,colend = 0,len(matrix)-1,0,len(matrix[0])-1
        while rowbegin<=rowend and colbegin<=colend:
            #right
            for j in range(colbegin,colend+1):
                ans.append(matrix[rowbegin][j])
            rowbegin+=1

            #down
            for i in range(rowbegin,rowend+1):
                ans.append(matrix[i][colend])
            colend-=1
            #left
            if rowbegin<=rowend:
                for j in list(range(colend,colbegin-1,-1)):
                    ans.append(matrix[rowend][j])
                rowend-=1
            #up
            if colbegin<=colend:
                for i in list(range(rowend,rowbegin-1,-1)):
                    ans.append(matrix[i][colbegin])
                colbegin+=1
        return ans

s = Solution()
ans = s.spiralOrder([])
print(ans)