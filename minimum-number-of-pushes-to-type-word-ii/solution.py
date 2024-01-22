class Solution:
    def minimumPushes(self, word: str) -> int:
        ans=0
        c=0
        for ch,x in Counter(word).most_common():
            ans+=x*((c//8)+1)
            c+=1
        return ans
            