class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        long left = 0, right = x / 2;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long num = mid * mid;
            if (num < x) {
                left = mid + 1;
            } else if (num > x) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        
        return right;
    }
};