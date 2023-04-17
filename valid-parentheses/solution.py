class Solution:
    def isValid(self, s: str) -> bool:
        x=[]
        for i in s:
            if i in ['{','[','(']:
                x.append(i)
            if i =='}':
                if len(x)>0 and x[-1]=='{':
                    x.pop()
                else:
                    return False

            if i ==')':
                if len(x)>0 and x[-1]=='(':
                    x.pop()
                else:
                    return False
            
            if i ==']':
                if len(x)>0 and x[-1]=='[':
                    x.pop()
                else:
                    return False
        
        return len(x)==0