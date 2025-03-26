class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [tuple(stone) for stone in stones]
        parent = {stone:stone for stone in stones}
        def find_ancestor(node):
            if parent[node] == node:
                return node
            parent[node] = find_ancestor(parent[node])
            return parent[node]
        
        row_to_stone = {}
        col_to_stone = {}
        for stone in stones:
            if stone[0] not in row_to_stone:
                row_to_stone[stone[0]] = stone
            else:
                parent[find_ancestor(stone)] = find_ancestor(row_to_stone[stone[0]])

            if stone[1] not in col_to_stone:
                col_to_stone[stone[1]] = stone
            else:
                parent[find_ancestor(stone)] = find_ancestor(col_to_stone[stone[1]])

        s = set()
        for stone in stones:
            ancestor = find_ancestor(stone)
            if ancestor not in s:
                s.add(ancestor)
        return len(stones) - len(s)

