from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ''
        in_dic = {c: 0 for word in words for c in word}
        out_dic = {}
        
        curr = words[0]
        for i in range(1, len(words)):
            target = words[i]
            j = 0
            while j < min(len(curr), len(target)):
                if curr[j] != target[j]:
                    if curr[j] not in out_dic:
                        out_dic[curr[j]] = set()
                    if target[j] not in out_dic[curr[j]]:
                        out_dic[curr[j]].add(target[j])
                        in_dic[target[j]] += 1
                    break
                j += 1
            
            if j == min(len(curr), len(target)) and len(target) < len(curr):
                return ''
            curr = target
            
        res = ''
        
        q = deque([c for c in in_dic if in_dic[c] == 0])
        while len(q) != 0:
            c = q.popleft()
            res += c
            if c not in out_dic:
                continue
            for d in out_dic[c]:
                in_dic[d] -= 1
                if in_dic[d] == 0:
                    q.append(d)
                    
        if len(res) != len(in_dic):
            return ''
        
        return res
