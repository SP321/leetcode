class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mn=inf
        mn2=inf
        for x in nums:
            if x>mn2:
                return True
            if x>mn:
                mn2=min(x,mn2)
            mn=min(mn,x)
        return False