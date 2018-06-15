class Solution:
    def __init__(self):
        self.worddict = {}

    def word_Break(self, s, wordDict):
        if s in self.worddict:
            return self.worddict[s]

        if s=="":
            return [""]

        res = []
        for word in wordDict:
            if s[:len(word)] == word:
                sublist = self.word_Break(s[len(word):],wordDict)
                for sub in sublist :
                    if sub=="":
                        res.append(word)
                    else:
                        res.append(word+" "+sub)

        self.worddict[s] = res
        return res

    def wordBreak(self, s, wordDict):
        return self.word_Break(s, set(wordDict))

s = Solution()

result = s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                     ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])

# result = s.wordBreak("aab",["a", "aa", "b"])
print(result)