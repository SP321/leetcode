class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        c=Counter()
        nums = [1] + nums + [1]

        for windowsize in range(2, len(nums)):
            for left in range(len(nums) - windowsize):
                right = left + windowsize
                for mid in range(left + 1, right):
                    coins = nums[left] * nums[mid] * nums[right]
                    coins += c[(left, mid)] + c[(mid, right)]
                    c[(left, right)] = max(coins, c[(left, right)])
        return c[(0, len(nums) - 1)]
