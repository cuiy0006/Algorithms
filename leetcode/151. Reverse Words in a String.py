class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        res = []
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] != '':
                res.append(lst[i])
        
        return ' '.join(res)
        
        
        
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        words = s.split(' ')
        words = list(filter(lambda word: word != '', words))
        words.reverse()
        
        return ' '.join(words)
