class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        
        res = 0
        count = 0
        for [num_b, num_u] in boxTypes:
            if num_b + count < truckSize:
                count += num_b
                res += num_b * num_u
            else:
                res += (truckSize - count) * num_u
                break
        
        return res
