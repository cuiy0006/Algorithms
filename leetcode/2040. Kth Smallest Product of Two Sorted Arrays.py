class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def find_count(nums2, num, target):
            if num == 0:
                return len(nums2) if target >= 0 else 0
            
            target = target / num
            
            left = 0
            right = len(nums2)
            if num > 0:
                while left < right:
                    mid = (left + right) // 2
                    if nums2[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid
                return left
            else:
                while left < right:
                    mid = (left + right) // 2
                    if nums2[mid] >= target:
                        right = mid
                    else:
                        left = mid + 1
                return len(nums2) - left
                    
        
        left = -10000000000
        right = 10000000000
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        res = 0
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for num1 in nums1:
                cnt += find_count(nums2, num1, mid)
            
            if cnt >= k:
                res = mid
                right = mid
            else:
                left = mid + 1
        
        return res
