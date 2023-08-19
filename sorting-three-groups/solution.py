class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [[0, 0, 0, 0] for _ in range(n + 1)]
        for i, num in enumerate(nums):
            for j in range(1, 4):
                prefix[i + 1][j] = prefix[i][j]
            prefix[i + 1][num] += 1
        
        def operations_needed(count_1, count_2, count_3):
            ops_1 = count_1 - (prefix[count_1][1])
            ops_2 = count_2 - (prefix[count_1 + count_2][2] - prefix[count_1][2])
            ops_3 = count_3 - (prefix[count_1 + count_2 + count_3][3] - prefix[count_1 + count_2][3])
            return ops_1 + ops_2 + ops_3
        
        min_ops = float('inf')
        for count_1 in range(n + 1):
            for count_2 in range(n - count_1 + 1):
                count_3 = n - count_1 - count_2
                ops = operations_needed(count_1, count_2, count_3)
                min_ops = min(min_ops, ops)
        
        return min_ops