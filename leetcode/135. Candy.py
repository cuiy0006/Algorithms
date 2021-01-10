class Solution:
    def candy(self, ratings: List[int]) -> int:
        lst = [1 for r in ratings]
        i = 1
        while i < len(ratings):
            if ratings[i] > ratings[i - 1]:
                lst[i] = lst[i - 1] + 1
            i += 1
        
        j = len(ratings) - 2
        while j >= 0:
            if ratings[j] > ratings[j + 1]:
                lst[j] = max(lst[j], lst[j + 1] + 1)
            j -= 1
        
        return sum(lst)
