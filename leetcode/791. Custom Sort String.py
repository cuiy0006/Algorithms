class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c_to_cnt = defaultdict(int)
        for c in s:
            c_to_cnt[c] += 1
        
        res = ''
        
        for c in order:
            if c in c_to_cnt:
                res += c * c_to_cnt[c]
                del c_to_cnt[c]
        
        for c, cnt in c_to_cnt.items():
            res += c * cnt
        
        return res
