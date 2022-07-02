class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                destroyed = False
                while len(stack) != 0 and stack[-1] > 0:
                    curr = stack[-1] + ast
                    if curr == 0:
                        destroyed = True
                        stack.pop()
                        break
                    elif curr < 0:
                        stack.pop()
                    else:
                        destroyed = True
                        break
                
                if not destroyed:
                    stack.append(ast)
        
        return stack
