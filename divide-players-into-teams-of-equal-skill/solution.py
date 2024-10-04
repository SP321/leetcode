class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans=0
        target=2*sum(skill)//len(skill)
        c=Counter(skill)
        for x,v in c.items():
            y=target-x
            if v!=c[y]:
                return -1
            ans+=x*y*v
        return ans//2
