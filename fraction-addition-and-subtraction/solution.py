class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        signs=[x for x in expression if x in '-+']
        if expression[0]!='-':
            signs.insert(0,'+')

        fracs=expression.replace('-','+').split('+')
        if fracs[0]=='':
            fracs=fracs[1:]
        a=[tuple(map(int,x.split('/'))) for x in fracs]
        lcm=reduce(math.lcm,[x[-1] for x in a])
        ans=0
        for val,sig in zip(a,signs):
            x,y=val
            if sig=='-':    
                x=-x
            n=lcm//y
            ans+=n*x
        gcd=math.gcd(ans,lcm)
        ans//=gcd
        lcm//=gcd
        if ans==0:
            return "0/1"
        return str(ans)+'/'+str(lcm)