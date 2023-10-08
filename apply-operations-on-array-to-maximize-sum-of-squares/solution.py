class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        md=10**9+7
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit_counts[i] += 1

        ans = 0
        
        for _ in range(k):
            current_num = 0
            for i in range(31, -1, -1):
                if bit_counts[i]:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            ans += current_num*current_num
            ans%=md

        return ans