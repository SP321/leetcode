class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        a=[]
        l=[]
        for i,x in enumerate(arr):
            while a and x<a[-1][1]:
                a.pop()
            if not a:
                l.append(i+1)
            else:
                l.append(i-a[-1][0])
            a.append((i,x))
        a=[]
        r=[]
        for i,x in list(enumerate(arr))[::-1]:
            while a and x<=a[-1][1]:
                a.pop()
            if not a:
                r.append(n-i)
            else:
                r.append(a[-1][0]-i)
            a.append((i,x))
        r=r[::-1]
        return sum(x*y*z for x,y,z in zip(arr,l,r))%(10**9+7)
