class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()
        rows = [1] + hFences + [m]
        cols = [1] + vFences + [n]

        row_diffs = set()
        for i in range(len(rows)):
            for j in range(i+1, len(rows)):
                row_diffs.add(rows[j]-rows[i])

        res = -1
        for i in range(len(cols)):
            for j in range(i+1, len(cols)):
                d = cols[j]-cols[i]
                if d in row_diffs:
                    res = max(res, d*d)
        return res % (10**9+7) if res != -1 else -1
