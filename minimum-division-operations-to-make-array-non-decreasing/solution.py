seive=[None]*(10**6+1)
for i in range(2,len(seive)):
    for j in range(i+i,len(seive),i):
        seive[j]=i
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        limit=nums.pop()
        ans=0
        while nums:
            cur=nums.pop()
            while cur>limit:
                if seive[cur]==None:
                    return -1
                cur//=seive[cur]
                ans+=1
            limit=cur
        return ans