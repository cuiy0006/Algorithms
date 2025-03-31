class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i):
                if bombs[i] == bombs[j]:
                    continue
                d = ((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)**0.5
                if d <= bombs[i][2]:
                    dic[tuple(bombs[i])].append(tuple(bombs[j]))
                if d <= bombs[j][2]:
                    dic[tuple(bombs[j])].append(tuple(bombs[i]))

        count = defaultdict(int)
        for bomb in bombs:
            count[tuple(bomb)] += 1

        def get_cnt(bomb, seen):
            if bomb in seen:
                return 0
            seen.add(bomb)
            res = count[bomb]
            for child in dic[bomb]:
                res += get_cnt(child, seen)
            return res

        res = 0
        for bomb in bombs:
            res = max(res, get_cnt(tuple(bomb), set()))
        return res
