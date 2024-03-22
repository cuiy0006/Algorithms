num_map = {
    '0': ['1', '9'],
    '1': ['2', '0'],
    '2': ['3', '1'],
    '3': ['4', '2'],
    '4': ['5', '3'],
    '5': ['6', '4'],
    '6': ['7', '5'],
    '7': ['8', '6'],
    '8': ['9', '7'],
    '9': ['0', '8']
}

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set()
        deadends = set(deadends)
        if target in deadends:
            return -1
        height = 0
        q = deque(['0000'])

        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr == target:
                    return height
                if curr in deadends or curr in seen:
                    continue
                seen.add(curr)
                lst = list(curr)
                for i, c in enumerate(lst):
                    for c1 in num_map[c]:
                        lst[i] = c1
                        s = ''.join(lst)
                        q.append(s)
                        lst[i] = c
            height += 1
        return -1


