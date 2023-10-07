class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        md=10**9+7
        @cache
        def dp(i,cur_max,k):
            if i==n and k==0:
                return 1
            if i>=n or k<0:
                return 0
            ans=0
            for j in range(1,m+1):
                new_k=k
                if j>cur_max:
                    new_k-=1
                ans+=dp(i+1,max(cur_max,j),new_k)
                ans%=md
            return ans
        return dp(0,-1,k)