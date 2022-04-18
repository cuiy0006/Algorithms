class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        k_to_lines = {}
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                
                if p1[0] == p2[0]:
                    k = 'inf'
                else:
                    k = (p1[1] - p2[1]) / (p1[0] - p2[0])
                
                if k not in k_to_lines:
                    k_to_lines[k] = []
                k_to_lines[k].append((tuple(p1), tuple(p2)))
        
        def find_ancestor(p, dic):
            while p in dic and dic[p] != p:
                p = dic[p]
            return p
        
        res = 0
        for lst in k_to_lines.values():
            dic = {}
            for (p1, p2) in lst:
                ancestor1 = find_ancestor(p1, dic)
                ancestor2 = find_ancestor(p2, dic)
                dic[ancestor1] = ancestor1
                dic[p1] = ancestor1
                dic[ancestor2] = ancestor1
                dic[p2] = ancestor1
            
            ancestor_to_p = {}
            for p in dic:
                ancestor = find_ancestor(p, dic)
                if ancestor not in ancestor_to_p:
                    ancestor_to_p[ancestor] = []
                ancestor_to_p[ancestor].append(p)
                res = max(res, len(ancestor_to_p[ancestor]))
        return res




class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        res = 0
        
        for i in range(len(points)):
            [x1, y1] = points[i]
            kp_to_cnt = {}
            for j in range(i+1, len(points)):
                [x2, y2] = points[j]
                
                if x1 == x2:
                    k = 'inf'
                else:
                    k = (y1 - y2) / (x1 - x2)
                if (k, i) not in kp_to_cnt:
                    kp_to_cnt[(k, i)] = 1
                kp_to_cnt[(k, i)] += 1
                res = max(res, kp_to_cnt[(k, i)])
        
        return res
                    
