class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for s in strs:
            chars = [0 for _ in range(26)]
            for c in s:
                chars[ord(c) - ord('a')] += 1
            chars = tuple(chars)
            if chars not in dic:
                dic[chars] = []
            dic[chars].append(s)
        
        return list(dic.values())
