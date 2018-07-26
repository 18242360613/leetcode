# from queue import Queue
#
# class Solution:
#
#     def getNeighbors(self,cur,wordSet):
#         wordlist = list(cur)
#         neighbors = []
#         for i in range(97,123):
#             ch = chr(i)
#             for i in range(len(wordlist)):
#                 ch_old = wordlist[i]
#                 wordlist[i] = ch
#                 tmpkey = ''.join(wordlist)
#                 if tmpkey in wordSet:
#                     neighbors.append(tmpkey)
#                 wordlist[i] = ch_old
#         return neighbors
#
#
#
#     def bfs(self,curWord,endWord,nodeNeighbors,distances,wordSet):
#         # 建立词列表
#         for word in wordSet:
#             nodeNeighbors[word] = []
#
#         q = Queue()
#         q.put(curWord)
#         distances[curWord] = 0
#
#         found = False
#         while not q.empty():
#             count = q.qsize()
#             for i in range(count):
#                 cur = q.get()
#                 distance = distances.get(cur)
#                 neighbors = self.getNeighbors(cur,wordSet)
#                 for neighbor in neighbors:
#                     nodeNeighbors.get(cur).append(neighbor)
#                     if not neighbor in distances:
#                         distances[neighbor] = distance+1
#                         if neighbor == endWord:
#                             found = True
#                         else:
#                             q.put(neighbor)
#             if found:
#                 break
#
#     def dfs(self,curWord,endWord,nodeNeighbors,distances,ans,tmplist):
#         tmplist.append(curWord)
#         if curWord == endWord:
#             ans.append(tmplist.copy())
#         else:
#             for word in nodeNeighbors.get(curWord):
#                 if distances[word] == (distances[curWord]+1):
#                     self.dfs(word,endWord,nodeNeighbors,distances,ans,tmplist)
#         tmplist.pop()
#
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#         ans,solution,nodeNeighbors,distances,wordSet  = [],[],{},{},set()
#         for word in wordList:
#             wordSet.add(word)
#         wordSet.add(beginWord)
#         self.bfs(beginWord,endWord,nodeNeighbors,distances,wordSet)
#         self.dfs(beginWord,endWord,nodeNeighbors,distances,ans,[])
#         return ans

import collections
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict:
            return []
        front, back = set([beginWord]), set([endWord])

        direction = 1
        parents = collections.defaultdict(set)

        while front and back:
            if len(front) > len(back):
                front, back = back, front
                direction *= -1

            wordDict -= front
            next_level = set()

            for word in front:
                for index in range(len(beginWord)):
                    p1, p2 = word[:index], word[index + 1:]
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = p1 + ch + p2
                        if next_word in wordDict:
                            next_level.add(next_word)
                            if direction == 1:
                                parents[next_word].add(word)
                            else:
                                parents[word].add(next_word)

            if next_level & back:
                res = [[endWord]]
                while res and res[0][0] != beginWord:
                    res = [[p] + r for r in res for p in parents[r[0]]]
                return res

            front = next_level

        return []


beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

s = Solution()
ans = s.findLadders(beginWord,endWord,wordList)
print(ans)