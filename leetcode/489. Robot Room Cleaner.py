# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        
        def dfs(x, y, d):
            robot.clean()
            
            for i in range(1, len(directions)+1):
                next_d = (d + i) % 4
                
                next_x = x + directions[next_d][0]
                next_y = y + directions[next_d][1]
                
                robot.turnRight()
                
                if (next_x, next_y) in visited:
                    continue
                visited.add((next_x, next_y))
                
                if not robot.move():
                    continue
                dfs(next_x, next_y, next_d)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
                
        dfs(0, 0, 0)
                
