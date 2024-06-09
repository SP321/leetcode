class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # dedup and sort rewards
        rewards = sorted(set(rewardValues))
        if len(rewards) == 1:
            return rewards[0]

        mask = [False]*(rewards[-1]+1)
        for x in rewards:
            mask[x] = True
        
        def dfs(idx, cursum, target):
            # constraint: total rewards(from 0 to idx) < rewards[idx+1]
            if target-cursum >= rewards[idx+1]:
                return False
            if mask[target-cursum]:
                return True
            for i in range(idx, -1, -1):
                if cursum+rewards[i] <= target:
                    # memorization
                    mask[cursum+rewards[i]] = True
                    if dfs(i-1, cursum+rewards[i], target):
                        return True
            return False
        
        # maximum total rewards must include the max reward
        n = len(rewards)
        for x in range(rewards[-1]-1, rewards[-2]-1, -1):
            if mask[x] or dfs(n-2, 0, x):
                return rewards[-1] + x
        return rewards[-1]
      