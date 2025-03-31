class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque([0])
        while len(q) != 0:
            room = q.popleft()
            if room in visited:
                continue
            visited.add(room)
            if len(visited) == len(rooms):
                return True
            for key in rooms[room]:
                q.append(key)
        return False
