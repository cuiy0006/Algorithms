class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            curr = 0
            for j in range(i, len(arr)):
                curr += arr[j]
                if (j - i) % 2 == 0:
                    res += curr
        
        return res
