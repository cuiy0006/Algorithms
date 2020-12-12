class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        
        def helper(curr_lst, curr_sum, index):
            if curr_sum == target:
                res.append(curr_lst[:])
                return
            elif curr_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr_lst.append(candidates[i])
                helper(curr_lst, curr_sum + candidates[i], i+1)
                curr_lst.pop()
        
        helper([], 0, 0)
        return res
