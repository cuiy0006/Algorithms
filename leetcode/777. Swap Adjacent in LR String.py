class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start = list(start)
        end = list(end)
        
        l_lst = []
        r_lst = []
        
        for i in range(len(start)):
            if start[i] == 'L' and len(r_lst) != 0:
                return False
            
            if end[i] == 'R' and len(l_lst) != 0:
                return False
            
            if start[i] == end[i]:
                continue
            
            if start[i] == 'L' and end[i] == 'R' or start[i] == 'R' and end[i] == 'L':
                return False
            
            if start[i] == 'L' and end[i] == 'X':
                if len(l_lst) == 0:
                    return False
                idx = l_lst.pop()
                end[idx], end[i] = end[i], end[idx]
            
            elif start[i] == 'R' and end[i] == 'X':
                r_lst.append(i)

            elif start[i] == 'X' and end[i] == 'L':
                l_lst.append(i)
            elif start[i] == 'X' and end[i] == 'R':
                if len(r_lst) == 0:
                    return False
                idx = r_lst.pop()
                start[idx], start[i] = start[i], start[idx]
            
            
        return start == end
            
