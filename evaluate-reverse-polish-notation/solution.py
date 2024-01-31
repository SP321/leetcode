class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for x in tokens:
            if x not in "+-*/":
                s.append(int(x))
            else:
                b=s.pop()
                a=s.pop()
                if x=='+':
                    s.append(a+b)
                elif x=='-':
                    s.append(a-b)
                elif x=='*':
                    s.append(a*b)
                elif x=='/':
                    s.append(int(a/b))
        return s.pop()