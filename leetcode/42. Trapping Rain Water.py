class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        
        res = 0
        left_max = 0
        right_max = 0
        
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            
            while i < j and height[i] < height[j]:
                i += 1
                left_max = max(left_max, height[i])
                res += left_max - height[i]
            
            while i < j and height[i] >= height[j]:
                j -= 1
                right_max = max(right_max, height[j])
                res += right_max - height[j]
        
        return res




class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0,len(height)-1
        total = 0
        while l < r:
            if height[l] <= height[r]:
                tmp = height[l]
                while l < r and tmp >= height[l]:
                    total += tmp - height[l]
                    l += 1
            else:
                tmp = height[r]
                while l < r and tmp >= height[r]:
                    total += tmp - height[r]
                    r -= 1
        return total
