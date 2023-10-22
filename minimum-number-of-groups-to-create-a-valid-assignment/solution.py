class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        f =Counter(nums)
        ff=Counter(f.values())
        
        for groupsize in range(min(ff.keys()),-1,-1):
            ans = 0
            for freq,times in ff.items():
                x, r = divmod(freq, groupsize+1)
                groups = x+(r > 0)
                if groups*groupsize <= freq:                    
                    ans += groups*times
                else:
                    break
            else:
                return ans