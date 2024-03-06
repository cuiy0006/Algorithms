class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        prefix = [0]
        for num in nums:
            if len(prefix) == 1:
                prefix.append(num)
            else:
                prefix.append(prefix[-1]+num)

        def sort(i, j):
            if i >= j:
                return
            mid = (i + j)//2
            sort(i, mid)
            sort(mid+1, j)
            merge(i, j, mid)

        tmp = [None for _ in prefix]
        def merge(i, j, mid):
            nonlocal count
            start = mid+1
            end = mid+1
            for k in range(i, mid+1):
                while start <= j and prefix[start] - prefix[k] < lower:
                    start += 1
                while end <= j and prefix[end] - prefix[k] <= upper:
                    end += 1 
                count += end - start

            for k in range(i, j+1):
                tmp[k] = prefix[k]

            t1 = i
            t2 = mid+1
            for k in range(i, j+1):
                if t1 > mid:
                    prefix[k] = tmp[t2]
                    t2 += 1
                elif t2 > j:
                    prefix[k] = tmp[t1]
                    t1 += 1
                elif tmp[t1] < tmp[t2]:
                    prefix[k] = tmp[t1]
                    t1 += 1
                else:
                    prefix[k] = tmp[t2]
                    t2 += 1

        sort(0, len(prefix)-1)
        return count

