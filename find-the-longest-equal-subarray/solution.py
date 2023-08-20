class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for idx, num in enumerate(nums):
            d[num].append(idx)
        ans = 1
        for val, positions in d.items():
            left, right = 0, 0
            while right < len(positions):
                to_delete = positions[right] - positions[left] - (right - left)
                if to_delete <= k:
                    ans = max(ans, right - left + 1)
                    right += 1
                else:
                    left += 1
        return ans