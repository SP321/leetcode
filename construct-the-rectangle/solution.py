class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i=2
        factor=1
        while i*i<=area:
            if area%i==0:
                factor=i
            i+=1
        return [area//factor,factor]