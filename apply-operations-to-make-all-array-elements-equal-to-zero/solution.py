
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        decrement = [0] * (n + 1)
        limit = 0
        for i in range(n - k + 1):
            limit -= decrement[i]
            if nums[i] > limit:
                decrement[i + k] = nums[i] - limit
                limit = nums[i]
            elif nums[i] < limit:
                return False
                
        for i in range(n - k + 1, n):
            limit -= decrement[i]
            if nums[i] != limit:
                return False
        return True
