class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @cache
        def dfs(i,prev):
            if i==n:
                return 1
            letters="aeiou"
            if prev=='a':
                letters="e"
            if prev=='e':
                letters="ai"
            if prev=='i':
                letters="aeou"
            if prev=='o':
                letters="iu"
            if prev=='u':
                letters="a"
            ans=0
            for j in letters:
                ans+=dfs(i+1,j)
            return ans%(10**9+7)
        return dfs(0,"_")
