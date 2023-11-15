class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        x=[i-j for i,j in zip(gas,cost)]
        if sum(x)<0:
            return -1
        cur=0
        ans=0
        for i in range(len(x)):
            cur+=x[i]
            if cur<0:
                cur=0
                ans=i+1
        return ans
