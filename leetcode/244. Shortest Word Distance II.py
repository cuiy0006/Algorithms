class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = {}
        for i, word in enumerate(wordsDict):
            if word not in self.dic:
                self.dic[word] = []
            self.dic[word].append(i)
        
        for word in self.dic.keys():
            self.dic[word].sort()

    def shortest(self, word1: str, word2: str) -> int:
        idx_lst1 = self.dic[word1]
        idx_lst2 = self.dic[word2]
        
        i = j = 0
        shortest = sys.maxsize
        while i < len(idx_lst1) and j < len(idx_lst2):
            shortest = min(shortest, abs(idx_lst1[i] - abs(idx_lst2[j])))
            if idx_lst1[i] < idx_lst2[j]:
                i += 1
            else:
                j += 1
        return shortest
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
