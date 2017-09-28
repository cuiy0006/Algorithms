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
