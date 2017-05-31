from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dic = {beginWord:1}
        s = set(wordList)
        
        if endWord not in s:
            return 0
        
        q = deque([beginWord])
        while len(q) != 0:
            word = q.popleft()
            for i in range(len(word)):
                for j in range(26):
                    c = chr(ord('a') + j)
                    new_word = word[:i] + c + word[i+1:]

                    if new_word == endWord:
                        return dic[word] + 1
                    if new_word in s and new_word not in dic:
                        dic[new_word] = dic[word] + 1
                        q.append(new_word)
        return 0
