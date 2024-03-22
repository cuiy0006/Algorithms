class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def helper(expression):
            if expression.isnumeric():
                return [int(expression)]
            lst = []
            for i in range(1, len(expression)-1):
                if expression[i] in ops:
                    operation = ops[expression[i]]
                    for l in helper(expression[:i]):
                        for r in helper(expression[i+1:]):
                            lst.append(operation(l, r))
            return lst
        
        return helper(expression)