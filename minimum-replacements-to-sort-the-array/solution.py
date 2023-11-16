class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        limit=nums.pop()
        ans=0
        while nums:
            x=nums.pop()
            if x>limit:
                parts_required=(x+(limit-1))//limit #min no of parts.
                ans+=parts_required-1 #-1 because we divide from 1 part.
                limit=x//parts_required # max possible smallest part.
            else:
                limit=min(x,limit)
        return ans
