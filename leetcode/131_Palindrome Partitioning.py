class Solution:
    def isvalid(self,temlist):
        for s in temlist:
            if s!=s[::-1]:
                return False
        return True

    def dfs(self,ans,templist):
        if self.isvalid(templist):
            ans.append(templist.copy())


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
