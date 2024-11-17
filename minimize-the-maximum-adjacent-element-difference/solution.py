class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        t1=[]
        t2=[]
        t3=[]
        mx_diff = 0
        a=[]
        for i,x in enumerate(nums):
            if x!=-1:
                a.append(i)
        for x,y in pairwise(a):
            if y-x==1:
                mx_diff=max(mx_diff,abs(nums[x]-nums[y]))
            elif y-x==2:
                t2.append(sorted([nums[x],nums[y]]))
            elif y-x>2:
                t3.append(sorted([nums[x],nums[y]]))
        if len(a)==0:
            return 0
        if len(a)==1 or len(a)==n:
            return mx_diff
        if a[0]!=0:
            t1.append(nums[a[0]])
        if a[-1]!=n-1:
            t1.append(nums[a[-1]])
        r1=set(x for x in chain(t1,*t3))
        r2=set((x,y) for x,y in chain(t2,t3))
        def check(limit):
            ranges = []
            for x in r1:
                ranges.append([x-limit, x+limit])
            for x,y in t2:
                l,r=y-limit, x+limit
                if r<l:
                    return False
                ranges.append([l,r])

            ch1 = min(r for _,r in ranges)
            ch2 = max(l for l,_ in ranges)
            
            if ch1 + limit < ch2:
                for x,y in r2:
                    for choice in [ch1,ch2]:
                        if (abs(x-choice)<=limit and abs(y-choice)<=limit):
                            break
                    else:
                        return False
            return True
        return bisect_left(range(10**9+1), True, key=check, lo=mx_diff)