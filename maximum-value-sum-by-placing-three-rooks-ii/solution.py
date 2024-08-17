class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n=len(board)
        m=len(board[0])
        
        idxs=set()
        for i in range(n):
            for j in nlargest(3, range(m), key=lambda j: board[i][j]):
                idxs.add((i,j))

        h=[]
        for j in set(x[1] for x in idxs):
            for i in nlargest(3, range(n), key=lambda i: board[i][j]):
                if (i,j) in idxs:
                    heappush(h, (board[i][j],i,j) )
                    if len(h)>9:
                        heappop(h)
                
        ans=-inf
        for ch in combinations(h,3):
            if len(set(x[1] for x in ch))==3 and len(set(x[2] for x in ch))==3:
                ans=max(ans,sum(x[0] for x in ch))
        return ans