int cmp(vector<int> &a, vector<int> &b) {
    if (a[0] == b[0]) {
        return a[1] > b[1];
    }
    return a[0] < b[0];
}
class Solution {
public:
    int numberOfPairs(vector<vector<int>>& P) {
        
       int ret = 0;
        sort(P.begin(), P.end(), cmp);
        for(int i = 0;i < P.size(); ++i) {
            int my = -1100000000;
            for (int j=i+1;j<P.size();++j) {
                auto &x = P[i]; auto &y = P[j];
 
                if (y[1] <= x[1]) {
                    if (y[1] > my) {
                        ++ret;
                        my = y[1];
                    }
                }
            }
        }
        return ret;
    }
};