class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n=len(grid)
        mid=n//2
        def is_y(x,y):
            if x==y and x<=mid and y<=mid:
                return True
            if x==n-1-y and x<=mid and n-1-y<=mid:
                return True
            if x>=mid and y==mid:
                return True
            return False
        not_y=[0,0,0]
        y=[0,0,0]
        for i in range(n):
            for j in range(n):
                x=grid[i][j]
                if is_y(i,j):
                    y[x]+=1
                else:
                    not_y[x]+=1
        ans=float("inf")
        for comb in itertools.combinations([0,1,2],2):
            ans=min(ans,sum(y)-y[comb[0]]+sum(not_y)-not_y[comb[1]])
            ans=min(ans,sum(y)-y[comb[1]]+sum(not_y)-not_y[comb[0]])
        return ans