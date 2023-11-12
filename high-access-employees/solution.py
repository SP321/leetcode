class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d=defaultdict(list)
        def conv(ts):
            hh=ts[:2]
            mm=ts[2:]
            return int(hh)*60+int(mm)
        for name,ts in access_times:
            d[name].append(conv(ts))
        ans=[]
        for name in d:
            x=sorted(d[name])
            for i in range(len(x)-2):
                if x[i+2]-x[i]<60:
                    ans.append(name)
                    break
        return ans