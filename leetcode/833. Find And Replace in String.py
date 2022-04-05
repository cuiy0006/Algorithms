class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        if len(indices) == 0:
            return s
        
        zipped = list(zip(indices, sources, targets))
        zipped.sort(key=lambda tp: tp[0])
        
        res = s[:zipped[0][0]]
        
        for i in range(len(indices)):
            idx = zipped[i][0]
            source = zipped[i][1]
            target = zipped[i][2]
            
            s_l = len(source)
            
            if s[idx:idx+s_l] == source:
                res += target
                if i == len(zipped) - 1:
                    res += s[idx+s_l:]
                else:
                    res += s[idx+s_l:zipped[i+1][0]]
            else:
                if i == len(zipped) - 1:
                    res += s[idx:]
                else:
                    res += s[idx:zipped[i+1][0]]
        return res
