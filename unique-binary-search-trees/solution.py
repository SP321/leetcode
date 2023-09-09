class Solution:
    def numTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def catalan(n: int) -> int:
            if n <= 1:
                return 1
            ans = 0
            for i in range(n):
                ans += catalan(i) * catalan(n-i-1)
            return ans
        return catalan(n)