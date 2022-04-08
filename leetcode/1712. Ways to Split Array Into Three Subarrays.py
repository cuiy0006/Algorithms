class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        lst = []
        acc = 0
        res = 0
        
        for num in nums:
            acc += num
            lst.append(acc)
        
        right = 0
        for i in range(len(nums)-1, 1, -1):
            right += nums[i]
            total = lst[-1] - right
            m = 0
            n = i - 1
            
            while m < n:
                k = (m + n) // 2
                left = lst[k]
                mid = total - lst[k]
                if left <= mid:
                    if mid <= right:
                        n = k
                    else:
                        m = k + 1
                else:
                    n = k
                    
            if n == i - 1 or lst[n] > total - lst[n] or total - lst[n] > right:
                continue
                
            left_bound = n
            
            m = n + 1
            n = i - 1
            
            while m < n:
                k = (m + n) // 2
                
                left = lst[k]
                mid = total - lst[k]
                if left <= mid:
                    m = k + 1
                else:
                    n = k

            right_bound = m
            res += right_bound - left_bound
        
        return res % 1000000007
