class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        x=[0]*(n+1)
        for a,b in trust:
            x[a]-=1
            x[b]+=1
        for i in range(1,n+1):
            if x[i]==n-1:
                return i
        return -1