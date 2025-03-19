class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        def helper(i1, i2, k):
            if i1 == m:
                return nums2[i2+k-1]
            if i2 == n:
                return nums1[i1+k-1]
            
            if k == 1:
                return min(nums1[i1], nums2[i2])
            
            # leftover1 <= leftover2
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
        
        if (m + n) % 2 == 1:
            return helper(0, 0, (m + n) // 2 + 1)
        else:
            return (helper(0, 0, (m + n) // 2) + helper(0, 0, (m + n) // 2 + 1)) / 2
        
#                 i1+k1
#                  |
#  nums1 xx i1 xxxxxxx  m
#  nums2 xxxx i2 xxxxx  n
#                  |
#                 i2+k2

#  leftover1 = m - i1
#  leftover2 = n - i2
#
#   k1, k2 are how many we would proceed in nums1 and nums2
#   k2 = min(k/2, n-i2) 
#   k1 = min(k/2, m-i1)

#   We want to advance k/2, 
#   nums1[i1 + k1 - 1] > nums2[i2 + k2 - 1] ---> target must be at (i1, m) or (i2+k2, n)
#   nums1[i1 + k1 - 1] < nums2[i2 + k2 - 1] ---> target must be at (i1+k1, m) or (i2, n)

# 
#
