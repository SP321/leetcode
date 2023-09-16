class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        skip = (n+1)//2
        ans = n%2
        for i in range(n//2):
            if nums[i] == nums[skip+i]:
                ans += 2
        return ans