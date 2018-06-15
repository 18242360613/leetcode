import  collections

class Solution(object):
    def minWindow(self, s, t):
        i= starti = endj = 0
        need,missing = collections.Counter(t),len(t)
        for j,c in enumerate(s,1):
            missing -= need[c]>0
            need[c]-=1
            if not missing:
                while i < j and need[s[i]]<0:
                    need[s[i]]+=1
                    i+=1
                if not endj or (endj-starti) > (j-i):
                    starti,endj = i,j
        return s[starti:endj]

s = Solution()
# print(s.minWindow("ADOBECODEBANC","ABC"))
print(s.minWindow("a","aa"))