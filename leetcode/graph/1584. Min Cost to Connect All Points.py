class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distances.append(
                    (i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))

        distances.sort(key=lambda d:d[2])
        parent = {node:node for node in range(len(points))}
        def find_root(node):
            if parent[node] == node:
                return node
            parent[node] = find_root(parent[node])
            return parent[node]
        
        total = 0
        for [x, y, distance] in distances:
            x_root = find_root(x)
            y_root = find_root(y)
            if x_root != y_root:
                total += distance
                parent[x_root] = parent[y_root]
        return total

