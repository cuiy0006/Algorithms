class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(curr_lst, curr_sum, curr_num):
            if curr_sum == n and len(curr_lst) == k:
                res.append(curr_lst[:])
                return
            elif curr_sum > n:
                return
            elif len(curr_lst) > k:
                return
            
            if curr_num > 9:
                return
            
            for num in range(curr_num, 10):
                curr_lst.append(num)
                helper(curr_lst, curr_sum + num, num + 1)
                curr_lst.pop()
        
        helper([], 0, 1)
        return res
