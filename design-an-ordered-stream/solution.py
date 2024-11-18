class OrderedStream:
    def __init__(self, n: int):
        self.a=[""]*(n+1)
        self.ptr=1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.a[idKey]=value
        ans=[]
        while self.ptr<len(self.a) and self.a[self.ptr]!="":
            ans.append(self.a[self.ptr])
            self.ptr+=1
        return ans


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)