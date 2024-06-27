class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s=set()
        for x,y in edges:
            if x in s:
                return x
            if y in s:
                return y
            s.add(x)
            s.add(y)