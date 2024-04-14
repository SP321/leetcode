class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        lcms=Counter()
        for mask in range(1,1<<len(coins)):
            cur=reduce(lcm,(coins[i] for i in range(len(coins)) if (1<<i)&mask))
            lcms[cur]+=1 if mask.bit_count()%2 else -1
        def check(n):
            return sum((n//x)*c for x,c in lcms.items())
        return bisect_left(range(min(coins)*k+1),k,key=check)