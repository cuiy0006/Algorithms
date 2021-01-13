class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda e: (-len(e), e))
        for sub in d:
            if len(sub) == 0:
                return sub
            i = 0
            for c in s:
                if c == sub[i]:
                    i += 1
                    if i == len(sub):
                        return sub
        return ""
