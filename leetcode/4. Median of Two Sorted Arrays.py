class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        
        def helper(i1, i2, k):
            if i1 == m:
                return nums2[i2+k-1]
            if i2 == n:
                return nums1[i1+k-1]
            
            if k == 1:
                return min(nums1[i1], nums2[i2])
            
            if m - i1 <= n - i2:
                if i1 + k // 2 >= m:
                    k1 = m - i1
                else:
                    k1 = k // 2
                k2 = k - k1
            else:
                if i2 + k // 2 >= n:
                    k2 = n - i2
                else:
                    k2 = k // 2
                k1 = k - k2
            
            if nums1[i1 + k1 - 1] > nums2[i2 + k2 - 1]:
                return helper(i1, i2 + k2, k - k2)
            else:
                return helper(i1 + k1, i2, k - k1)
            
        m = len(nums1)
        n = len(nums2)
        
        if (m + n) % 2 == 1:
            return helper(0, 0, (m + n) // 2 + 1)
        else:
            return (helper(0, 0, (m + n) // 2) + helper(0, 0, (m + n) // 2 + 1)) / 2



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        
        left = 0
        right = len(nums1)
        i = j = 0
        while left <= right:
            i = (left + right)//2
            j = (m + n + 1)//2 - i
            if (i == 0 or nums1[i-1] <= nums2[j]) and (i ==m or nums2[j-1] <= nums1[i]):
                break
            elif i > 0 and nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                left = i + 1
                
        if i == 0:
            left_max = nums2[j-1]
        elif j == 0:
            left_max = nums1[i-1]
        else:
            left_max = max(nums1[i-1], nums2[j-1])
        if (m + n) % 2 == 1:
            return left_max / 1.0
        
        if i == m:
            right_min = nums2[j]
        elif j == n:
            right_min = nums1[i]
        else:
            right_min = min(nums1[i], nums2[j])
        
        return (left_max + right_min) / 2.0
