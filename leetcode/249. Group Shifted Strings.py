class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strings:
            diff = ord(s[0]) - ord('a')
            root = ''
            for c in s:
                c_val = ord(c) - diff
                if c_val < ord('a'):
                    c_val += 26
                root += chr(c_val)
            dic[root].append(s)
        
        return list(dic.values())