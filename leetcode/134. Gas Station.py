class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            curr = 0
            j = i
            while j < len(gas):
                curr += gas[j] - cost[j]
                if curr < 0:
                    i = j + 1
                    break
                j += 1
            if j == len(gas):
                j = 0
                while j < i:
                    curr += gas[j] - cost[j]
                    if curr < 0:
                        return -1
                    j += 1
                return i
        return -1
