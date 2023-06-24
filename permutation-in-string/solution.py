class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=[0]*26
        for i in s1:
            a[ord(i)-ord('a')]+=1
        b=[0]*26
        for i in range(len(s2)):
            b[ord(s2[i])-ord('a')]+=1
            if i>=len(s1):
                b[ord(s2[i-len(s1)])-ord('a')]-=1
            if a==b:
                return True
        return False
            

        