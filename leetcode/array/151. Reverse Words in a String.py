class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        filtered = [word for word in lst if word != '']
        filtered.reverse()
        return ' '.join(filtered)
