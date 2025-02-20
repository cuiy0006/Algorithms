class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        j = k-1
        while j < len(arr):
            if j == len(arr)-1:
                return arr[i:]
            if x-arr[i] <= arr[j+1]-x:
                return arr[i:j+1]
            i += 1
            j += 1
        return None



class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)
        while l < r:
            mid = (l+r)//2
            if arr[mid] < x:
                l = mid+1
            else:
                r = mid
        i = l-1
        j = l
        left_res = []
        right_res = []
        for _ in range(k):
            if i < 0:
                right_res.append(arr[j])
                j += 1
            elif j > len(arr)-1:
                left_res.append(arr[i])
                i -= 1
            else:
                if abs(arr[i]-x) <= abs(arr[j]-x):
