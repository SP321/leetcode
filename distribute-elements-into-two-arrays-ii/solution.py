class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
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

    def __len__(self):
        return len(self.bit)

    def __setitem__(self,idx,x):
        self.update(idx,x-self[idx])

    def __getitem__(self,idx):
        if isinstance(idx, slice):
            st=idx.start if idx.start else 0
            end=idx.stop if idx.stop else len(self)
        else:
            st=idx
            end=idx+1
        return self.query(end)-self.query(st)

class QueryList:
    def __init__(self,normalize_map) -> None:
        self.x=[]
        self.m=normalize_map
        self.tr=FenwickTree([0]*len(normalize_map))

    def push(self,val):
        self.x.append(val)
        self.tr.update(self.m[val],1)

    def get_g_c(self,val):
        return self.tr[self.m[val]+1:]

    def __len__(self):
        return len(self.x)

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        ll = sorted(set(nums))
        m = {ll[i]:i for i in range(len(ll))}
        a,b=QueryList(m),QueryList(m)
        a.push(nums[0])
        b.push(nums[1])
        for x in nums[2:]:
            aa,bb= a.get_g_c(x),b.get_g_c(x)
            if aa>bb:
                a.push(x)
            elif aa<bb:
                b.push(x)
            else:
                if len(a)<=len(b):
                    a.push(x)
                else:
                    b.push(x)
        return a.x+b.x