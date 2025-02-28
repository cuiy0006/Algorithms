class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def helper(a, b, seen):
            if a + b == target:
                return True
            if (a, b) in seen:
                return False
            seen.add((a, b))
            if helper(0, b, seen):
                return True
            if helper(a, 0, seen):
                return True
            if helper(x, b, seen):
                return True
            if helper(a, y, seen):
                return True
            if y-b > a:
                if helper(0, a+b, seen):
                    return True
            else:
                if helper(a-(y-b), y, seen):
                    return True
            if x-a > b:
                if helper(a+b, 0, seen):
                    return True
            else:
                if helper(x, b-(x-a), seen):
                    return True
            return False

        return helper(0, 0, set())

