class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] - 1 >= k:
            return k

        k -= arr[0] - 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > k:
                return arr[i-1] + k
            k -= arr[i] - arr[i-1] - 1
        
        return arr[-1] + k
