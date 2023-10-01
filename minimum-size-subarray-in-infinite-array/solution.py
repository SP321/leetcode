class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
        def subarray_length(a, target, find_max=True):
            i, su, ans = 0, 0, float('inf') if not find_max else 0
            for j in range(len(a)):
                su += a[j]
                while i < j and su > target:
                    su -= a[i]
                    i += 1
                if su == target:
                    if find_max:
                        ans = max(ans, j - i + 1)
                    else:
                        ans = min(ans, j - i + 1)
            return ans
        
        x = sum(nums)
        ans = float('inf')
        if target < x:
            ans = subarray_length(nums, target, find_max=False)
            pass

        times = target // x
        rem = target % x
        new_t = rem
        
        if new_t == 0:
            return len(nums) * times
        
        if times > 0:
            new_t += x
            times -= 1
        
        wholes = times * len(nums)
        
        ans2 = subarray_length(nums + nums, x * 2 - new_t, find_max=True)
        if ans2 != 0:
            ans=min(ans, wholes + len(nums) * 2 - ans2)
        
        return ans if ans!=float('inf') else -1