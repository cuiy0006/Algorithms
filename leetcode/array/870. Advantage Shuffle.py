class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums1))]
        nums1.sort()
        nums2 = [(i, num) for i, num in enumerate(nums2)]
        nums2.sort(key=lambda x:-x[1])

        i = 0
        j = len(nums1)-1

        for k, num in nums2:
            if nums1[j] > num:
                res[k] = nums1[j]
                j -= 1
            else:
                res[k] = nums1[i]
                i += 1
        return res
