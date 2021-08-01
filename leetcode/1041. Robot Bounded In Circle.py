class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        
        dic = {
            (0, 1, 'L'): (-1, 0),
            (0, 1, 'R'): (1, 0),
            (1, 0, 'L'): (0, 1),
            (1, 0, 'R'): (0, -1),
            (0, -1, 'L'): (1, 0),
            (0, -1, 'R'): (-1, 0),
            (-1, 0, 'L'): (0, -1),
            (-1, 0, 'R'): (0, 1)
        }
        
        d = (0, 1)
        
        # 
        for inst in instructions:
            if inst == 'G':
                pos[0] += d[0]
                pos[1] += d[1]
            else:
                d = dic[(d[0], d[1], inst)]
           
        return pos == [0, 0] and d == (0, 1) or d != (0, 1)
