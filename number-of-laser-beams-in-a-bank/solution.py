class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_count=0
        ans=0
        for i in bank:
            x=i.count("1")
            if x>0:
                ans+=prev_count*x
                prev_count=x
        return ans