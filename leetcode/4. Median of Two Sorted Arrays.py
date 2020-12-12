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
