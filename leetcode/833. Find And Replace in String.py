class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        def is_subseq(s, i, sub):
            j = 0
            while j < len(sub) and i < len(s):
                if sub[j] != s[i]:
                    return False
                i += 1
                j += 1
            return j == len(sub)
        
        combo = list(zip(indices, sources, targets))
        combo.sort()
        indices = [tp[0] for tp in combo]
        sources = [tp[1] for tp in combo]
        targets = [tp[2] for tp in combo]
        
        res = ''
        if indices[0] != 0:
            res += s[:indices[0]]
        
        for i, idx in enumerate(indices):
            if i == len(indices) - 1:
                j = len(s)
            else:
                j = indices[i + 1]
                
            if is_subseq(s, idx, sources[i]):
                res += targets[i] + s[idx+len(sources[i]): j]
            else:
                res += s[idx: j]
                
        return res
                    
