class Solution {
public:
    int minLength(const std::string& s) {
        stack<char> st;
        for (char x : s) {
            if (!st.empty() && x == 'D' && st.top() == 'C') {
                st.pop();
            } else if (!st.empty() && x == 'B' && st.top() == 'A') {
                st.pop();
            } else {
                st.push(x);
            }
        }
        return st.size();
    }
};
