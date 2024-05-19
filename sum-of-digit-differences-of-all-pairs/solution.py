class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        cc=[Counter() for _ in range(9)]
        for x in nums:
            pos=0
            while x>0:
                cc[pos][x%10]+=1
                x//=10
                pos+=1
        n=len(nums)
        ans=0
        for c in cc:
            for x in c.values():
                ans+=x*(n-x)
        return ans//2