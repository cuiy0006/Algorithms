class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = [None for _ in range(len(nums2))]
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack) == 0:
                next_greater[i] = -1
            else:
                next_greater[i] = stack[-1]
            stack.append(nums2[i])
        
        dic = {}
        for i in range(len(nums2)):
            dic[nums2[i]] = next_greater[i]
        
        res = []
        for num in nums1:
            res.append(dic[num])
        return res
