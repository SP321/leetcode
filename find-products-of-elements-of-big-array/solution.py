class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def bit_count_at_pos(n, bit):
            cur=1<<bit
            cycle=1<<(bit+1)
            total=n+1
            zero_group=total//cycle
            zeroes=zero_group*cur
            rem=total%cycle
            ans=total-zeroes-min(cur,rem)
            return ans

        def bit_count_0n(num):
            return sum(bit_count_at_pos(num,i) for i in range(60))
        
        def two_count_0n(num):
            return sum(bit_count_at_pos(num,i)*i for i in range(60))
        
        def count(k):
            target = bisect_left(range(k), k, key=bit_count_0n)
            rest = k - bit_count_0n(target-1)
            ans = two_count_0n(target-1)
            for i in range(60):
                if target & (1<<i):
                    ans += i
                    rest -= 1
                    if not rest:

                        break
            return ans
        
        return [pow(2,count(high+1)-count(low),mod) for low,high,mod in queries]