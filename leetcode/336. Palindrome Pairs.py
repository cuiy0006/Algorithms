class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # case 1: CAT TAC
        # case 2: CAT SOLOSTAC
        # case 3: CATSOLOS TAC
        
        # case 2
        def get_valid_suffix(word):
            res = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    res.append(word[i+1:])
            return res
        
        # case 3
        def get_valid_prefix(word):
            res = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    res.append(word[:i])
            return res
        
        word_to_idx = {word: i for i, word in enumerate(words)}
        
        res = []
        
        for i, word in enumerate(words):
            # case 1
            rev = word[::-1]
            if rev in word_to_idx and word_to_idx[rev] != i:
                res.append([i, word_to_idx[rev]])
            
            # case 2
            for suffix in get_valid_suffix(word):
                rev_suffix = suffix[::-1]
                if rev_suffix in word_to_idx:
                    res.append([word_to_idx[rev_suffix], i])
            
            # case 3
            for prefix in get_valid_prefix(word):
                rev_prefix = prefix[::-1]
                if rev_prefix in word_to_idx:
                    res.append([i, word_to_idx[rev_prefix]])
        
        return res
