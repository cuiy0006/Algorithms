class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = list(tiles)
        cnt = 0
        def dfs(idx):
            if idx != 0:
                nonlocal cnt
                cnt += 1
            if idx == len(tiles):
                return
            seen = set()
            for i in range(idx, len(tiles)):
                if tiles[i] in seen:
                    continue
                seen.add(tiles[i])
                tiles[i], tiles[idx] = tiles[idx], tiles[i]
                dfs(idx+1)
                tiles[i], tiles[idx] = tiles[idx], tiles[i]
        
        dfs(0)
        return cnt



class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        dic = {}
        for tile in tiles:
            if tile not in dic:
                dic[tile] = 0
            dic[tile] += 1
        
        def helper():
            if len(dic) == 0:
                return 0
            res = 0
            tiles = list(dic.keys())
            for tile in tiles:
                res += 1
                dic[tile] -= 1
                if dic[tile] == 0:
                    del dic[tile]
                res += helper()
                if tile not in dic:
                    dic[tile] = 0
                dic[tile] += 1
            return res
        return helper()
