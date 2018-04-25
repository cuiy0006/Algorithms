class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(curr_lst, curr_num):
            if len(curr_lst) == k:
                res.append(curr_lst[:])
                return
            
            if curr_num > n:
                return
            
            for num in range(curr_num, n-(k - len(curr_lst))+2):
                curr_lst.append(num)
                helper(curr_lst, num + 1)
                curr_lst.pop()
        
        helper([], 1)
        return res
