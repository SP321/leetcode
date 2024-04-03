class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c=Counter(word1)
        c2=Counter(word2)
        for x in ascii_lowercase:
            for y in ascii_lowercase:
                if c[x]>0 and c2[y]>0:
                    c[x]-=1
                    c[y]+=1
                    c2[y]-=1
                    c2[x]+=1
                    if sum(c[i]>0 for i in ascii_lowercase) == sum(c2[i]>0 for i in ascii_lowercase):
                        return True
                    c[x]+=1
                    c[y]-=1
                    c2[y]+=1
                    c2[x]-=1
        return False