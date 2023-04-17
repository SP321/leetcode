class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x=[]
        for i in tokens:
            if i == "+":
                x.append(x.pop()+x.pop())
            elif i == "-":
                a=x.pop()
                x.append(x.pop()-a)
            elif i == "*":
                x.append(x.pop()*x.pop())
            elif i == "/":
                a=x.pop()
                x.append(int(x.pop()/a))
            else:
                x.append(int(i))
        return x[-1]