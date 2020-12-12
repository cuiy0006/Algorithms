#1
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def lengthSquare(v1, v2):
            return (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2
        lens = [lengthSquare(p1,p2),lengthSquare(p1,p3),lengthSquare(p1,p4), lengthSquare(p2,p3), lengthSquare(p2,p4), lengthSquare(p3,p4)]
        maxlen = max(lens)
        if len([l for l in lens if l == maxlen]) != 2:
            return False
        minlen = 0
        for l in lens:
            if l != maxlen:
                minlen = l
                break
        return len([l for l in lens if l == minlen]) == 4



#mine
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def isParallel(v1, v2):
            if v1[1] == 0 or v2[1] == 0:
                if v1[1] == v2[1]:
                    return True
                else:
                    return False
            if abs(v1[0] * v2[1]) == abs(v2[0] * v1[1]):
                return True
            return False
        
        def equalDegree(v1, v2):
            if v1[0] * v2[0] + v1[1] * v2[1] == 0:
                return True
            return False
        
        if p1[0]-p2[0]==0 and p1[1]-p2[1]==0 or p1[0]-p3[0]==0 and p1[1]-p3[1]==0 or p1[0]-p4[0]==0 and p1[1]-p4[1]==0 or p2[0]-p3[0]==0 and p2[1]-p3[1]==0 or p2[0]-p4[0]==0 and p2[1]-p4[1]==0 or p3[0]-p4[0]==0 and p3[1]-p4[1]==0:
            return False
        
        if isParallel((p1[0]-p2[0], p1[1]-p2[1]), (p3[0]-p4[0], p3[1]-p4[1])):
            if isParallel((p1[0]-p3[0], p1[1]-p3[1]), (p2[0]-p4[0], p2[1]-p4[1])):
                if equalDegree((p1[0]-p3[0], p1[1]-p3[1]), (p1[0]-p2[0], p1[1]-p2[1])):
                    if (p3[0]-p1[0])**2 + (p3[1]-p1[1])**2==(p2[0]-p1[0])**2 + (p2[1]-p1[1])**2:
                        return True
            if isParallel((p1[0]-p4[0], p1[1]-p4[1]), (p2[0]-p3[0], p2[1]-p3[1])):
                if equalDegree((p1[0]-p4[0], p1[1]-p4[1]), (p1[0]-p2[0], p1[1]-p2[1])):
                    if (p4[0]-p1[0])**2 + (p4[1]-p1[1])**2==(p2[0]-p1[0])**2 + (p2[1]-p1[1])**2:
                        return True
        if isParallel((p1[0]-p4[0], p1[1]-p4[1]), (p2[0]-p3[0], p2[1]-p3[1])):
            if isParallel((p1[0]-p3[0], p1[1]-p3[1]), (p2[0]-p4[0], p2[1]-p4[1])):
                if equalDegree((p1[0]-p3[0], p1[1]-p3[1]), (p1[0]-p4[0], p1[1]-p4[1])):
                    if (p3[0]-p1[0])**2 + (p3[1]-p1[1])**2==(p4[0]-p1[0])**2 + (p4[1]-p1[1])**2:
                        return True
        return False
