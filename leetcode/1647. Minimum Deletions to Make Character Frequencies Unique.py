import sys
class Solution:
    def minDeletions(self, s: str) -> int:
        dic = {}
        
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        
        freq_dic = {}
        for c, freq in dic.items():
            if freq not in freq_dic:
                freq_dic[freq] = 0
            freq_dic[freq] += 1
        
        freqs = list(freq_dic.keys())
        freqs.sort(key=lambda x:-x)

        res = 0
        i = sys.maxsize
        for freq in freqs:
            cnt = freq_dic[freq] - 1
            if cnt == 0:
                continue
            if i == 0:
                res += freq * cnt
                continue
            
            if i >= freq:
                i = freq
            else:
                res += (freq - i) * cnt
                
            while i > 0:
                if i not in freq_dic:
                    freq_dic[i] = 1
                    cnt -= 1
                    if cnt == 0:
                        break

                res += cnt
                i -= 1
                
        return res
                
            
