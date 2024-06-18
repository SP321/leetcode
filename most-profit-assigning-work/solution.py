class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        a=sorted(zip(difficulty,profit))
        i=0
        cur=0
        n=len(a)
        ans=0
        for x in sorted(worker):
            while i<n and a[i][0]<=x:
                cur=max(cur,a[i][1])
                i+=1
            ans+=cur
        return ans