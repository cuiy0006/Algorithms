class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = list(sorted(nums))
        groups = []
        i = 0
        j = 1
        while j < len(sorted_nums):
            if sorted_nums[j]-sorted_nums[j-1] <= limit:
                j += 1
                continue
            groups.append(sorted_nums[i:j])
            i = j
            j += 1
        groups.append(sorted_nums[i:j])
        num_to_group = {}
        for i in range(len(groups)):
            groups[i].sort(key=lambda x:-x)
            for num in groups[i]:
                num_to_group[num] = groups[i]

        for i in range(len(nums)):
            nums[i] = num_to_group[nums[i]][-1]
            num_to_group[nums[i]].pop()

        return nums

