class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        c=lcm(a,b)
        def get_pos(x):
            both=x//c
            only_a=x//a - both
            only_b=x//b - both
            return both+only_a+only_b
        return bisect_left(range(int(1e14)),n,key=get_pos)%(int)(1e9+7)