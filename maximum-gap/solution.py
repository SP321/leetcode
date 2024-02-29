class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        max_value, min_value = max(nums), min(nums)
        
        bucket_size = max(1, (max_value - min_value) // (n - 1))
        
        num_buckets = (max_value - min_value) // bucket_size + 1
        
        buckets = [[float('inf'), float('-inf')] for _ in range(num_buckets)]
        for num in nums:
            bucket_index = (num - min_value) // bucket_size
            buckets[bucket_index][0] = min(buckets[bucket_index][0], num)
            buckets[bucket_index][1] = max(buckets[bucket_index][1], num)
        
        max_diff = 0
        prev_max = buckets[0][1]
        for i in range(1, num_buckets):
            if buckets[i][0] == float('inf'):
                continue
            max_diff = max(max_diff, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]
        
        return max_diff