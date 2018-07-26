from queue import Queue

class Solution:
    def __init__(self):
        self.minlen = 0

    def getNeighbors(self,cur,wordSet):
        wordlist = list(cur)
        neighbors = []
        for i in range(97,123):
            ch = chr(i)
            for i in range(len(wordlist)):
                ch_old = wordlist[i]
                wordlist[i] = ch
                tmpkey = ''.join(wordlist)
                if tmpkey in wordSet:
                    neighbors.append(tmpkey)
                wordlist[i] = ch_old
        return neighbors



    def bfs(self,curWord,endWord,nodeNeighbors,distances,wordSet):
        # 建立词列表
        for word in wordSet:
            nodeNeighbors[word] = []

        q = Queue()
        q.put(curWord)
        distances[curWord] = 1

        found = False
        while not q.empty():
            count = q.qsize()
            for i in range(count):
                cur = q.get()
                distance = distances.get(cur)
                neighbors = self.getNeighbors(cur,wordSet)
                for neighbor in neighbors:
                    nodeNeighbors.get(cur).append(neighbor)
                    if not neighbor in distances:
                        distances[neighbor] = distance+1
                        if neighbor == endWord:
                            found = True
                            self.minlen = distance+1
                        else:
                            q.put(neighbor)
            if found:
                break

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        solution,nodeNeighbors,distances,wordSet  = [],{},{},set()
        for word in wordList:
            wordSet.add(word)
        wordSet.add(beginWord)
        self.bfs(beginWord,endWord,nodeNeighbors,distances,wordSet)
        return self.minlen
