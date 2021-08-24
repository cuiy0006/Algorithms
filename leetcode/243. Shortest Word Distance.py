class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dic = {}
        for i, word in enumerate(wordsDict):
            if word not in dic:
                dic[word] = []
            dic[word].append(i)
        
        i = j = 0
        
        lst1 = dic[word1]
        lst2 = dic[word2]
        
        min_dist = sys.maxsize
        
        while i < len(lst1) and j < len(lst2):
            min_dist = min(min_dist, abs(lst1[i] - lst2[j]))
            if lst1[i] < lst2[j]:
                i += 1
            else:
                j += 1
        
        return min_dist
