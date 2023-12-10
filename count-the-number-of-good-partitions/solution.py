class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        first_occurrence = {}
        last_occurrence = {}
        MOD=10**9+7
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i

        intervals = [(first_occurrence[num], last_occurrence[num]) for num in first_occurrence]
        intervals.sort()
        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        n=len(merged)
        return pow(2, n-1, MOD )