from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        def helper(start, end, dic, tmp, res):
            if start not in dic:
                return
            for word in dic[start]:
                tmp.append(word)
                if word == end:
                    res.append(tmp[::-1])
                helper(word, end, dic, tmp, res)
                tmp.pop()
                
        
        dic = {}
        ladder = {word:sys.maxsize for word in wordList}
        ladder[beginWord] = 0
        q = deque([beginWord])
        minimum = sys.maxsize
        
        while len(q) != 0:
            word = q.popleft()
            step = ladder[word] + 1
            if step > minimum:
                continue
            
            for i, c in enumerate(word):
                for j in range(26):
                    newc = chr(ord('a') + j)
                    if newc == c:
                        continue
                    newWord = word[:i] + newc + word[i+1:]
                    if newWord in ladder:
                        if step > ladder[newWord]:
                            continue
                        elif step < ladder[newWord]:
                            ladder[newWord] = step
                            q.append(newWord)
                        
                        if newWord in dic:
                            dic[newWord].append(word)
                        else:
                            dic[newWord] = [word]
                        
                        if newWord == endWord:
                            minimum = step
                            
        res = []
        helper(endWord, beginWord, dic, [endWord], res)
        return res
