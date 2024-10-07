class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost=cost[::-1]
        @cache
        def get_length(k):
            if k<0:
                return -inf
            if k==0:
                return 0
            ans=-inf
            for x in cost:
                ans=max(ans,get_length(k-x)+1)
            return ans
        n=get_length(target)
        if n==-inf:
            return "0"
        ans=[""]*n
        get_length.cache_clear()
        @cache
        def dp(pos,k):
            if k<0:
                return False
            if pos==n:
                return k==0
            for i,x in enumerate(cost):
                ans[pos]=str(9-i)
                if dp(pos+1,k-x):
                    return True
            return False
        dp(0,target)
        dp.cache_clear()
        return ''.join(ans)                