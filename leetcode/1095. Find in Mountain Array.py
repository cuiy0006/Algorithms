# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 1
        right = mountain_arr.length()-2
        peak = 1
        
        @cache
        def get_val(idx):
            return mountain_arr.get(idx)
        
        while left < right:
            mid = (left+right)//2
            if get_val(mid) > get_val(mid-1) and get_val(mid) > get_val(mid+1):
                peak = mid
                break
            elif get_val(mid) < get_val(mid-1):
                right = mid
            elif get_val(mid) < get_val(mid+1):
                left = mid+1
            if left == right:
                peak = left
 
        if target > get_val(peak) or target < min(get_val(0), get_val(mountain_arr.length()-1)):
            return -1
        
        left = 0
        right = peak
        while left < right:
            mid = (left+right)//2
            if get_val(mid) < target:
                left = mid+1
            else:
                right = mid
        
        if get_val(left) == target:
            return left
        
        left = peak
        right = mountain_arr.length()-1

        while left < right:
            mid = (left+right)//2
            if get_val(mid) > target:
                left = mid+1
            else:
                right = mid
        
        if get_val(left) == target:
            return left
        return -1
        
        
