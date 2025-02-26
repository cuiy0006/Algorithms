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
