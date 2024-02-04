class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
    
        ans=[[0 for j in range(m)] for i in range(n)]
        c=[[0 for j in range(m)] for i in range(n)]

        for i in range(n-2):
            for j in range(m-2):
                mx=0
                s=0
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if x+1<i+3:
                            mx=max(mx,abs(image[x][y]-image[x+1][y]))
                        if y+1<j+3:
                            mx=max(mx,abs(image[x][y]-image[x][y+1]))
                        s+=image[x][y]
                region_average=s//9
                if mx<=threshold:
                    for x in range(i,i+3):
                        for y in range(j,j+3):
                            ans[x][y]+=region_average
                            c[x][y]+=1

        for i in range(n):
            for j in range(m):
                if c[i][j]==0:
                    ans[i][j]=image[i][j]
                else:
                    ans[i][j]//=c[i][j]
        return ans