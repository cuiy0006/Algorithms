class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i = 0
        while i < len(num):
            while len(stack) != 0 and num[i] < stack[-1]:
                stack.pop()
                k -= 1
                if k == 0:
                    break
            if k == 0:
                break
            stack.append(num[i])
            i += 1
        
        s = ''.join(stack)
        if k == 0:
            res = s + num[i:]
        else:
            res = s[:-k]
        i = 0
        while i < len(res):
            if res[i] == '0':
                i += 1
            else:
                break
        res = res[i:]
        return res if res != '' else '0'
