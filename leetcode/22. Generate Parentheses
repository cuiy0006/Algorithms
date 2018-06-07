class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(left, right, res, curr):
            """
            :type left: int
            :type right: int
            :type res: List[str]
            :type curr: str
            """
            if left == n:
                while len(curr) < 2 * n:
                    curr += ')'
                res.append(curr)
                return
            if right != left:
                helper(left, right + 1, res, curr + ')')
            helper(left + 1, right, res, curr + '(')
        if n == 0:
            return []
        res = []
        helper(0, 0, res, '')
        return res
