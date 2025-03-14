class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[:]
        stack = deque()
        for i in range(len(dp)):
            while len(stack) != 0 and i - stack[0] > k:
                stack.popleft()

            if len(stack) != 0:
                dp[i] = max(dp[i], dp[stack[0]] + nums[i])

            while len(stack) != 0 and dp[i] >= dp[stack[-1]]:
                stack.pop()
            stack.append(i)

        return max(dp)

