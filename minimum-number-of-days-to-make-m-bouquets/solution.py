class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        class bs:
            def __init__(self,lo,hi):
                self.lo=lo
                self.hi=hi

            def __getitem__(self, x):# return -1  for left invalid, +1 for right invalid 0 for valid.
                y=[i<=x for i in bloomDay]
                adj=0
                ans=0
                for i in y:
                    if i:
                        adj+=1
                    else:
                        ans+=adj//k
                        adj=0
                ans+=adj//k
                if ans>=m:
                    return 0
                return -1
                    
                    
            def __len__(self):
                return self.hi

            def right(self):
                pos= bisect.bisect_right(self,0,lo=self.lo,hi=self.hi)
                if pos==self.hi:
                    return None
                return pos-1
            
            def left(self):
                pos= bisect.bisect_left(self,0,lo=self.lo,hi=self.hi)
                if pos==self.hi:
                    return None
                return pos
            
        ans= bs(0,10**9+1).left()
        return ans if ans!=None else -1