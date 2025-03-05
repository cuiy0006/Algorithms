class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        d = 3
        while d < len(nums):
            while d < len(nums)-1 and nums[d] == nums[d+1]:
                d += 1
            c = 2
            while c < d:
                while c < d-1 and nums[c] == nums[c+1]:
                    c += 1
                a = 0
                b = c-1
                while a < b:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        a += 1
                    elif total > target:
                        b -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        a += 1
                        b -= 1
                        while a < b and nums[a] == nums[a-1]:
                            a += 1
                        while a < b and nums[b] == nums[b+1]:
                            b -= 1
                c += 1
            d += 1
        return res

