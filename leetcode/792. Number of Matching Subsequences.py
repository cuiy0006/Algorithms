class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = {}
        for word in words:
            if word[0] not in dic:
                dic[word[0]] = deque()
            dic[word[0]].append(word)

        cnt = 0
        for c in s:
            if c not in dic:
                continue
            size = len(dic[c])
            for i in range(size):
                word = dic[c].pop()
                if len(word) == 1:
                    cnt += 1
                else:
                    if word[1] not in dic:
                        dic[word[1]] = deque()
                    dic[word[1]].appendleft(word[1:])
        return cnt

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list) # start char -> rest str
        
        for word in words:
            dic[word[0]].append(word[1:])
        
        res = 0
        for c in s:
            if c not in dic:
                continue
            
            words = dic[c]
            del dic[c]
            for word in words:
                if word == '':
                    res += 1
                    continue
                dic[word[0]].append(word[1:])
        
        return res

    

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_to_idx = defaultdict(int) # word -> idx
        word_to_cnt = defaultdict(int) # word -> count
        for word in words:
            word_to_cnt[word] += 1
            word_to_idx[word] = 0
        
        res = 0
        for i in range(len(s)):
            words = list(word_to_idx.keys())
            for word in words:
                idx = word_to_idx[word]
                if s[i] == word[idx]:
                    word_to_idx[word] += 1
                if word_to_idx[word] > len(word) - 1:
                    res += word_to_cnt[word]
                    del word_to_idx[word]
                    del word_to_cnt[word]
        return res
