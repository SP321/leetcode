class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        nums.append((1<<10)-1)
        prev_max=-1
        cur_max=-1
        cur_min=float('inf')
        for x in groupby(nums,lambda x:x.bit_count()):
            y=list(x[1])
            cur_max=max(y)
            cur_min=min(y)
            if cur_min<prev_max:
                return False
            prev_max=cur_max
        return True