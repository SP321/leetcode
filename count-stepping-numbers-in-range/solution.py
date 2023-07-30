md=10**9+7
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        low=str(int(low)-1)
        maximums=[high,low]
        @cache
        def dp(i,max_flag,prev):
            if i==0:
                return 1
            ans=0
            limit=9
            if max_flag<2:
                limit=int(maximums[max_flag][-i])
            ans=0
            for j in range(limit+1):
                if prev==-1 or prev==j+1 or prev==j-1:
                    nx=j
                    if prev==-1 and j==0:
                        nx=-1
                    if j==limit:
                        ans+=dp(i-1,max_flag,nx)
                    else:
                        ans+=dp(i-1,2,nx)
            return ans%md
        return (dp(len(high),0,-1)-dp(len(low),1,-1)+md)%md