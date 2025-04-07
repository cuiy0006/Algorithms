class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = None
        c2 = None
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1 = num
                cnt1 = 1
            elif cnt2 == 0:
                c2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
        res = []
        if cnt1 > len(nums) / 3:
            res.append(c1)
        if cnt2 > len(nums) / 3:
            res.append(c2)
        return res
