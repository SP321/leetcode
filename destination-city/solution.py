class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a=set(i[0] for i in paths)
        b=set(i[1] for i in paths)
        return (b-a).pop()