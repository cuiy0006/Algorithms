class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        dic = {0:1} # curr_sum%k -> cnt
        cnt = 0
        
        for num in nums:
            curr_sum += num
            r = curr_sum % k
            if r in dic:
                cnt += dic[r]
            else:
                dic[r] = 0
            dic[r] += 1
        
        return cnt
                
        
