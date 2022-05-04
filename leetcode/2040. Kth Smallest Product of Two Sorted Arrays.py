import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        def count_smaller_or_equal(m):
            res = 0
            for i in range(len(nums1)):
                num1 = nums1[i]
                if num1 == 0:
                    if m >= 0:
                        res += len(nums2)
                elif num1 > 0:
                    target = m / num1
                    idx = bisect.bisect_right(nums2, target)
                    res += idx
                else:
                    target = m / num1
                    idx = bisect.bisect_left(nums2, target)
                    res += len(nums2)-idx
            return res
        
        left = -10000000000
        right = 10000000000
        
        while left < right:
            mid = (left + right) // 2
            cnt = count_smaller_or_equal(mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
                
        return left
