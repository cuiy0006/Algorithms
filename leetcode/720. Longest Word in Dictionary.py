class Solution:
    def longestWord(self, words: List[str]) -> str:
        dic = defaultdict(set)
        for word in words:
            dic[len(word)].add(word)
        
        i = 1
        if 1 not in dic:
            return ''
        
        while i+1 in dic:
            lv2 = dic[i+1]
            lv1 = dic[i]
            
            new_lv2 = set()
            for word in lv2:
                for j in range(len(word)):
                    new_word = word[:j] + word[j+1:]
                    if new_word in lv1:
                        new_lv2.add(word)
                        break
            
            dic[i+1] = new_lv2
            if len(new_lv2) == 0:
                lv1 = list(lv1)
                lv1.sort()
                return lv1[0]
            i += 1
        
        lv = list(dic[i])
        lv.sort()
        return lv[0]
