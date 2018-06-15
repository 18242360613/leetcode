class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans,tmpstr,tmpans,tmplen = [],"",[],0
        for word in words:
            if len(tmpstr)==0 or len(tmpstr)+len(word)<=maxWidth:
                tmpans.append(word)
                tmpstr=tmpstr+word+" "
                tmplen+=len(word)
            else:
                fk = []
                if len(tmpans)==1:
                    fk.append(maxWidth - tmplen)
                else:
                    tk = (maxWidth - tmplen)//(len(tmpans)-1)
                    fk = [tk]*(len(tmpans)-1)
                    re = maxWidth-tk*(len(tmpans)-1)-tmplen
                    for i in range(re):
                        fk[i] = fk[i]+1
                tmpstr = ""
                for i in list(range(len(tmpans))):
                    if i < len(tmpans)-1 or i==0:
                        tmpstr=tmpstr+tmpans[i]+" "*fk[i]
                    else:
                        tmpstr = tmpstr + tmpans[i]
                ans.append(tmpstr)
                tmpans.clear()
                tmpans.append(word)
                tmpstr,tmplen,=word+" ",len(word)

        if len(tmpans)>0:
            tmpstr = tmpans[0]
            for w in tmpans[1:]:
                tmpstr = tmpstr+" "+w
            tmpstr = tmpstr+" "*(maxWidth - len(tmpstr))
            ans.append(tmpstr)
        return ans

s = Solution()
ans = s.fullJustify(["What","must","be","acknowledgment","shall","be"],16)
print(ans)