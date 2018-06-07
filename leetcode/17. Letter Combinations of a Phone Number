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




dic = {'1':'*', '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def helper(digit, lst):
            new_lst = []
            chars = dic[digit]
            for word in lst:
                for c in chars:
                    new_lst.append(word + c)
            return new_lst
        
        if len(digits) == 0:
            return []
        
        res = ['']
        for digit in digits:
            res = helper(digit, res)
        return res
