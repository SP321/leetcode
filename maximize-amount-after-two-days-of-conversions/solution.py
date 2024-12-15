class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        dp0=defaultdict(int)
        dp0[initialCurrency]=1.0
        for p,r in zip(pairs1*len(pairs1),rates1*len(rates1)):

            dp1=defaultdict(int)
            for k,v in dp0.items():
                if k==p[0]:
                    dp1[p[1]]=max(dp1[p[1]],v*r)
            for k,v in dp0.items():
                if k==p[1]:
                    dp1[p[0]]=max(dp1[p[0]],v/r)
                
            for k,v in dp1.items():
                dp0[k]=max(dp0[k],v)
        
        for p,r in zip(pairs2*len(pairs2),rates2*len(rates2)):

            dp1=defaultdict(int)
            for k,v in dp0.items():
                if k==p[0]:
                    dp1[p[1]]=max(dp1[p[1]],v*r)
            for k,v in dp0.items():
                if k==p[1]:
                    dp1[p[0]]=max(dp1[p[0]],v/r)
            for k,v in dp1.items():
                dp0[k]=max(dp0[k],v)

        return dp0[initialCurrency]