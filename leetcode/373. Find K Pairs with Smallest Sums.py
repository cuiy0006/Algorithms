class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = [(nums1[0]+nums2[0], 0, 0)]
        res = []
        seen = set()
        while len(h) != 0:
            total, i, j = heappop(h)
            res.append([nums1[i], nums2[j]])
            if len(res) == k:
                break
            if i+1 < len(nums1) and (i+1, j) not in seen:
                seen.add((i+1, j))
                heappush(h, (nums1[i+1]+nums2[j], i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in seen:
                seen.add((i, j+1))
                heappush(h, (nums1[i]+nums2[j+1], i, j+1))
        return res
