class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if not s or not words or not words[0]:
            return result
        n = len(s)
        nums = len(words)
        wordlen = len(words[0])
        totallen = nums*wordlen
        worddir = {}
        for w in words:
            worddir[w] = worddir.get(w,0)+1
        for i in range(wordlen):
            left = i
            right = i
            seen={}
            while right+wordlen<=n:
                word = s[right:right + wordlen]
                right = right + wordlen
                if word in worddir:
                    seen[word] = seen.get(word,0)+1
                    while seen[word] > worddir[word]:
                        seen[s[left:left+wordlen]] = seen[s[left:left+wordlen]]-1
                        left+=wordlen
                    if right - left ==totallen:
                        result.append(left)
                else:
                    seen.clear()
                    left = right

        return result

s = Solution()
print(s.findSubstring("aaaaaaaabb",["aa","bb"]))