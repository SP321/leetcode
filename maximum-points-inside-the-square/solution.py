class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        d=defaultdict(list)
        for i,(x,y) in enumerate(points):
            d[max(abs(x),abs(y))].append(i)
        ans=0
        st=set()
        for key in sorted(d.keys()):
            for i in d[key]:
                if s[i] in st:
                    return ans
                st.add(s[i])
            ans=len(st)
        return ans