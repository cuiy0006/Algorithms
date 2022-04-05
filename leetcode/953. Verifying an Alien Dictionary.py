class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i, c in enumerate(order):
            dic[c] = i
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            
            min_len = min(len(word1), len(word2))
            
            for j in range(min_len):
                if dic[word1[j]] > dic[word2[j]]:
                    return False
                elif dic[word1[j]] < dic[word2[j]]:
                    break
                
                if j == min_len - 1 and len(word1) > len(word2):
                    return False

        return True
