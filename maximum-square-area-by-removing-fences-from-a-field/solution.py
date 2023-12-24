class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences=[1]+sorted(hFences)+[m]
        vFences=[1]+sorted(vFences)+[n]
        h_gaps=set()
        v_gaps=set()
        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                h_gaps.add(hFences[j]-hFences[i])
        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                v_gaps.add(vFences[j]-vFences[i])
        ans=h_gaps&v_gaps
        return -1 if len(ans)==0 else (max(list(ans))**2)%(10**9+7)