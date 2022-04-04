class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def find_comb(idx, curr_sum, curr_lst):
            if curr_sum == target:
                res.append(curr_lst[:])
                return
            
            if idx > len(candidates) - 1:
                return
            
            while curr_sum <= target:
                find_comb(idx+1, curr_sum, curr_lst)
                curr_sum += candidates[idx]
                curr_lst.append(candidates[idx])
            
            while len(curr_lst) > 0 and curr_lst[-1] == candidates[idx]:
                curr_lst.pop()
                
        find_comb(0, 0, [])
        return res
