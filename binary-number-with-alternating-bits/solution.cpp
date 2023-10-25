class Solution {
public:
    bool hasAlternatingBits(int n) {
        int cur_bit=n&1;
        while (n){
            n>>=1;
            if ((n&1) == cur_bit)
                return 0;
            cur_bit=n&1;
        }
        return 1;
    }
};