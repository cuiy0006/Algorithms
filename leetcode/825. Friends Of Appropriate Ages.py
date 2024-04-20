class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        dic = defaultdict(int)
        for age in ages:
            dic[age] += 1

        ages.sort()
        res = 0
        l = 0
        for x in range(1, len(ages)):
            lower = 0.5 * ages[x] + 7
            r = x
            while l < r:
                mid = (l + r) // 2
                if lower >= ages[mid]:
                    l = mid + 1
            else:
                    r = mid
            res += x - l

        for age in dic:
            n = dic[age]
            if age <= 0.5 * age + 7:
                continue
            res += (n - 1) * n // 2
        return res

