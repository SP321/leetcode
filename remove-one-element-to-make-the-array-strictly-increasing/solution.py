class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        prev, seen = -inf, False
        for i, x in enumerate(nums): 
            if prev < x: prev = x
            else: 
                if seen: return False 
                seen = True 
                if i == 1 or nums[i-2] < x: prev = x
        return True 