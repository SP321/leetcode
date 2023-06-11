class SnapshotArray:

    def __init__(self, length: int):
        self.x=[[]for i in range(length)]
        self.snapid=0

    def set(self, index: int, val: int) -> None:
        self.x[index].append((val,self.snapid))

    def snap(self) -> int:
        self.snapid+=1
        return self.snapid-1

    def get(self, index: int, snap_id: int) -> int:
        ans=0
        a=self.x[index]
        l=0
        r=len(a)-1
        while l<=r:
            m=(l+r)//2
            x,y=a[m]
            if y>snap_id:
                r=m-1
            elif y<=snap_id:
                l=m+1
                ans=x
        return ans


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)