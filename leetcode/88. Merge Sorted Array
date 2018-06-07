class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = len(nums1) - 1
        while i >= 0:
            nums1[j] = nums1[i]
            i -= 1
            j -= 1
        i = j + 1
        j = 0
        k = 0
        while i < len(nums1) and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1):
            nums1[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
