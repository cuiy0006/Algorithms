class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ['']
        for i, digit in enumerate(digits):
            tmp = []
            for c in dic[digit]:
                for element in res:
                    tmp.append(element + c)
            res = tmp
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
        res = []
        digits = list(digits)
        
        def helper(idx, curr):
            if idx == len(digits):
                res.append(curr)
                return
            
            for c in dic[digits[idx]]:
                helper(idx+1, curr+c)
        
        helper(0, '')
        return res
