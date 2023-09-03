class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans=0
        for i in range(low,high+1):
            x=str(i)
            a=[int(j) for j in x[:len(x)//2]]
            b=[int(j) for j in x[len(x)//2:]]
            if len(x)%2==0:
                if sum(a)==sum(b):
                    ans+=1
        return ans
                
        