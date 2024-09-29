class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        long long sz = 1;
        vector<int> st;
        for (int x : operations) {
            if (sz > k) break;
            sz*=2;
            st.push_back(x);
       }
       int val = 0;
       while (!st.empty()) {
           int opr = st.back();
           st.pop_back();
           sz/=2;
           if (k > sz) {
               val += opr;
               val %= 26;
               k -= sz;
           }
       }
       return 'a' + val;
    }
};