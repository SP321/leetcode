
class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        if isinstance(x,int):
            self.bit=[0]*x
        else:
            self.bit = x
            for i in range(len(x)):
                j = i | (i + 1)
                if j < len(x):
                    x[j] += x[i]

    def update(self, idx, x):
        """update bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1
        
    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def __setitem__(self,idx,x):
        self.update(idx,x-self[idx])

    def __getitem__(self,idx):
        if isinstance(idx, slice):
            st=idx.start if idx.start else 0
            end=idx.stop if idx.stop else len(self.bit)
        else:
            st=idx
            end=idx+1
        return self.query(end)-self.query(st)

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n=len(nums)
        tr=FenwickTree(n)
        def update_tree(i):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                tr[i]=1
            else:
                tr[i]=0
        for i in range(1,n-1):
            update_tree(i)
        ans=[]
        for t,a,b in queries:
            if t==1:
                ans.append(tr[a+1:b] if a+1<b else 0)
            elif t==2:
                nums[a]=b
                for i in range(max(1,a-1),min(n-1,a+2)):
                    update_tree(i)
        return ans