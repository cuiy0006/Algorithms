class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @cache
        def func1(n: str) -> int: # xxxx -> 0000
            if len(n) == 0:
                return 0
            if n == '0':
                return 0
            elif n == '1':
                return 1
            
            if n[0] == '0':
                return func1(n[1:])
            
            return func2(n[1:]) + 1 + func1('1'+'0' * (len(n)-2))
            
        @cache
        def func2(n: str) -> int: # xxxx -> 1000
            if len(n) == 0:
                return 0
            if n == '0':
                return 1
            elif n == '1':
                return 0
            
            if n[0] == '1':
                return func1(n[1:])
            else:
                return func2(n[1:]) + 1 + func1('1' + '0' * (len(n)-2))
        
        ns = ''
        while n != 0:
            ns = str(n%2) + ns
            n = n // 2
        return func1(ns)
