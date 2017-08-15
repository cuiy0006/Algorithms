class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        res = []
        start = -1
        end = -1
        for i in range(len(s)):
            for word in dict:
                if s[i:].startswith(word):
                    if start < 0:
                        start = i
                        end = i + len(word) -1
                        continue
                    if i > end + 1:
                        res.append((start, end))
                        start = i
                        end = i + len(word) -1
                    else:
                        end = max(end, i+len(word)-1)
        if start >= 0:
            res.append((start, end))
        start = 0
        arr = []
        for left, right in res:
            arr.append(s[start:left])
            arr.append('<b>')
            arr.append(s[left:right+1])
            arr.append('</b>')
            start = right+1
        arr.append(s[start:])
        return ''.join(arr)
            
