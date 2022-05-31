from bisect import bisect_left

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        def merge_interval(interval, arr):
            res = []
            i = 0
            while i < len(arr):
                [start, end] = arr[i]
                if end < interval[0]:
                    res.append(arr[i])
                elif start > interval[1]:
                    break
                else:
                    interval[0] = min(interval[0], start)
                    interval[1] = max(interval[1], end)
                i += 1
            res.append(interval)
            while i < len(arr):
                res.append(arr[i])
                i += 1
            return res
        
        painted = []
        res = []
        for i, [start, end] in enumerate(paint):
            idx = bisect_left(painted, [start, end])
            left = start
            right = end
            if idx != 0:
                if painted[idx-1][1] > start:
                    left = painted[idx-1][0]
                    idx -= 1

            total = 0
            j = idx
            while j < len(painted):
                if painted[j][0] >= right:
                    break
                right = max(right, painted[j][1])
                total += painted[j][1] - painted[j][0]
                j += 1

            res.append(right-left-total)
            
            painted = merge_interval([start, end], painted)
        
        return res
