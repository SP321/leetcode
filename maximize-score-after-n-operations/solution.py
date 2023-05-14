class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcds = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                gcds[i][j] = gcds[j][i] = math.gcd(nums[i], nums[j])

        def solve_recursive(remaining,cur_gcds):
            if not remaining:
                cur_gcds.sort()
                return sum( (i + 1) * cur_gcds[i] for i in range(len(cur_gcds)) )
            else:
                ans=0
                first = remaining.pop()
                for second in set(remaining):
                    remaining.remove(second)
                    ans=max(ans,solve_recursive(remaining,cur_gcds+[gcds[first][second]]))
                    remaining.add(second)
                remaining.add(first)
                return ans
        return solve_recursive(set(range(n)),[])