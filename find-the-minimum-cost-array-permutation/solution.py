class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        memo={}
        @cache
        def dp(mask,prev):
            if mask==(1<<n)-1:
                return abs(nums[0]-prev)
            best_score,best_choice=inf,None
            for i in range(n):
                if mask&(1<<i):
                    continue
                next_score=dp(mask|(1<<i),i)
                cur_score=next_score+abs(prev-nums[i])
                if cur_score<best_score:
                    best_score,best_choice=cur_score,i
            memo[mask,prev]=best_choice
            return best_score
        dp(1,0)
        ans=[0]
        mask=1
        while len(ans)!=n:
            ans.append(memo[mask,ans[-1]])
            mask|=(1<<ans[-1])
        return ans