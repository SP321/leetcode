from sortedcontainers import SortedList

class SL2():
    def __init__(self,x):
        self.a=SortedList()
        self.b=SortedList()
        self.sm=0
        self.x=x


    def add(self,val):
        self.b.add( val )
        self.sm+=prod(val)
        if len(self.b)>self.x:
            m=self.b.pop(0)
            self.sm-=prod(m)
            self.a.add(m)

    def discard(self,val):
        if val>=self.b[0]:
            self.sm-=prod(val)
            self.b.discard(val)
            if len(self.b)<self.x and self.a:
                m=self.a.pop(-1)
                self.sm+=prod(m)
                self.b.add(m)
        else:
            self.a.discard(val)


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i=0
        c=Counter()
        n=len(nums)
        sl=SL2(x)
        ans=[]
        for j in range(n):
            cur=nums[j]
            if c[cur]>0:
                sl.discard( (c[cur],cur) )
            c[cur]+=1
            sl.add( (c[cur],cur) )

            if j-i+1>k:
                cur=nums[i]
                sl.discard( (c[cur],cur) )
                c[cur]-=1
                if c[cur]>0:
                    sl.add( (c[cur],cur) )
                i+=1
            if j-i+1==k:
                ans.append(sl.sm)
        return ans