from sortedcontainers import SortedDict

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        dic = SortedDict() # num -> [idx]
        res = 0
        
        for i in range(len(nums)):
            while len(dic) > 0 and abs(dic.peekitem(0)[0] - nums[i]) > limit:
                val, idxs = dic.peekitem(0)
                left = max(left, idxs[-1]+1)
                del dic[val]
            
            while len(dic) > 0 and abs(dic.peekitem()[0] - nums[i]) > limit:
                val, idxs = dic.peekitem()
                left = max(left, idxs[-1]+1)
                del dic[val]

            res = max(res, i-left+1)
            if nums[i] not in dic:
                dic[nums[i]] = []
            
            dic[nums[i]].append(i)
        
        return res
