class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @cache
        def dp(x,target):
            if len(x)==1:
                return 0 if x==target else 1
            if x[0]==target[0]:
                return dp(x[1:],target[1:])
            else:
                target1='1'+target[2:]
                target2=target[1:]
                return 1+dp(x[1:],target1)+dp(target1,target2)
        x=bin(n)[2:]
        return dp(x,'0'*len(x))