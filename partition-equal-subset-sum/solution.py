class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 == 1:
            return False

        bitset = 1
        target = total_sum // 2

        for num in nums:
            bitset |= (bitset << num)
        
        return (bitset & (1 << target)) != 0
