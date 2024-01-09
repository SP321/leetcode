# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class bs:
    def __init__(self,lo,hi):
        self.lo=lo
        self.hi=hi

    def __getitem__(self, x):
        return -guess(x)
            
    def __len__(self):
        return self.hi
    
    def left(self):
        pos= bisect.bisect_left(self,0,lo=self.lo,hi=self.hi)
        if pos==self.hi or self[pos]==-1:
            return None
        return pos

class Solution:
    def guessNumber(self, n: int) -> int:
        return bs(0,n+1).left()
        