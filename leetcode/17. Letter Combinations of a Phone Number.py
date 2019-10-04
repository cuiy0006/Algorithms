class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        dic = {'2':'abc',
                '3': 'def',
                '4': 'ghi'
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        res = []
        def helper(idx, curr):
            if idx == len(digits):
                res.append(''.join(curr))
                return;
            s = dic[digits[idx]]
            for c in s:
                curr.append(c)
                helper(idx + 1, curr)
                curr.pop()
        helper(0, [])
        return res
            
            
            
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        dic = {'2':'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        res = ['']
        
        for digit in digits:
            s = dic[digit]
            tmp = []
            for c in s:
                for prev in res:
                    tmp.append(prev + c)
            res = tmp
        return res
            
