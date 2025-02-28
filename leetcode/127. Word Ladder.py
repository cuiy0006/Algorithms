class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        
        q = deque([beginWord])
        d = 0
        while len(q) != 0:
            size = len(q)
            d += 1
            for _ in range(size):
                word = q.popleft()
                if word == endWord:
                    return d
                for i in range(len(word)):
                    lst = list(word)
                    for j in range(26):
                        lst[i] = chr(ord('a')+j)
                        new_word = ''.join(lst)
                        if new_word not in words:
                            continue
                        words.remove(new_word)
                        q.append(new_word)
        return 0
