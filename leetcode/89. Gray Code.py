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
        def helper(curr, seen, curr_lst):
            if curr in seen:
                return None

            curr_lst.append(curr)
            seen.add(curr)

            if len(curr_lst) == 2**n:
                ones = 0
                tmp = curr
                while tmp != 0:
                    if tmp & 1 == 1:
                        ones += 1
                        if ones > 1:
                            return None
                    tmp = tmp >> 1
                return curr_lst[:]

            k = 0
            tmp = 1
            while k < n:
                res = helper(curr^tmp, seen, curr_lst)
                if res is not None:
                    return res
                tmp = tmp<<1
            seen.remove(curr)
            curr_lst.pop()
            return None

