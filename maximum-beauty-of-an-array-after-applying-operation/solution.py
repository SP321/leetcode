class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 1, len(nums)
        
        def check(mid):
            for i in range(mid-1, len(nums)):
                min_val = nums[i-mid+1]
                max_val = nums[i]
                if min_val + k >= max_val - k:
                    return True
            return False
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left