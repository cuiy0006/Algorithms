class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        curr = 1
        up = True
        for i in range(1, len(arr)):
            if up:
                if arr[i] > arr[i - 1]:
                    curr += 1
                elif arr[i] < arr[i - 1]:
                    if curr == 1:
                        continue
                    else:
                        curr += 1
                        up = False
                else:
                    curr = 1
            else:
                if arr[i] > arr[i - 1]:
                    res = max(res, curr)
                    curr = 2
                    up = True
                elif arr[i] == arr[i - 1]:
                    res = max(res, curr)
                    curr = 1
                    up = True
                else:
                    curr += 1
                    
            if i == len(arr) - 1 and not up:
                res = max(res, curr)
                
        return res
