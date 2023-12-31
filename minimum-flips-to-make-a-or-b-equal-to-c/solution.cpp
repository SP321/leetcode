class Solution {
public:
    int minFlips(int a, int b, int c) {
        int ans = 0;
        for (int i = 0; i < 31; ++i) {
            int bit_a = (a >> i) & 1;
            int bit_b = (b >> i) & 1;
            int bit_c = (c >> i) & 1;
            
            ans += ((bit_a | bit_b) != bit_c) & bit_c;
            ans += bit_a & (~bit_c);
            ans += bit_b & (~bit_c);
        }
        return ans;
    }
};