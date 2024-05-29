class Solution {
public:
    int numSteps(std::string s) {
        int carry = 0;
        int ans = 0;
        while (s.size() > 1) {
            int x = s.back() - '0' + carry;
            s.pop_back();
            if (x == 2) {
                carry = 1;
                x = 0;
            }
            if (x == 0) {
                ans += 1;
            } else {
                carry = 1;
                ans += 2;
            }
        }
        return ans + carry;
    }
};