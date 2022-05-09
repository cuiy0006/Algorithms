class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_d = sys.maxsize
        if word1 == word2:
            i = 0
            j = 0
            while i < len(wordsDict) and wordsDict[i] != word1:
                i += 1
            j = i+1
            while j < len(wordsDict):
                while j < len(wordsDict) and wordsDict[j] != word1:
                    j += 1
                if j == len(wordsDict):
                    break
                min_d = min(min_d, j-i)
                i = j
                j = j + 1
        else:
            i = 0
            j = 0
            while i < len(wordsDict) and wordsDict[i] != word1:
                i += 1
            while j < len(wordsDict) and wordsDict[j] != word2:
                j += 1
            
            while i < len(wordsDict) and j < len(wordsDict):
                min_d = min(min_d, abs(i-j))
                if i < j:
                    i += 1
                    while i < len(wordsDict) and wordsDict[i] != word1:
                        i += 1
                else:
                    j += 1
                    while j < len(wordsDict) and wordsDict[j] != word2:
                        j += 1
        return min_d
