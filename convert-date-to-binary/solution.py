class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a=list(map(int,date.split("-")))
        b=[bin(x)[2:] for x in a]
        return '-'.join(b)