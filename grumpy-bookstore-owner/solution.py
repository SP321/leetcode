class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total=0
        n=len(customers)
        i=0
        cur=0
        ans=0
        for j in range(n):
            if grumpy[j]:
                cur+=customers[j]
            else:
                total+=customers[j]
            while j-i+1>minutes:
                if grumpy[i]:
                    cur-=customers[i]
                i+=1
            ans=max(ans,cur)
        return ans+total
