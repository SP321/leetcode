class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        x='\n'.join(source)
        pos=0
        a={
            "//":("\n","\n"),
            "/*":("*/","")
        }
        cur=""
        y=""
        skip_until_end=False
        i=0
        while i<len(x):
            if skip_until_end:
                end,rep=a[cur]
                if x[i:i+len(end)] == end :
                    y=y+rep
                    i+=len(end)-1
                    skip_until_end=False
            else:
                if x[i:i+2] in a:
                    cur=x[i:i+2]
                    st=i
                    i+=1
                    skip_until_end=True
                else:
                    y=y+x[i]
            i+=1

        new_lines=y.split("\n")
        ans=[]
        for line in new_lines:
            if len(line)>0:
                ans.append(line)
        return ans
