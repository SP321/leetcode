class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a=sentence1.split()
        b=sentence2.split()
        if len(a)>len(b):
            a,b=b,a
        n=len(b)
        i=0
        j=n-1
        for x in a:
            if b[i]==x:
                i+=1
            else:
                break
        a=a[i:]
        for x in a[::-1]:
            if b[j]==x:
                j-=1
            else:
                return False
        return not( i==0 and j==n-1)