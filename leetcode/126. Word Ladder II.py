from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        
        word_to_depth = {beginWord: 0}
        word_to_parent = defaultdict(set)
        
        q = deque([beginWord])
        
        depth = 1
        done = False
        
        while len(q) != 0:
            size = len(q)
            if done:
                break
            
            for _ in range(size):
                word = q.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        c = chr(ord('a')+j)
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            if new_word not in word_to_depth or depth <= word_to_depth[new_word]:
                                word_to_depth[new_word] = depth
                                word_to_parent[new_word].add(word)
                                q.append(new_word)
                                if new_word == endWord:
                                    done = True
            depth += 1
            
        res = []
        def dfs(word, curr):
            if word == beginWord:
                lst = curr[:]
                lst.append(word)
                res.append(lst[::-1])
                return

            curr.append(word)
            parents = word_to_parent[word]
            for parent in parents:
                dfs(parent, curr)
            curr.pop()
            
            
        dfs(endWord, [])
        
        return res
