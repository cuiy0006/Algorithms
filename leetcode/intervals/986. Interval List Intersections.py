class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        res = []
        while a < len(firstList) and b < len(secondList):
            [start_a, end_a] = firstList[a]
            [start_b, end_b] = secondList[b]
            if end_a < start_b:
                a += 1
            elif start_a > end_b:
                b += 1
            else:
                start = max(start_a, start_b)
                end = min(end_a, end_b)
                res.append([start, end])
                if end_a > end_b:
                    b += 1
                else:
                    a += 1
        return res
