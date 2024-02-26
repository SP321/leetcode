class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        c=Counter()
        for j,x in enumerate(nums):
            c[x]+=1
            while j-i>k:
                c[nums[i]]-=1
                i+=1
            if c[x]==2:
                return True
        return False