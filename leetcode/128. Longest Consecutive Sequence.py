class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        res = 0
        
        for num in nums:
            seen.add(num)
            
        for num in nums:
            if num in seen:
                cnt = 1
                seen.remove(num)
                curr = num + 1
                while curr in seen:
                    cnt += 1
                    seen.remove(curr)
                    curr += 1
                    
                curr = num - 1
                while curr in seen:
                    cnt += 1
                    seen.remove(curr)
                    curr -= 1
                res = max(res, cnt)
        
        return res
