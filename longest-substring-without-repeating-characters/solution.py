class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        ans=1
        prev=defaultdict(int)
        m=0
        for i in range(len(s)):
            if prev[s[i]]:
                m=max(m,prev[s[i]])
            prev[s[i]]=i+1
            ans=max(ans,i-m+1)
        return ans