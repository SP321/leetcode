class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op = ['*','+','-']
        @cache
        def fun(s):
            count = sum([op[i] in s for i in range(3)])
            if count==0:
                return [int(s)]
            ans = []
            for i in range(len(s)):
                if s[i] in op:
                    left = fun(s[:i])
                    right = fun(s[i+1:])
                    for j in left:
                        for k in right:
                            ans.append(eval(str(j) + s[i] + str(k)))
            return ans
        return fun(expression)