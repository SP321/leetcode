class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        n=len(coins)
        ans=0
        coins.sort()
        max_possible_sum=0
        for i in coins:
            while max_possible_sum+1<i:
                max_possible_sum=max_possible_sum*2+1
                ans+=1
                if max_possible_sum>=target:
                    return ans
            max_possible_sum+=i
            if max_possible_sum>=target:
                return ans
        while max_possible_sum<target:
            max_possible_sum=max_possible_sum*2+1
            ans+=1
        return ans