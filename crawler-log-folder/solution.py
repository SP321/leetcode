class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for x in logs:
            if x == "../":
                c=max(0,c-1)
            elif x=='./':
                pass
            else:
                c+=1
        return c