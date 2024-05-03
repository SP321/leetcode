class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        s = set(nums)
        for n in nums:
            if n > 0:
                if n > ans and -n in s:
                    ans = n
        return ans