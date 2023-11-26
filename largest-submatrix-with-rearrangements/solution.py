class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        ans= 0
        for j in range(m):
            for i in range(1, n):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j] else 0
        for i in range(n): 
            matrix[i].sort(reverse=1)
            for j in range(m):
                ans = max(ans, (j+1)*matrix[i][j])
        return ans