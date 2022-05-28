class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        res = []
        
        curr = 2
        curr_sum = 0
        while curr_sum < finalSum:
            curr_sum += curr
            res.append(curr)
            curr += 2
        
        if curr_sum == finalSum:
            return res
        else:
            curr_sum -= curr-2
            res.pop()

        last = finalSum - curr_sum
        if last <= res[-1]:
            res[-1] += last
        else:
            res.append(last)
        return res
            
        
