class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        @cache
        def dfs(i,mask):
            if i==n:
                return 0
            ans=dfs(i+1,mask)
            x=arr[i]
            new_mask=mask
            for ch in x:
                if new_mask & 1<<(ord(ch)-ord('a'))!=0:
                    return ans
                new_mask|=1<<(ord(ch)-ord('a'))
            ans=max(ans,dfs(i+1,new_mask)+len(x))
            return ans
        return dfs(0,0)