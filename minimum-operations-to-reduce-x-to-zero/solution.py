class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        n = len(nums)
        max_len_subarray = -1
        current_sum = 0
        left = 0
        for right in range(n):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:
                max_len_subarray = max(max_len_subarray, right - left + 1)
                
        if max_len_subarray == -1:
            return -1
        else:
            return n - max_len_subarray