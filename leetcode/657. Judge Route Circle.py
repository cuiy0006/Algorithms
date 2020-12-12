class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        R = 0
        U = 0
        for move in moves:
            if move == 'R':
                R += 1
            elif move == 'L':
                R -= 1
            elif move == 'U':
                U += 1
            else:
                U -= 1
        return R == 0 and U == 0
