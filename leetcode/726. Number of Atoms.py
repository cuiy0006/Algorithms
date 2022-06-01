class Solution:
    def countOfAtoms(self, formula: str) -> str:
        curr = defaultdict(int)
        stack = []
        i = 0
        last = None
        
        while i < len(formula):
            c = formula[i]
            if c == '(':
                stack.append(curr)
                curr = defaultdict(int)
                i += 1
            elif c == ')':
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                if i+1 == j:
                    num = 1
                else:
                    num = int(formula[i+1:j])
                curr = defaultdict(int, {key: val*num for key, val in curr.items()})
                if len(stack) != 0:
                    for key, val in stack[-1].items():
                        curr[key] += val
                    stack.pop()
                i = j
            else:
                if c.isdigit():
                    j = i
                    while j < len(formula) and formula[j].isdigit():
                        j += 1
                    num = int(formula[i:j])
                    curr[last] += num - 1
                    i = j
                else:
                    j = i + 1
                    last = c
                    while j < len(formula) and formula[j].islower():
                        last += formula[j]
                        j += 1
                    curr[last] += 1
                    i = j
        
        lst = [key+str(val) if val != 1 else key for key, val in curr.items()]
        lst.sort()
        return ''.join(lst)
