class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sl = SortedList()
        for i, num in enumerate(nums):
            j = i - indexDiff
            if j > 0:
                sl.remove(nums[j-1])
            idx = sl.bisect_left(num)
            if idx > 0 and abs(num-sl[idx-1]) <= valueDiff:
                return True
            if idx < len(sl) and abs(num-sl[idx]) <= valueDiff:
                return True
            sl.add(num)
        return False
