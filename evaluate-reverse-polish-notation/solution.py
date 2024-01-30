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
                    val=a/b
                    s.append(math.floor(val) if val>0 else math.ceil(val))
        return s.pop()