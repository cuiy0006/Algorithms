class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remove = set()
        for i in range(len(num)):
            while len(stack) != 0 and num[i] < num[stack[-1]]:
                r = stack.pop()
                remove.add(r)
                if len(remove) == k:
                    break
            if len(remove) == k:
                break
            stack.append(i)
        res = ''
        cnt = 0
        for i, c in enumerate(num):
            if cnt == len(num)-k:
                break
            if i not in remove:
                cnt += 1
                if res == '' and c == '0':
                    continue
                res += c
        if res == '':
            return '0'
        return res
