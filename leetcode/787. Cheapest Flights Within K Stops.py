class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic = defaultdict(list) # from -> [(to, price)]
        
        for [f, to, price] in flights:
            dic[f].append((to, price))
            
        @cache
        def dfs(curr_loc, num_stop):
            if curr_loc == dst:
                return 0
            
            if num_stop > k:
                return -1
            
            if curr_loc not in dic:
                return -1
            
            min_price = -1
            for to, price in dic[curr_loc]:
                rest = dfs(to, num_stop+1)
                if rest >= 0:
                    if min_price == -1:
                        min_price = rest + price
                    else:
                        min_price = min(min_price, rest + price)
                    
            return min_price
        
        return dfs(src, 0)
