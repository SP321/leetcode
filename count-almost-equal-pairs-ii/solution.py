class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
            
        d0=defaultdict(set)
        d1=defaultdict(set)
        d2=defaultdict(set)
        for pos in range(n):
            x=list(str(nums[pos]))
            st=d0[nums[pos]]|d1[nums[pos]]|d2[nums[pos]]
            
            st1=set()
            for i in range(len(x)):
                for j in range(i+1,len(x)):
                    x[i],x[j]=x[j],x[i]
                    cur=int(''.join(x))
                    st1.add(cur)
                    x[i],x[j]=x[j],x[i]

            for cur in st1:
                st|=d0[cur]
                st|=d1[cur]

            for cur in st1:
                d1[cur].add(pos)

            st2=set()
            if len(x)>=4:
                for i,ii,j,jj in permutations(range(len(x)),4):
                        x[i],x[ii]=x[ii],x[i]
                        x[j],x[jj]=x[jj],x[j]
                        cur=int(''.join(x))
                        st2.add(cur)
                        x[i],x[ii]=x[ii],x[i]
                        x[j],x[jj]=x[jj],x[j]
            for cur in st2:
                st|=d0[cur]

            for cur in st2:
                d2[cur].add(pos)
            d0[nums[pos]].add(pos)
            ans+=len(st)
        return ans