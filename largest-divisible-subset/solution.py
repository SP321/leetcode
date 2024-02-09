class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = [[x] for x in nums]
        
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(ans[i]) < len(ans[j]) + 1:
                    ans[i] = ans[j] + [nums[i]]
                    
        return max(ans, key=len)
  