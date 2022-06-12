
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dic = defaultdict(int)
        for num in arr:
            dic[num] += 1
        
        nums = list(dic.keys())
        nums.sort()
    
        def factorial(n):
            res = 1
            while n > 1:
                res *= n
                n -= 1
            return res
        
        res = 0
        for k in range(len(nums)):
            i = k+1
            j = len(nums)-1
            while i < j:
                total = nums[k]+nums[i]+nums[j]
                if total == target:
                    res += dic[nums[k]]*dic[nums[i]]*dic[nums[j]]
                    i += 1
                    j -= 1
                elif total > target:
                    j -= 1
                else:
                    i += 1
            
            for i in range(k+1, len(nums)):
                if nums[k]+2*nums[i] == target and dic[nums[i]] >= 2:
                    cnt = dic[nums[i]]
                    res += dic[nums[k]] * factorial(cnt) // factorial(2) // factorial(cnt-2)
                if nums[k]*2+nums[i] == target and dic[nums[k]] >= 2:
                    cnt = dic[nums[k]]
                    res += dic[nums[i]] * factorial(cnt) // factorial(2) // factorial(cnt-2)
            
            if dic[nums[k]] >= 3 and 3 * nums[k] == target:
                cnt = dic[nums[k]]
                res += factorial(cnt) // factorial(3) // factorial(cnt-3)
            
            res %= 1000000007

        return res
