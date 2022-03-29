class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq_to_cnt = {}
        
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq not in seq_to_cnt:
                seq_to_cnt[seq] = 0
            seq_to_cnt[seq] += 1
            
        res = []
        for seq, cnt in seq_to_cnt.items():
            if cnt > 1:
                res.append(seq)
        return res
