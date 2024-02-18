dirs_8=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        c=Counter()
        def prime(n):
            i=2
            while i*i<=n:
                if n%i==0:
                    return False
                i+=1
            return True
        
        def solve(x,y,dx,dy):
            pre=""
            for i in range(max(n,m)):
                xx=x+dx*i
                yy=y+dy*i
                if 0<=xx<n and 0<=yy<m:
                    pre+=str(mat[xx][yy])
                    if len(pre)>1:
                        if prime(int(pre)):
                            c[int(pre)]+=1
        
        for sx in range(n):
            for sy in range(m):
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    solve(sx,sy,dx,dy)

        if len(c)==0:
            return -1
        return max(c,key=lambda x:(c[x],x))
