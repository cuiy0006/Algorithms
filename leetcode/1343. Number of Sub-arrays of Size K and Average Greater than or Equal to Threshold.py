class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        i = 0
        j = k
        
        res = 0
        if total / k >= threshold:
            res += 1
        
        while j < len(arr):
            total += arr[j] - arr[i]
            if total / k >= threshold:
                res += 1
            i += 1
            j += 1
        
        return res
