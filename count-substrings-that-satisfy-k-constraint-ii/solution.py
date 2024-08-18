class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n=len(s)
        ans=0
        i=0
        c=0
        c1=0
        end=[n-1 for _ in range(n)]
        start=[0 for _ in range(n)]
        sizes=[]
        for j in range(n):
            c+=1-int(s[j])
            c1+=int(s[j])
            while c>k and c1>k:
                c-=1-int(s[i])
                c1-=int(s[i])
                end[i]=j-1
                i+=1
            start[j]=i
            sizes.append(j-i+1)

        pref_sum = [0] + list(accumulate(sizes))
        ans = []
        for l, r in queries:
            r2=min(r,end[l])
            sz = r2 - l + 1
            curr = sz * (sz + 1) // 2
            curr += pref_sum[r + 1] - pref_sum[r2 + 1]
            ans.append(curr)
        return ans
