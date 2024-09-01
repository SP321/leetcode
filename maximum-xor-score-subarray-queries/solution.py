class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i,j in queries:
            d[j - i].append([i, j])
        cur = nums[:]
        ans = {}
        n = len(nums)
        for v in range(len(nums)):
            for i,j in d[v]:
                ans[i,j] = cur[i]
            for i in range(n - v - 1):
                nums[i] ^= nums[i + 1]
                cur[i] = max(cur[i], cur[i + 1], nums[i])
        return [ans[i,j] for i,j in queries]