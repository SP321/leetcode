class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=Counter(chars)
        ans=0
        for word in words:
            c2=Counter(word)
            flag=True
            for i in c2:
                if c2[i]>c[i]:
                    flag=False
            if flag:
                ans+=len(word)
        return ans