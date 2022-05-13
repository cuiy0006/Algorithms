class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt = [0] * 26
        for c in chars:
            char_cnt[ord(c)-ord('a')] += 1
            
        def is_word_good(word, curr):
            for c in word:
                idx = ord(c) - ord('a')
                if curr[idx] == 0:
                    return False
                curr[idx] -= 1
            return True
        
        res = 0
        for word in words:
            if is_word_good(word, char_cnt[:]):
                res += len(word)
        
        return res
            
