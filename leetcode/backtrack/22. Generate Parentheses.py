class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(left, right, curr):
            if left == n and right == n:
                res.append(''.join(curr))
                return
            
            if left < n:
                curr.append('(')
                helper(left+1, right, curr)
                curr.pop()
            
            if right < left:
                curr.append(')')
                helper(left, right+1, curr)
                curr.pop()
            
        helper(0, 0, [])
        return res
