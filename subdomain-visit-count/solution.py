class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c=Counter()
        def helper(domain,count):
            c[domain]+=count
            subdomain='.'.join(domain.split('.')[1:])
            if len(subdomain)>0:
                helper(subdomain,count)
        for i in cpdomains:
            count,domain=i.split()
            count=int(count)
            helper(domain,count)
        return [str(val)+" "+index for index,val in c.items()]
