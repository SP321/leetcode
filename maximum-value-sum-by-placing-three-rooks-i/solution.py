class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n=len(board)
        m=len(board[0])
        dp=defaultdict()

        for i in range(n):
            largest3=nlargest(3,range(m),key=lambda j:board[i][j])
            board[i]=[(j,board[i][j])  for j in largest3]
        @cache
        def dp(i,ban):
            if i==n:
                return -inf
            ans=dp(i+1,ban)
            for idx,val in board[i]:
                if (1<<idx)&ban==0:
                    if ban.bit_count()==2:
                        ans=max(ans,val)
                    else:
                        ans=max(ans,dp(i+1,ban|(1<<idx))+val)
            return ans
        return dp(0,0)