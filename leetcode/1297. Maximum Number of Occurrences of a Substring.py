class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = {}
        count = defaultdict(int)
        j = 0
        i = 0
        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = 0
            dic[s[j]] += 1
            j += 1
            if j > minSize:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    del dic[s[i]]
                i += 1

            if j > minSize-1:
                if len(dic) <= maxLetters:
                    count[s[i:j]] += 1
            
        if len(count) == 0:
            return 0
        return max(count.values())
