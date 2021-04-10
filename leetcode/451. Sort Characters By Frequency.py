from heapq import heappush, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        
        lst = [(freq, c) for c, freq in dic.items()]
        
        def quicksort(lst, l, r):
            if l >= r:
                return
            
            pivot = lst[l][0]
            left = l + 1
            right = r
            while left < right:
                while left < right and lst[left][0] >= pivot:
                    left += 1
                
                while left < right and lst[right][0] <= pivot:
                    right -= 1
                
                lst[left], lst[right] = lst[right], lst[left]
                
            if lst[left][0] < pivot:
                left -= 1
            lst[left], lst[l] = lst[l], lst[left]
            quicksort(lst, l, left - 1)
            quicksort(lst, left + 1, r)
        
        quicksort(lst, 0, len(lst) - 1)
        
        return ''.join([freq * c for freq, c in lst])
