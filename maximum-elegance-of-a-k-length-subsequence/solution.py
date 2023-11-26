class Solution:
    def findMaximumElegance(self, items, K):
        items.sort(reverse=True)
        
        other = []
        distinct_categories  = set()
        ans = cur = 0
        for p, c in items:
            cur += p
            if c not in distinct_categories :
                distinct_categories .add(c)
            else:
                other.append(p)

            while other and len(other) + len(distinct_categories ) > K:
                cur -= other.pop()
            if len(distinct_categories ) <= K:
                ans = max(ans, cur + len(distinct_categories ) ** 2)
        
        return ans