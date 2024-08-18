class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n=len(board)
        m=len(board[0])

        a=[]
        for i in range(n):
            for j in range(m):
                a.append((board[i][j],i,j))
        a.sort(reverse=True)

        def get_top(banned_i,banned_j,c):
            ans=[]
            for x,i,j in a:
                if i not in banned_i and j not in banned_j:
                    ans.append((x,i,j))
                if len(ans)==c:
                    return ans
            assert(True)
            
        ans=-inf
        for val1,i,j in get_top({},{},5):
            for val2,i2,j2 in get_top({i},{j},3):
                for val3,i3,j3 in get_top({i,i2},{j,j2},1):
                    ans=max(ans,val1+val2+val3)
        return ans