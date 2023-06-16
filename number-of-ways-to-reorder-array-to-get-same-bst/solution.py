class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7 
        def solve(x):
            if len(x) <= 2:
                return 1
            left = [v for v in x if v < x[0]]
            right = [v for v in x if v > x[0]]
            return comb(len(x)-1, len(right))*solve(left)*solve(right)
        return (solve(nums) - 1)%mod