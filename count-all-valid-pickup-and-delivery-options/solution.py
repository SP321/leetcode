class Solution:
    def countOrders(self, n: int) -> int:
        md=10**9+7
        @cache
        def dp(pickup,delivery):
            if pickup==0 and delivery==0:
                return 1
            ans=0
            if pickup>0:
                ans+=dp(pickup-1,delivery)*pickup
            if pickup<delivery:
                ans+=dp(pickup,delivery-1)*(delivery-pickup)
            return ans%md
        return dp(n,n)
        