class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr=[]
        for i,(start,end) in enumerate(times):
            arr.append((start,True,i))
            arr.append((end,False,i))
        arr.sort()
        h=[]
        k=0
        seat={}
        for t,enter,i in arr:
            if enter:
                if h:
                    cur=heappop(h)
                else:
                    cur=k
                    k+=1
                if i==targetFriend:
                    return cur
                seat[i]=cur
            else:
                heappush(h,seat[i])
