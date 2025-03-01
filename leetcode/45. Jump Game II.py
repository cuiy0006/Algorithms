class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        furthest = 0
        k = 1
        idx = 0

        q = deque([0])
        while len(q) != 0:
            size = len(q)
            idx = furthest
            for _ in range(size):
                curr = q.popleft()
                furthest = max(furthest, curr+nums[curr])
                if furthest >= len(nums)-1:
                    return k
            k += 1
            for i in range(idx+1, furthest+1):
                q.append(i)
        
        return -1

