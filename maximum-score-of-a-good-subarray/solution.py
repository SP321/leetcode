class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k, k
        curmin = nums[k]
        ans = nums[k]
        
        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
                curmin = min(curmin, nums[right])
            elif right == n - 1 or nums[left - 1] >= nums[right + 1]:
                left -= 1
                curmin = min(curmin, nums[left])
            else:
                right += 1
                curmin = min(curmin, nums[right])
            
            ans = max(ans, curmin * (right - left + 1))
        return ans