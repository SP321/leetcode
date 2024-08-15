class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c=Counter()
        for x in bills:
            c[x]+=1
            if x==20:
                if c[10]>0 and c[5]>0:
                    c[10]-=1
                    c[5]-=1
                elif c[5]>2:
                    c[5]-=3
                else:
                    return False
            elif x==10:
                if c[5]>0:
                    c[5]-=1
                else:
                    return False
        return True