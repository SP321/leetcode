class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n

        closest_larger_left = [None] * n
        closest_larger_right = [None] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                if i - stack[-1] <= d:
                    closest_larger_left[stack[-1]] = i
                stack.pop()
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                if stack[-1] - i <= d:
                    closest_larger_right[stack[-1]] = i
                stack.pop()
            stack.append(i)

        for i, height in sorted(enumerate(arr), key=lambda x: x[1]):
            if closest_larger_left[i] is not None:
                dp[closest_larger_left[i]] = max(dp[closest_larger_left[i]], dp[i] + 1)
            if closest_larger_right[i] is not None:
                dp[closest_larger_right[i]] = max(dp[closest_larger_right[i]], dp[i] + 1)

        return max(dp)