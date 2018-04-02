class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = {} #word -> index
        for i, word in enumerate(words):
            dic[word] = i
            
        res = set()
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                sub = word[:j]
                panlindrome = word[j:]
                if panlindrome == panlindrome[::-1]:
                    reverse_sub = sub[::-1]
                    if reverse_sub in dic and reverse_sub != word:
                        res.add((i, dic[reverse_sub]))
                        
                sub = word[j:]
                panlindrome = word[:j]
                if panlindrome == panlindrome[::-1]:
                    reverse_sub = sub[::-1]
                    if reverse_sub in dic and reverse_sub != word:
                        res.add((dic[reverse_sub], i))
        return [[i, j] for i, j in res]
