class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix[0])
        height = [0] * (m + 1)
        ans = 0

        for row in matrix:
            for i in range(m):
                height[i] = height[i] + 1 if row[i] == '1' else 0

            stack = [-1]
            for i in range(m + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)

        return ans