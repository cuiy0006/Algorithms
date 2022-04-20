class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word:len(word))
        
        len_to_words = DefaultDict(set)
        
        for word in words:
            len_to_words[len(word)].add(word)
            
        len_lst = list(len_to_words.keys())
        len_lst.sort()
        
        word_path = {word:1 for word in words}
        res = 1
        
        for l in len_lst:
            if l + 1 not in len_to_words:
                continue
            
            first = len_to_words[l]
            second = len_to_words[l+1]
            for word1 in first:
                for word2 in second:
                    for i in range(len(word1)):
                        if word1[i] != word2[i]:
                            if word1[:i] + word2[i] + word1[i:] == word2:
                                word_path[word2] = max(word_path[word2], word_path[word1] + 1)
                            break
                        if i == len(word1) - 1:
                            if word1 + word2[-1] == word2:
                                word_path[word2] = max(word_path[word2], word_path[word1] + 1)
                                
                    res = max(res, word_path[word2])
        return res
