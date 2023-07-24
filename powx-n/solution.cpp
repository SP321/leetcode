class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0)
            return 1;
        if(n == 1)
            return x;
        if(n < 0){
            x = 1 / x;
            if (n == INT_MIN){
                n = -(n + 1);
                return x * x * myPow(x * x, n / 2);
            }
            n = -n;
        }
        double result = myPow(x * x, n / 2);
        if(n % 2)
            result *= x;
        return result;
    }
};