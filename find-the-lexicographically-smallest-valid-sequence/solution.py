class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i]=dp[i+1]
            if dp[i+1]<m and word1[i]==word2[m-dp[i+1]-1]:
                dp[i]+=1
        
        ans=[]
        free=True
        for i in range(n):
            if len(ans)==m:
                break
            if word1[i]==word2[len(ans)]:
                ans.append(i)
            elif free and len(ans)+1+dp[i+1]>=m:
                if len(ans)==0:
                    ans.append(i)
                else:
                    ans.append(ans[-1]+1)
                free=False
        if len(ans)!=m:
            return []
        return ans