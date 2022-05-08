from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        q = deque([beginWord])
        
        depth = 1
        while len(q) != 0:
            size = len(q)
            while size != 0:
                size -= 1
                word = q.popleft()
                if word == endWord:
                    return depth
                
                for i in range(len(word)):
                    for j in range(26):
                        c = chr(ord('a') + j)
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            q.append(new_word)
                            word_set.remove(new_word)
            depth += 1
        return 0
