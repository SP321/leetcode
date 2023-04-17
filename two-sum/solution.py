class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in c:
                return [c[req],i]
            c[nums[i]]=i
        return []