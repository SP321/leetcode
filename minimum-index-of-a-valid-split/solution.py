class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left_counter = Counter()
        right_counter = Counter(nums)
        dominant = max(right_counter, key=right_counter.get)
        
        for i in range(len(nums) - 1):
            left_counter[nums[i]] += 1
            right_counter[nums[i]] -= 1
            if left_counter[dominant]*2 > i+1 and right_counter[dominant]*2 > len(nums)-i-1:
                return i
        return -1