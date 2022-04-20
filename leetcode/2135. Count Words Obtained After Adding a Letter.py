class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        targets = defaultdict(int)
        for word in targetWords:
            chars = [0] * 26
            for c in word:
                chars[ord(c) - ord('a')] += 1
            targets[tuple(chars)] += 1

        res = 0
        for word in startWords:
            chars = [0] * 26
            for c in word:
                chars[ord(c) - ord('a')] += 1
            
            for i in range(26):
                if chars[i] != 0:
                    continue
                chars[i] = 1
                tp = tuple(chars)
                if tp in targets:
                    res += targets[tp]
                    del targets[tp]
                chars[i] = 0

        return res
