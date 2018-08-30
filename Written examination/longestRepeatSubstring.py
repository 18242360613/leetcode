import sys

class Solution():
    def __init__(self,line):
        self.line = line
        self.suffix_arr = [ i for i in range(len(line))]

    def costum_key(self,s):
        return self.line[s:]

    def commonlen(self,str1,str2):
        lenght1,lenght2,l = len(str1),len(str2),0
        while l < lenght1 and l < lenght2:
            if str1[l]==str2[l]:
                l+=1
            else:
                break
        return l

    def longsetRepeatSubstring(self):
        self.suffix_arr = sorted(self.suffix_arr,key=self.costum_key)
        maxlen,curlen,maxindex = 0,0,0
        for i in range(len(self.suffix_arr)-1):
            curlen = self.commonlen(self.line[self.suffix_arr[i]:],self.line[self.suffix_arr[i+1]:])
            if curlen > maxlen:
                maxlen = curlen
                maxindex = self.suffix_arr[i]
        return self.line[maxindex:maxindex+maxlen]
    

line = "banana"
s = Solution(line)
ans = s.longsetRepeatSubstring()
print(ans)