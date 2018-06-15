class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,over = 0,0
        a,b,c = a[::-1],b[::-1],[]
        while i < len(a) and i<len(b):
            tmp = int(a[i])+int(b[i])+over
            c.append(tmp%2)
            over = tmp//2
            i+=1

        while i<len(a):
            tmp = int(a[i])+over
            c.append(tmp%2)
            over = tmp//2
            i+=1

        while i<len(b):
            tmp = int(b[i])+over
            c.append(tmp%2)
            over = tmp//2
            i+=1

        if over>0:
            c.append(1)

        ans = ""
        for b in c[::-1]:
            ans=ans+str(b)
        return ans

s = Solution()
ans = s.addBinary("1","111")
print(ans)