class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s == goal[i:len(s)] + goal[0:i]:
                return True
        return False
