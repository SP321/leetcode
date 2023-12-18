class Solution:
    def countEven(self, num: int) -> int:
        return sum(1 for i in range(1,num+1) if sum(map(int,str(i)))%2==0)