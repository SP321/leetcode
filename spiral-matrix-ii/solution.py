class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]
        x=1
        top, bottom, left, right = 0, n - 1, 0, n - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                ans[top][j]=x
                x+=1
            top += 1
            for i in range(top, bottom + 1):
                ans[i][right]=x
                x+=1
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans[bottom][j]=x
                    x+=1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans[i][left]=x
                    x+=1
                left += 1
        return ans
                

