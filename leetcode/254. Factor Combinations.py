class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def helper(curr_lst, rest, last_factor):
            if rest != n:
                curr_lst.append(rest)
                res.append(curr_lst[:])
                curr_lst.pop()

            for num in range(last_factor, int(rest**0.5)+1):
                if rest % num == 0:
                    curr_lst.append(num)
                    helper(curr_lst, rest//num, num)
                    curr_lst.pop()
        
        helper([], n, 2)
        return res
