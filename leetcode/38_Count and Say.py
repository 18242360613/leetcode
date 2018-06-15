class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=1:return '1';
        ans = '1'
        for _ in list(range(2,n+1)):
            key,count,tmp = ans[0],0,""
            for c in ans:
                if c==key:
                    count+=1
                else:
                    tmp=tmp+str(count)+key
                    key = c
                    count = 1
            tmp = tmp + str(count) + key
            ans = tmp
        return ans

s = Solution()
for i in range(20):
    print(s.countAndSay(i))