class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c=Counter()
        for i in nums:
            c[i]+=1
        ans=0
        for x in c:
            if c[x]==2:
                ans^=x
        return ans