class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m
        
        while left < right:
            mid = (left+right)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid+1
            else:
                right = mid

        if left == 0:
            return False
        row = matrix[left-1]
        
        left = 0
        right = n
        
        while left < right:
            mid = (left+right)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid+1
            else:
                right = mid
        
        return False
        
        
