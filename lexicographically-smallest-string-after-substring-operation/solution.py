class Solution:
    def smallestString(self, s: str) -> str:
        if s.count('a')==len(s):
            return ''.join(['a' for i in range(len(s)-1)]+['z'])
        x=s.split('a')
        for j in range(len(x)):
            if len(x[j])>0:
                x[j]=''.join([chr(ord(i)-1) for i in x[j]])
                break
        return 'a'.join(x)
            
        