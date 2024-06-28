class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        c=Counter(chain(*roads))
        ans=0
        for node,c in c.most_common():
            ans+=n*c
            n-=1
        return ans