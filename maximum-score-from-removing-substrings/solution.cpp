class Solution {
public:
    int maximumGain(string s, int x, int y) {
        auto helper = [&](string a, int x, int y) {
            int ans = 0;
            vector<char> st;
            for (char ch : s) {
                if (ch == a[1] && !st.empty() && st.back() == a[0]) {
                    st.pop_back();
                    ans += x;
                } else {
                    st.push_back(ch);
                }
            }
            vector<char> st2;
            for (char ch : st) {
                if (ch == a[0] && !st2.empty() && st2.back() == a[1]) {
                    st2.pop_back();
                    ans += y;
                } else {
                    st2.push_back(ch);
                }
            }
            return ans;
        };
        
        if (x > y) {
            return helper("ab", x, y);
        }
        return helper("ba", y, x); 
    }
};