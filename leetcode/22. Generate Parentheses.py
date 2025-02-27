class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(left, right, curr):
            if left == 0 and right == 0:
                res.append(curr)
                return
            
            if left == right:
                helper(left-1, right, curr+'(')
            elif left < right:
                if left != 0:
                    helper(left-1, right, curr+'(')
                helper(left, right-1, curr+')')
        
        helper(n, n, '')
        return res
