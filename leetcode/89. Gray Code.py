class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        idx = 0
        lst = [0]
        while idx < n:
            sub = []
            for i, num in enumerate(lst):
                sub.append((1<<idx)|num)
            lst = lst + list(reversed(sub))
            idx += 1
        return lst


class Solution:
    def grayCode(self, n: int) -> List[int]:
        def str_to_num(s):
            num = 0
            n = 1
            for i in range(len(s)-1, -1, -1):
                if s[i] == '1':
                    num += n
                n *= 2
            return num

        def helper(curr, seen, curr_lst):
            if curr in seen:
                return None

            curr_lst.append(curr)
            seen.add(curr)

            if len(curr_lst) == 2**n:
                ones = 0
                for c in curr:
                    if c == '1':
                        ones += 1
                        if ones > 1:
                            return None
                return curr_lst[:]

            for i in range(len(curr)):
                r = '0' if curr[i] == '1' else '1' 
                res = helper(curr[:i] + r + curr[i+1:], seen, curr_lst)
                if res is not None:
                    return res
            seen.remove(curr)
            curr_lst.pop()
            return None

        res = helper('0'*n, set(), [])
        return [str_to_num(s) for s in res]
