class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = len(nums1) - 1
        while i >= 0:
            nums1[j] = nums1[i]
            i -= 1
            j -= 1
            
        i = j + 1
        j = 0
        idx = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums1[idx] = nums1[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1
        
        while i < len(nums1):
            nums1[idx] = nums1[i]
            idx += 1
            i += 1
            
        while j < len(nums2):
            nums1[idx] = nums2[j]
            idx += 1
            j += 1
            
            
            
            
            
 class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        
        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
            
        
