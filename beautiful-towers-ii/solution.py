class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        def push_to_stack(stack, h):
            count = 1
            running_sum = 0 if not stack else stack[-1][2]
            while stack and stack[-1][0] > h:
                x, c, _ = stack.pop()
                running_sum -= x * c
                count += c
            running_sum += h * count
            stack.append((h, count, running_sum))
            return running_sum

        l_r_stack = []
        r_l_stack = []

        left_sum = [push_to_stack(l_r_stack, h) for h in maxHeights]
        right_sum = [push_to_stack(r_l_stack, h) for h in reversed(maxHeights)]
        right_sum = right_sum[::-1]

        ans = 0
        for i in range(n):
            ans = max(ans, left_sum[i] + right_sum[i] - maxHeights[i])

        return ans