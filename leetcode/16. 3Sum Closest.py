class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_delta = sys.maxsize
        for k in range(2, len(nums)):
            i = 0
            j = k-1
            k_target = target - nums[k]
            while i < j:
                total = nums[i] + nums[j]
                delta = k_target-total
                if abs(delta) < abs(min_delta):
                    min_delta = delta
                if total == k_target:
                    return nums[i]+nums[j]+nums[k]
                elif total < k_target:
                    i += 1
                else:
                    j -= 1
        return target - min_delta

