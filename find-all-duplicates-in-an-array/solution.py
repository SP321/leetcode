class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            n = abs(num)
            if nums[n - 1] < 0:
                ans.append(n)
            nums[n - 1] = -nums[n - 1]
        return ans