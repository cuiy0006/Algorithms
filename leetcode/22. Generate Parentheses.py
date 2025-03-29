class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, left, right):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if left != n:
                dfs(curr + '(', left+1, right)
            if left > right:
                dfs(curr + ')', left, right+1)
        dfs('', 0, 0)
        return res
            
