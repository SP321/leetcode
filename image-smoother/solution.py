class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m  = len(img), len(img[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                s=0
                c=0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if x>=0 and x<n and y>=0 and y<m:
                            s+=img[x][y]
                            c+=1
                ans[i][j]=s//c 
        return ans