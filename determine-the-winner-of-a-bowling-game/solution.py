class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def countscore(a):
            ans=0
            double=0
            for i in range(len(a)):
                if double>0:
                    ans+=a[i]
                    double-=1
                if a[i]==10:
                    double=2
                ans+=a[i]
            return ans
        s1=countscore(player1)
        s2=countscore(player2)
        if(s1>s2):
         return 1
        if(s2>s1):
         return 2
        return 0
        
        
                    
        