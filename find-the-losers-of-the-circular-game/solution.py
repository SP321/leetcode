class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        x=[i for i in range(1,n+1)]
        i=0
        step=1
        recieved=set()
        while True:
            if i+1 in recieved:
                return sorted(list(set(x)-recieved))
            recieved.add(i+1)
            pos=i+k*step
            pos%=n
            i=pos
            step+=1