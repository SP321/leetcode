class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x=[]
        for i in operations:
            if i=='C':
                x.pop()
            elif i=='D':
                x.append(x[-1]*2)
            elif i=="+":
                x.append(x[-1]+x[-2])
            else:
                x.append(int(i))
        return sum(x)