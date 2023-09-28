class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def helper(nums):
                    tails = []
                    res = []
                    for num in nums:
                        idx = bisect.bisect_left(tails, num)
                        if idx == len(tails):
                            tails.append(num)
                        else:
                            tails[idx] = num
                        res.append(len(tails))
                    return res

        left = helper(nums)
        right = helper(nums[::-1])[::-1]
        
        ans = float('inf')
        
        for l, r in zip(left, right):
            if l > 1 and r > 1:
                ans = min(ans, len(nums) - l - r + 1)
        
        return ans