class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0
        nums.sort()
        n = len(nums)
        diffs = [nums[i] - nums[i-1] for i in range(1, n)]
        sorted_diffs = sorted(diffs)
        def can_form_pairs(mid_diff):
            used = set()
            count = 0
            i=0
            while i<n-1:
                if diffs[i] <= mid_diff:
                    i+=1
                    count+=1
                    if count==p:
                        return True
                i+=1
            return False
        
        low, high = 0, n - 2
        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(sorted_diffs[mid]):
                high = mid - 1
            else:
                low = mid + 1
        return sorted_diffs[low]


