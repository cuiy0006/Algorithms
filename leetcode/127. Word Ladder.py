from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        seen = set([beginWord])
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        level = 1
        while len(q) != 0:
            size = len(q)
            while size != 0:
                word = q.popleft()
                size -= 1
                for i in range(len(word)):
                    for c in alpha:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word == endWord:
                            return level + 1
                        if new_word not in seen and new_word in wordList:
                            q.append(new_word)
                            seen.add(new_word)
            level += 1
        return 0
