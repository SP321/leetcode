class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        left_sum = [0] * n
        stack = []
        acc_sum = 0
        for i, h in enumerate(maxHeights):
            current_count = 1
            while stack and stack[-1][0] > h:
                height, count = stack.pop()
                acc_sum -= height * count
                current_count += count
            stack.append((h, current_count))
            acc_sum += h * current_count
            left_sum[i] = acc_sum

        right_sum = [0] * n
        stack = []
        acc_sum = 0
        for i in range(n - 1, -1, -1):
            h = maxHeights[i]
            current_count = 1
            while stack and stack[-1][0] > h:
                height, count = stack.pop()
                acc_sum -= height * count
                current_count += count
            stack.append((h, current_count))
            acc_sum += h * current_count
            right_sum[i] = acc_sum

        ans = 0
        for i in range(n):
            ans = max(ans, left_sum[i] + right_sum[i] - maxHeights[i])
        return ans