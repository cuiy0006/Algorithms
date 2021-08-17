class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        def generate(left, right, curr):
            if left == 0 and right == 0:
                res.append(curr)
                return
            
            if left == right:
                generate(left - 1, right, curr + '(')
            elif left < right:
                if left > 0:
                    generate(left - 1, right, curr + '(')
                generate(left, right - 1, curr + ')')
                    
        generate(n, n, '')
        return res
