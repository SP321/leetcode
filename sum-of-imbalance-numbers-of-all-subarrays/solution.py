class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            counts = defaultdict(int)
            counts[nums[i]] = 1
            c = 0
            for j in range(i + 1, n):
                counts[nums[j]]+=1
                if counts[nums[j]] == 1:
                    c += 1
                    if nums[j] > 0 and counts[nums[j] - 1] >0: c -= 1
                    if nums[j] < n and counts[nums[j] + 1] >0: c -= 1
                counts[nums[j]]+=1
                ans += c
        return ans