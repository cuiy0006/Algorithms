class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = list(sorted(nums1))
        l2 = list(sorted(nums2))

        dic = defaultdict(list)
        l = 0
        r = len(l1)-1

        for i in range(len(l2)-1, -1, -1):
            if l2[i] >= l1[r]:
                dic[l2[i]].append(l1[l])
                l += 1
            else:
                dic[l2[i]].append(l1[r])
                r -= 1
        res = []
        for i in range(len(nums2)):
            res.append(dic[nums2[i]].pop())
        
        return res


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums1))]
        nums1.sort()
        nums2 = [(i, num) for i, num in enumerate(nums2)]
        nums2.sort(key=lambda x:-x[1])

        i = 0
        j = len(nums1)-1

        for k, num in nums2:
            if nums1[j] > num:
                res[k] = nums1[j]
                j -= 1
            else:
                res[k] = nums1[i]
                i += 1
        return res
