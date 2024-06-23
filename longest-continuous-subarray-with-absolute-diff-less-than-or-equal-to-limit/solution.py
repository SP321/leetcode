
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mi = deque()
        i = 0
        ans = 0
        
        for j, x in enumerate(nums):
            while mx and nums[mx[-1]] < x:
                mx.pop()
            mx.append(j)
            
            while mi and nums[mi[-1]] > x:
                mi.pop()
            mi.append(j)
            
            while nums[mx[0]] - nums[mi[0]] > limit:
                if mx[0] == i:
                    mx.popleft()
                if mi[0] == i:
                    mi.popleft()
                i += 1
            
            ans = max(ans, j - i + 1)
        return ans