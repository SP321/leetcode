class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path=[]
        ans=0
        for line in input.split('\n'):
            tab_count=line.count("\t")+1
            cur=line.replace('\t','')
            x=len(cur) 
            while(tab_count<=len(path)):
                path.pop()
            if tab_count>len(path):
                path.append(x)
            if '.' in cur:
                ans=max(ans,sum(path)+len(path)-1)
        return ans
        
                
        
            
            