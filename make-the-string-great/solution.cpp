class Solution {
public:
    string makeGood(string s) {
        string st;
        for (auto &c : s) {
            char x= c>='a'?c-('a'-'A'):c+('a'-'A');
            if (not st.empty() and x==st.back()) {
                st.pop_back();
            } else {
                st.push_back(c);
            }
        }
        return st;
    }
};