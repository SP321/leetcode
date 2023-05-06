class Solution {
public:
    int divide(int dividend, int divisor) {
        int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;
        uint64_t ans = 0;
        uint64_t abs_dividend = abs(dividend);
        uint64_t abs_divisor = abs(divisor);
        while (abs_dividend >= abs_divisor) {
            int c = 0;
            while (abs_dividend >= (abs_divisor << c))
                c += 1;
            ans += (1 << (c - 1));
            abs_dividend -= abs_divisor << (c - 1);
        }
        return sign == -1 ? -min(ans,(uint64_t)INT_MAX+1) : min(ans,(uint64_t)INT_MAX);
    }
};