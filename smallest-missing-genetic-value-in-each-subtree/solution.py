class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n
        seen = [0] * 100010
        if 1 not in nums:
            return ans
        children = [[] for i in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        def dfs(i):
            if seen[nums[i]] == 0:
                for j in children[i]:
                    dfs(j)
                seen[nums[i]] = 1

        i = nums.index(1)
        miss = 1
        while i >= 0:
            dfs(i)
            while seen[miss]:
                miss += 1
            ans[i] = miss
            i = parents[i]
        return ans