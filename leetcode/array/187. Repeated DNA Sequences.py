class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        dic = defaultdict(int)

        val = 0
        for i in range(10):
            val = val * 4 + mapping[s[i]]
        dic[val] += 1
        res = []
        
        for i in range(1, len(s)-9):
            val = (val - mapping[s[i-1]] * (4 ** 9)) * 4 + mapping[s[i+9]]
            dic[val] += 1
            if dic[val] == 2:
                res.append(s[i:i+10])
        
        return res
