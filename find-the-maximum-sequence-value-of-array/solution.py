class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def get_map(a): # d[SUBSEEUQNCE_OR]=min_end_index+1
            dp0=set([(0,0)])
            d=defaultdict(lambda :-1)
            for i,x in enumerate(a):
                dp1=set()
                for taken,val in dp0:
                    if taken+1==k:
                        if val|x not in d:
                            d[val|x]=i+1
                    else:
                        dp1.add( (taken+1,val|x) )
                dp0|=dp1
            return d
        a=get_map(nums)
        b=get_map(nums[::-1])
        ans=-inf
        for v1,x in a.items():
            for v2,y in b.items():
                if x+y<=n:
                    ans=max(ans,v1^v2)
        return ans