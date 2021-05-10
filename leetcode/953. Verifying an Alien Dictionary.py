class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        
        seq_dic = {}
        for i, c in enumerate(order):
            seq_dic[c] = i
            
        def is_valid(w1, w2):
            i = 0
            
            while i < len(w1) and i < len(w2):
                if seq_dic[w1[i]] < seq_dic[w2[i]]:
                    return True
                elif seq_dic[w1[i]] > seq_dic[w2[i]]:
                    return False
                i += 1
            
            if len(w1) > len(w2):
                return False
            else:
                return True
        
        curr = words[0]
        i = 1
        while i < len(words):
            target = words[i]
            valid = is_valid(curr, target)
            if not valid:
                return False
            curr = target
            i += 1
        return True
        
