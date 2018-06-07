class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(curr_lst, curr_sum, index):
            if curr_sum == target:
                res.append(curr_lst[:])
                return
            elif curr_sum > target:
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                tmp = curr_sum
                while tmp <= target:
                    tmp += num
                    curr_lst.append(num)
                    helper(curr_lst, tmp, i+1)
                while tmp != curr_sum:
                    tmp -= num
                    curr_lst.pop()
            
        helper([], 0, 0)
        return res
