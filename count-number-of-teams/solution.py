class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        ans=0
        for i in range(1,n):
            l,r=0,0
            for j in range(i):
                if(rating[j]<rating[i]):
                    l+=1
            for j in range(i+1,n):
                if(rating[j]>rating[i]):
                    r+=1
            ans+=l*r+(i-l)*(n-i-1-r)
        return ans
