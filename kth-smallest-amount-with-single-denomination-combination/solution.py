class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        c=Counter()
        for mask in range(1,1<<len(coins)):
            cur=reduce(lcm,[coins[i] for i in range(len(coins)) if (1<<i)& mask])
            if mask.bit_count()%2:
                c[cur]+=1
            else:
                c[cur]-=1
        def get_pos(n):
            return sum((n//x)*y for x,y in c.items())
        return bisect_left(range(1,min(coins)*k+1),k,key=get_pos)+1

