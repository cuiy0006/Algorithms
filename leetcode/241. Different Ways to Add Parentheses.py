class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def evaluate(expression) -> List[int]:
            res = []
            
            def add(left, right):
                res = []
                for num1 in left:
                    for num2 in right:
                        res.append(num1 + num2)
                return res
            
            def minus(left, right):
                res = []
                for num1 in left:
                    for num2 in right:
                        res.append(num1 - num2)
                return res
            
            def multiply(left, right):
                res = []
                for num1 in left:
                    for num2 in right:
                        res.append(num1 * num2)
                return res
            
            op = False
            for i in range(len(expression)):
                c = expression[i]
                if not c.isdigit():
                    op = True
                    left = evaluate(expression[:i])
                    right = evaluate(expression[i+1:])
                    if c == '+':
                        res = res + add(left, right)
                    elif c == '-':
                        res = res + minus(left, right)
                    else:
                        res = res + multiply(left, right)
            
            if not op:
                res.append(int(expression))
            return res
        
        return evaluate(expression)
