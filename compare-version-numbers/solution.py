class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a=list(map(int,version1.split('.')))
        b=list(map(int,version2.split('.')))
        while len(a)<len(b):
            a.append(0)
        while len(b)<len(a):
            b.append(0)
        if a<b:
            return -1
        elif a>b:
            return 1
        else:
            return 0