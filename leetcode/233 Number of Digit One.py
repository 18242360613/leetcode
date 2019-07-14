class Solution:
    def countDigitOne(self, n) :
        '''
        The idea is to calculate occurrence of 1 on every digit. There are 3 scenarios, for example

        if n = xyzdabc
        and we are considering the occurrence of one on thousand, it should be:
        (1) xyz * 1000 + 0                    if d == 0, means there is no 1 because of  this digit(none)
        (2) xyz * 1000 + abc + 1          if d == 1, means there is abc of  1 because  of this digit(patrial)
        (3) xyz * 1000 + 1000              if d > 1,  means there  is fully 1000 of  1 because of  this digit(fully)

        :param n:
        :return:
        '''
        ans,q,x = 0,n,1

        while q > 0:
            q,d = divmod(q,10)
            if d == 0:
                ans = ans + q*x
            elif d==1:
                ans = ans + q*x+n%x+1
            else:
                ans = ans + q*x+x

            x = x * 10

        return ans

S = Solution()
ans = S.countDigitOne(13)
print(ans)

