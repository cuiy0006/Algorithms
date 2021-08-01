class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = 0
        curr = '' 
        while i < len(s):
            c = s[i]
            if c == ' ':
                res.append(curr)
                curr = ''
            else:
                curr = c + curr
            i += 1
            
        res.append(curr)
        return ' '.join(res)
