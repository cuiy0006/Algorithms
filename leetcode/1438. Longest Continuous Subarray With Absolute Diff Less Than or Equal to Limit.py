class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        i = 0
        j = 0
        res = 0
        while j < len(nums):
            while len(min_dq) != 0 and abs(nums[min_dq[0]]-nums[j]) > limit:
                idx = min_dq.popleft()
                while len(max_dq) != 0 and max_dq[0] <= idx:
                    max_dq.popleft()
                i = max(i, idx+1)
            while len(max_dq) != 0 and abs(nums[max_dq[0]]-nums[j]) > limit:
                idx = max_dq.popleft()
                while len(min_dq) != 0 and min_dq[0] <= idx:
                    min_dq.popleft()
                i = max(i, idx+1)
            res = max(res, j-i+1)

            while len(max_dq) != 0 and nums[max_dq[-1]] < nums[j]:
                max_dq.pop()
            max_dq.append(j)
            while len(min_dq) != 0 and nums[min_dq[-1]] > nums[j]:
                min_dq.pop()
            min_dq.append(j)
            j += 1
        return res






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
