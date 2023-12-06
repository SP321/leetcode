class Solution:
    def totalMoney(self, n: int) -> int:
        a=[0]*n
        for i in range(0,n,7):
            a[i]=i//7+1
            for j in range(i+1,min(n,i+7)):
                a[j]=a[j-1]+1            
        return sum(a[:n])
        