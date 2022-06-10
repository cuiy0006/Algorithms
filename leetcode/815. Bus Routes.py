class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        q = deque()
        targets = set()
        graph = defaultdict(set) # bus -> list[bus]
        routes = [set(route) for route in routes]

        for bus1 in range(len(routes)):
            for bus2 in range(len(routes)):
                if bus1 == bus2:
                    continue
                if any(s in routes[bus2] for s in routes[bus1]):
                    graph[bus1].add(bus2)
                    graph[bus2].add(bus1)

        for bus, route in enumerate(routes):
            if source in route:
                q.append(bus)
            if target in route:
                targets.add(bus)

        seen = set()
        d = 1
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                bus = q.popleft()
                if bus in targets:
                    return d
                seen.add(bus)
                for child_bus in graph[bus]:
                    if child_bus in seen:
                        continue
                    q.append(child_bus)
            d += 1
        
        return -1



# timeout, use station as node
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = defaultdict(set) # station -> [station]
        
        for route in routes:
            s = set(route)
            for i in range(len(route)):
                curr = s.copy()
                dic[route[i]] |= curr

        seen = set()
        q = deque([source])

        d = 0
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                station = q.popleft()
                seen.add(station)
                if station == target:
                    return d
                for next_station in dic[station]:
                    if next_station in seen:
                        continue
                    q.append(next_station)
            d += 1
        
        return -1
            
         
