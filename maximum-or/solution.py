class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        or_ = 0
        or_multiple = 0
        for i in nums:
            or_multiple |= i & or_
            or_ |= i
        ans=0
        for i in nums:
            x = or_ & ~(i)
            x |= or_multiple
            x |= (i << k)            
            ans = max(ans, x)
        return ans