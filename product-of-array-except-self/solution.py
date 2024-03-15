class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=list(accumulate(nums,lambda x,y:x*y,initial=1))
        suf=list(accumulate(nums[::-1],lambda x,y:x*y,initial=1))[::-1]
        return [a*b for a,b in zip(pre,suf[1:])]