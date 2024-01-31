class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t=temperatures
        n=len(temperatures)
        x=[]
        ans=[0]*n
        for i in range(0,n):
            while len(x)>0 and t[i] > t[x[-1]] :
                b=x.pop()
                ans[b]=i-b
            x.append(i)
        return ans
