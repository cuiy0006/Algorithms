class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        j = len(letters)
        
        target = ord(target)
        
        while i < j:
            mid = (i + j) // 2
            if ord(letters[mid]) > target:
                j = mid
            else:
                i = mid + 1
        
        if i == len(letters):
            return letters[0]
        
        return letters[i]
