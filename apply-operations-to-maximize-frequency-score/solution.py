class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k -= nums[j] - nums[(i + j) // 2]
            if k < 0:
                k += nums[(i + j) // 2] - nums[i]
                k += nums[(i + j + 1) // 2] - nums[(i + j) // 2]
                i += 1
        return j - i + 1