class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        dic = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i):
                num = nums[i]+nums[j]
                if (int(num**0.5)) ** 2 == num:
                    dic[nums[i]].add(nums[j])
                    dic[nums[j]].add(nums[i])

        def get_count(idx):
            if idx == len(nums):
                return 1
            res = 0
            seen = set()
            for i in range(idx, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                if idx == 0 or nums[i] in dic[nums[idx-1]]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    res += get_count(idx+1)
                    nums[i], nums[idx] = nums[idx], nums[i]
            return res
        
        return get_count(0)
