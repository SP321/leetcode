class Solution:
    def maxDiff(self, num: int) -> int:
        x=y=s= str(num)
        n = len(s)
        flag1 = False
        flag2 = False

        a = '1' if s[0] > '1' else '0'

        for i in range(n):
            if not flag1 and s[i] > '1':
                x = s.replace(s[i], a)
                flag1 = True
            if not flag2 and s[i] != '9':
                y = s.replace(s[i], '9')
                flag2 = True
            if flag1 and flag2:
                break

        return int(y) - int(x)