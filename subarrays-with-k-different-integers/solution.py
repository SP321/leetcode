class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            c = Counter()
            ans = i = 0
            for j in range(len(nums)):
                c[nums[j]] += 1
                while len(c)>k:
                    c[nums[i]] -= 1
                    if c[nums[i]] == 0:
                        del c[nums[i]]
                    i += 1
                ans += j - i + 1
            return ans
        return helper(nums, k) - helper(nums, k - 1)

